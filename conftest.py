import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from time import sleep

@pytest.fixture(scope="function")
def browser():
    service = Service(executable_path=GeckoDriverManager().install())
    browser = webdriver.Firefox(service=service)
    yield browser
    sleep(5)
    browser.quit()

@pytest.fixture
def base_url():
    return "http://selenium1py.pythonanywhere.com/"
