FROM python:3.9
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install --upgrade pip -r requirements.txt
COPY ./app /app
EXPOSE 5000