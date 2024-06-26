include .env
export

up:
	docker-compose up --build --detach

migrate:
	docker-compose run web python manage.py makemigrations
	docker-compose run web python manage.py migrate

superuser:
	docker-compose run web python manage.py createsuperuser --noinput

collectstatic:
	docker-compose run web python manage.py collectstatic --noinput

down:
	docker-compose down

logs:
	docker-compose logs

requirements:
	pip-compile -o requirements.txt --strip-extras
	pip-compile -o requirements-dev.txt --strip-extras --extra=dev
