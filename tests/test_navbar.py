import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_logged_in_view_shows_users_name_pytest(seed_user, client):
    username, password = seed_user

    response = client.get(reverse("home"))
    assert username not in response.content.decode("utf-8")
    client.login(username=username, password=password)
    response = client.get(reverse("home"))
    assert username in response.content.decode("utf-8")
