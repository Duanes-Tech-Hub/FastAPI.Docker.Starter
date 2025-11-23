FROM python:3.13.9-slim

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt