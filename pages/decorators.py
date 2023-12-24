from pages.main_page import MainPage
from pages.login_page import LoginPage
from functools import wraps
from .locators import LoginPageLocators


def registered_user(func):
    @wraps(func)
    def wrapper(browser, base_url):
        page = MainPage(browser)
        page.open(base_url)
        page.go_to_login_page()
        login_page = LoginPage(browser)
        login_page.login()
        func(browser, base_url)
    return wrapper