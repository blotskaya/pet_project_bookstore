from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
import allure

class MainPage(BasePage):

    @allure.step("Open login page")
    def go_to_login_page(self):
        """Переходит на страницу логина"""
        login_link = MainPageLocators.LOGIN_LINK
        self.wait.until(EC.element_to_be_clickable(login_link)).click()

    def should_be_login_link(self):
        """Возвращает видимость кнопки логина"""
        return self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login form is not present"

    @allure.step("Open book page")
    def open_book_page(self):
        """Кликает на раздел книг в категориях"""
        books_link = MainPageLocators.BOOKS_LINK
        self.wait.until(EC.element_to_be_clickable(books_link)).click()

