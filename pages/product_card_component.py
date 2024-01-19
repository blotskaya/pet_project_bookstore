from .base_page import BasePage
from .locators import ProductCardComponentLocators
from random import choice

class ProductCardComponent(BasePage):

    def go_to_product(self):
        product_link = choice(self.browser.find_elements(*ProductCardComponentLocators.PRODUCT_LINK))
        product_link.click()
