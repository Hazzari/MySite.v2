# start from an official image
FROM python:3.8.5-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install our two dependencies
COPY ./Pipfile.lock .
COPY ./Pipfile .


RUN pip install --upgrade pip \
    && pip install pipenv \
    && pipenv install --system --deploy --ignore-pipfile



