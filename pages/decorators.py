from .main_page import MainPage
from .login_page import LoginPage
from functools import wraps


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