PY=pipenv run python
ENV=pipenv run
MANAGE=pipenv run python manage.py
test:
	$(ENV) pytest --driver Chrome
run:
	$(MANAGE) runserver
update_deps:
	pipenv lock --pre --dev \
	&& pipenv sync \
	&& pipenv lock --requirements > requirements.txt
migrate:
	for app in snekbook admin ; do \
		$(MANAGE) migrate "$$app" ; \
	done
makemigrations:
	$(MANAGE) makemigrations
makeandmigrate: makemigrations migrate