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
makemigrations:
	$(MANAGE) makemigrations
black:
	$(ENV) black .
lint:
	$(ENV) pylint \
			--load-plugins pylint_django \
			--load-plugins pylint_django.checkers.db_performance \
			--disable=line-too-long \
			--disable=missing-docstring \
			apps/*/*.py
deploy: test
	git push origin master \
	&& git push heroku master