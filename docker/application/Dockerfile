FROM python:3.10

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt update && apt upgrade -y
RUN apt install -y python3-pip
RUN pip3 install pipenv
COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pipenv install --system --deploy

# copy project
COPY . .
