.PHONY: install lint format test up down migrate typecheck build push

install:
	pip install -r requirements.txt

lint:
	black .
	isort .
	flake8 .

format:
	black .
	isort .

test:
	pytest

typecheck:
	mypy src

up:
	docker-compose up -d --build

down:
	docker-compose down

migrate:
	alembic upgrade head

build:
	docker build -t yourdockerhubusername/clinic-appointments:latest .

push:
	docker push yourdockerhubusername/clinic-appointments:latest
