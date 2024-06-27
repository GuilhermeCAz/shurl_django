include .env
export

# container
.PHONY: up
up:
	docker-compose up --build --detach

.PHONY: down
down:
	docker-compose down

.PHONY: restart
restart: down up

.PHONY: logs
logs:
	docker-compose logs

.PHONY: watch
# Use on a different terminal for live updates on container files
watch:
	docker-compose watch

# django
.PHONY: migrate
migrate:
	docker-compose run web python manage.py makemigrations
	docker-compose run web python manage.py migrate

.PHONY: superuser
superuser:
	docker-compose run web python manage.py createsuperuser --noinput

.PHONY: collectstatic
collectstatic:
	docker-compose run web python manage.py collectstatic --noinput

# python
.PHONY: dependencies
dependencies:
	python -m pip install --upgrade pip
	pip install -r requirements-dev.txt

.PHONY: requirements
requirements:
	pip-compile -o requirements.txt --strip-extras
	pip-compile -o requirements-dev.txt --strip-extras --extra=dev

.PHONY: help
help:
	@echo Available targets:
	@echo up               : Build and start containers (docker-compose up)
	@echo down             : Stop and remove containers (docker-compose down)
	@echo restart          : Restart containers
	@echo logs             : Show container logs
	@echo migrate          : Run Django migrations
	@echo superuser        : Create Django superuser
	@echo collectstatic    : Collect static files
	@echo dependencies     : Install dependencies
	@echo requirements     : Compile requirements files
	@echo help             : Show this help message

.DEFAULT_GOAL := help