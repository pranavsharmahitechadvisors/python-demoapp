import os
from driverfactory import make_driver
from home_page import HomePage

selenium_hub = os.environ["SELENIUM_HUB"]
app_url = os.environ["APP_URL"]


def test_selenium_remote():
    driver = make_driver(SELENIUM_HUB=selenium_hub, remote=True, vnc=True, headless=False)
    try:
        app = HomePage(driver, url=app_url)
        app.show_info()
    finally:
        driver.quit()
