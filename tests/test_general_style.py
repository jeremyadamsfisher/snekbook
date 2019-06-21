import time


def test_always_shows_snekbook(driver, live_server):
    driver.get(live_server.url)
    time.sleep(1)
    assert "snekbook" in driver.title
