FROM python:3.11.4-slim

RUN mkdir /job-hunter

WORKDIR /job-hunter

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .