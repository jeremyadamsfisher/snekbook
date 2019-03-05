PY=pipenv run python
ENV=pipenv run
MANAGE=pipenv run python manage.py
test:
	$(ENV) pytest --driver Chrome
run:
	$(MANAGE) runserver
