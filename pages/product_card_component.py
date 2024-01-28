from .base_page import BasePage
from .locators import ProductCardComponentLocators
from random import choice
from selenium.webdriver.support import expected_conditions as EC
import allure

class ProductCardComponent(BasePage):

    @allure.step("Go to product page")
    def go_to_product(self):
        product_link = choice(self.browser.find_elements(*ProductCardComponentLocators.PRODUCT_LINK))
        self.wait.until(EC.element_to_be_clickable(product_link)).click()
