# Shurl

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Django CI](https://github.com/GuilhermeCAz/shurl_django/actions/workflows/django.yaml/badge.svg)](https://github.com/GuilhermeCAz/shurl_django/actions/workflows/django.yaml)
[![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FGuilhermeCAz%2Fshurl_django%2Fmain%2Fpyproject.toml&logo=python&label=Python)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-%23092E20?logo=django)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-%232496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-%234169E1?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Make](https://img.shields.io/badge/Make-%236D00CC?logo=make)](https://www.gnu.org/software/make/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![OpenAPI](https://img.shields.io/badge/OpenAPI-%2385EA2D?logo=swagger&logoColor=white&color=null)](https://swagger.io/specification/)
[![Github Actions](https://img.shields.io/badge/GitHub%20Actions-%232088FF?logo=githubactions&logoColor=white)](https://github.com/features/actions)

Shurl is a URL shortening application built with Django. It allows users to create short URLs for their long URLs.

## Features

- Shorten long URLs
- Redirect to the original URL using the shortened URL
- User authentication and registration // _TODO_
- URL statistics // _TODO_

## Project Setup

Clone this repository:

```sh
git clone https://github.com/GuilhermeCAz/shurl_django.git
cd shurl_django
```

Create a .env file according to .env.example.

To build the Docker images and start the project in detached mode, use the following command:

```sh
docker compose up --build --detach
```

Using Make:

```sh
make up
```

Make Migrations

```sh
docker compose run web python manage.py makemigrations
docker compose run web python manage.py migrate
```

Using Make:

```sh
make migrate
```

**Optional**: To create a superuser for the Django admin, run:

```sh
docker compose run web python manage.py createsuperuser --noinput
```

Using Make:

```sh
make superuser
```

You'll need to set the necessary environment variables for the superuser credentials beforehand.

## Usage

1. Visit the Shurl homepage: `http://localhost:8000`
2. Paste a long URL into the input field and click "Shorten".
3. Copy the shortened URL and use it to share with others.
4. Click the shortened URL to be redirected to the original URL.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Installation (for development only)

Create .venv

```shell
python -m venv .venv
```

Activate the virtual environment

```shell
.venv/scripts/activate
```

Install dependencies

```shell
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
