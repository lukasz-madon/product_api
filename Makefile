# Variables
DC = docker-compose

build:
	$(DC) build

up:
	$(DC) up --build

down:
	$(DC) down

logs:
	$(DC) logs

migrate:
	$(DC) exec web python manage.py migrate

makemigrations:
	$(DC) exec web python manage.py makemigrations

superuser:
	$(DC) exec web python manage.py createsuperuser

test:
	$(DC) exec web python manage.py test

shell:
	$(DC) exec web python manage.py shell

run:
	$(DC) exec web python manage.py runserver 0.0.0.0:8000

clean:
	$(DC) down --volumes --remove-orphans

.PHONY: build up down logs migrate superuser test shell run clean
