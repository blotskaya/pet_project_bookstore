import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

@pytest.fixture(scope="function", autouse=True)
def browser():
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    yield browser
    sleep(5)
    browser.quit()

@pytest.fixture
def base_url():
    return "http://selenium1py.pythonanywhere.com/"
