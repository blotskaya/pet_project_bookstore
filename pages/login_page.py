from .base_page import BasePage
from .locators import LoginPageLocators
from ..consts import Login
from .page_factory import Component

login_consts = Login
login = login_consts.LOGIN
password = login_consts.PASSWORD

class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.input_login = Component(browser, *LoginPageLocators.LOGIN_INPUT)
        self.input_password = Component(browser, *LoginPageLocators.PASSWORD_INPUT)

    def should_be_login_page(self):
        """Проверяет переход на страницу логина"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверяет ожидаемый урл логина"""
        login_url = "login"
        assert login_url in self.browser.current_url, f"Login link does not contain {login_url}"

    def should_be_login_form(self):
        """Возвращает видимость формы логина"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        """Возвращает видимость формы регистрации"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register link is not presented"

    def login(self):
        self.input_login.fill_input(login)
        self.input_password.fill_input(password)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

