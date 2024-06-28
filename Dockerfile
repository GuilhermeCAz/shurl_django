FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt /app/

RUN python -m pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

COPY . /app/
