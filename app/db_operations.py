from peewee import PostgresqlDatabase
from config import database_name, database_user, database_pass
from peewee import Model, CharField, IntegerField, DateTimeField, InternalError, DoesNotExist
from datetime import datetime
db = PostgresqlDatabase(database_name, database_user, database_pass)

class Question(Model):
    pk = IntegerField(primary_key=True)
    text = CharField()
    answer = CharField()
    date_created = DateTimeField(default=datetime.now)
 
    class Meta:
        database = db


def create_question(text, answer, date_created):
    exist = True
    try:
        Question.select().where(Question.text == text.strip()).get()
    except DoesNotExist as de:
        exist = False
 
    if exist:
        row = Question(
            text=text.lower().strip(),
            answer=answer,
            date_created=date_created
        )
        row.save()
        return "Success"
    return "Already exists"
def get_prelast_question():
    exist = True
    last_question = Question.select().order_by(Question.pk.desc()).get()
    try:
        Question.select().where(Question.pk == last_question.pk - 1).get()
    except DoesNotExist as de:
        exist = False
    if exist:
        prelast = Question.select().where(Question.pk == last_question.pk - 1).get()
        return {
            'text' : prelast['text'],
            'answer' : prelast['answer'],
            'date_created' : prelast['date_created']
        }
    return {}