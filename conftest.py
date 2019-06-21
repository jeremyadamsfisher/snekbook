import pytest
import os, sys
from selenium import webdriver
import django.contrib.auth as dj_auth

sys.path.append(os.path.dirname(__file__))


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def seed_user():
    username, password = "admin", "123"
    dj_auth.get_user_model().objects.create_user(username=username, password=password)
    return username, password
