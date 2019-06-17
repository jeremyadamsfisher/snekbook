PY=pipenv run python
ENV=pipenv run
MANAGE=pipenv run python manage.py
test:
	$(MANAGE) test 
run:
	$(MANAGE) runserver
update_deps:
	pipenv lock --pre --dev \
	&& pipenv sync \
	&& pipenv lock --requirements > requirements.txt
migrate:
	$(MANAGE) migrate snekbook
	$(MANAGE) migrate
makemigrations:
	$(MANAGE) makemigrations
makeandmigrate: makemigrations migrate
black:
	$(PY) black .