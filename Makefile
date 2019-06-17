PY=pipenv run python
ENV=pipenv run
MANAGE=pipenv run python manage.py
test: collectstatic
	$(ENV) pytest -vv $(PYTEST_ARGS)
collectstatic:
	rm -r ./staticfiles |:
	$(MANAGE) collectstatic
run:
	$(MANAGE) runserver
migrate:
	for app in snekbook accounts; \
		do $(MANAGE) migrate snekbook ; \
	done ; $(MANAGE) migrate
black:
	$(ENV) black .