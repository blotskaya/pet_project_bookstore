from .base_page import BasePage
from selenium.webdriver.common.by import By
from typing import Tuple


class Component(BasePage):
    def __init__(self, browser, *locator):
        super().__init__(browser)
        self.by, self.what = locator

    def fill_input(self, value):
        input = self.browser.find_element(self.by, self.what)
        input.click()
        input.send_keys(value)


