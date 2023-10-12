FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

ADD . /app/
COPY requirements.txt .
COPY .env .

RUN pip install -r requirements.txt

