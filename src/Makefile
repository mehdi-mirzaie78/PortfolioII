install:
	# intall dependencies
	pip install --upgrade pip && pip install -r requirements.txt

format:
	# format code
	black *.py */*.py

lint:
	# flake8 or Pylint
	pylint --disable=R,C *.py

makemigrations:
	# make migrations
	python manage.py makemigrations

cleanmigrations:
	# clean migrations
	find -wholename "*/migrations/*.py" -not -name "__init__.py" -delete

migrate:
	# migrate
	python manage.py migrate

all: install format makemigrations migrate

run:
	python manage.py runserver