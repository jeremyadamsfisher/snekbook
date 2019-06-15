PY=pipenv run python
ENV=pipenv run
MANAGE=pipenv run python manage.py
test:
	$(ENV) pytest --driver Chrome
run: secrets
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
secrets:
	$(MAKE) -f secrets