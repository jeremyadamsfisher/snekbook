PY=pipenv run python
ENV=pipenv run
MANAGE=pipenv run python manage.py
test: collectstatic
	$(ENV) pytest --driver Safari -v $(PYTEST_ARGS)
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
			apps/*/*.py \
			tests/*.py
deploy: test
	$(MANAGE) runserver \
	&& git push origin master \
	&& git push heroku master