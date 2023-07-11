FROM python:3.11-alpine3.17

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apk del build-deps

COPY . /app/

COPY run_django.sh .
ENTRYPOINT [ "./run_django.sh" ]