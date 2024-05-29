FROM python:3.11.4-slim

RUN mkdir /head-hunter

WORKDIR /head-hunter

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .