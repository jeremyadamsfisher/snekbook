import time


def test_functional(selenium, live_server):
    selenium.get(live_server.url)
    assert "Snekbook" in selenium.title
