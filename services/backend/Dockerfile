FROM python:3.11-alpine

RUN mkdir app
WORKDIR /app

ENV PYTHONPATH=.

COPY requirements.txt ./
COPY .env.test .env ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src/ .
