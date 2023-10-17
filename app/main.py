from flask import Flask, request, jsonify   
from db_operations import get_prelast_question, create_question, db, Question
from marshmallow import Schema, fields, ValidationError
from json import loads, dumps
import requests as req


class BaseSchema(Schema):
    questions_num = fields.Integer(required=True)
    
def add_to_db(json_str:str):
    num = loads(json_str)['questions_num']
    resp = req.get(f'https://jservice.io/api/random?count={num}')
    data = resp.json()
    create_question(text=data['question'], answer=data['answer'], date_created=data['created_at'])
    return get_prelast_question()

app = Flask(__name__)

@app.route("/", methods=["POST"])
def main():
    request_data = request.json
    schema = BaseSchema()
    try:
        result = schema.load(request_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    data_now_json_str = dumps(result)

    response_data = add_to_db(data_now_json_str)

    return jsonify(response_data), 200
 

if __name__ == '__main__':
    try:
        db.connect()
        Question.create_table()
    except InternalError as px:
        print(str(px)) 
    app.run(debug=True)