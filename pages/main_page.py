from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
import allure

class MainPage(BasePage):

    @allure.step("Open login page")
    def go_to_login_page(self):
        """Переходит на страницу логина"""
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        """Возвращает видимость кнопки логина"""
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def open_book_page(self):
        """Кликает на раздел книг в категориях"""
        books_link = self.browser.find_element(*MainPageLocators.BOOKS_LINK)
        books_link.click()

