PY=pipenv run python
ENV=pipenv run
MANAGE=pipenv run python manage.py
test:
	$(MANAGE) test 
run:
	$(MANAGE) runserver
migrate:
	for app in snekbook accounts; \
		do $(MANAGE) migrate snekbook ; \
	done ; $(MANAGE) migrate
black:
	$(PY) black .