from pages.base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def product_page_is_opened(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Product page is not opened"

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def get_product_title(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        return product_title

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def should_be_product_title_notification(self):
        pass

    def should_be_product_price_notification(self):
        pass