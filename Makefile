PY=pipenv run python
ENV=pipenv run
MANAGE=pipenv run python manage.py
test:
	$(MANAGE) test -v 1
run:
	$(MANAGE) runserver
migrate:
	for app in snekbook accounts; \
		do $(MANAGE) migrate snekbook ; \
	done ; $(MANAGE) migrate
black:
	$(ENV) black .