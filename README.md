# Docker-Django-REST-API

This is a small REST API that I create in order to practice my skills in Django and Docker.

## Installation
Requirements
- You need to have [Docker](https://docs.docker.com/engine/installation/) and [Docker Compose](https://docs.docker.com/compose/install/) installed

## Run

Type in root folder,
~~~
cp .env.example .env
docker-compose build && docker-compose up -d
~~~~

Type http://127.0.0.1:8000/api/persons/ in your browser in order to check it
```
login as
username:admin
password:admin
```

## Stop 

Type in the root foldier,
```
docker-compose down
```
