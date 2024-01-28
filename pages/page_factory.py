from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Component(BasePage):
    def __init__(self, browser, *locator):
        super().__init__(browser)
        self.wait = WebDriverWait(browser, 10, poll_frequency=1)
        self.by, self.what = locator

    def fill_input(self, value):
        input = self.browser.find_element(self.by, self.what)
        self.wait.until(EC.element_to_be_clickable(input)).click()
        input.send_keys(value)




