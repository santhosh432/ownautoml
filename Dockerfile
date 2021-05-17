# syntax=docker/dockerfile:1
FROM ubuntu:18.04
FROM python:3.6.13-buster


ENV PYTHONUNBUFFERED=1
WORKDIR /ownautoml_app
COPY requirements.txt /ownautoml_app/
RUN pip install -r requirements.txt
COPY . /ownautoml_app/

