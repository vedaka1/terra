FROM python:3.11-buster

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

COPY requirements.txt .
COPY .env.test .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src/ .
RUN chmod a+x /app/src/app.sh