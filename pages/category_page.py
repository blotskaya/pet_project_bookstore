from pages.base_page import BasePage
from .locators import CategoryPageLocators
from random import choice

class CategoryPage(BasePage):
    def should_be_category_url(self):
        category_url = "category"
        assert category_url in self.browser.current_url, f"Category link does not contain {category_url}"

    def go_to_product(self):
        product_link = choice(self.browser.find_elements(*CategoryPageLocators.PRODUCT_LINK))
        product_link.click()