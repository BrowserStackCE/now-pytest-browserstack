import pytest
from selenium import webdriver
import os

@pytest.fixture
def selenium():
    """
    Replacement for the old pytest-selenium 'selenium' fixture.
    Works with BrowserStack or local Chrome.
    """

    # Check if using BrowserStack
    username = os.environ.get("BROWSERSTACK_USERNAME")
    access_key = os.environ.get("BROWSERSTACK_ACCESS_KEY")

    if username and access_key:
        remote_url = "https://hub.browserstack.com/wd/hub"

        options = webdriver.ChromeOptions()
        options.set_capability("browserName", "Chrome")
        options.set_capability("browserVersion", "latest")

        # Add any custom BrowserStack caps here
        options.set_capability("bstack:options", {
            "os": "OS X",
            "osVersion": "Ventura",
            "sessionName": "Python Pytest Example"
        })

        driver = webdriver.Remote(
            command_executor=remote_url,
            options=options
        )
    else:
        # Local fallback
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()
