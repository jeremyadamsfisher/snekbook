PY=pipenv run python
ENV=pipenv run
MANAGE=pipenv run python manage.py
test:
	$(MANAGE) test 
run:
	$(MANAGE) runserver
migrate:
	$(MANAGE) migrate snekbook
	$(MANAGE) migrate
black:
	$(PY) black .