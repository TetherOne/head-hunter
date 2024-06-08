FROM python:3.11.6-bookworm

ENV PYTHONUNBUFFERED=1

WORKDIR /head-hunter

RUN pip install --upgrade pip "poetry==1.6.1"
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY . .