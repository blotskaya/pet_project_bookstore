from pages.base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def product_page_is_opened(self):
        """Проверяет переход на страницу продукта"""
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Product page is not opened"

    def is_product_unavailable(self):
        """Возвращает видимость уведомления о недоступности продукта"""
        return self.is_element_present(*ProductPageLocators.UNAVAILABILITY_ALERT)

    def add_product_to_basket(self):
        """Добавляет продукт в корзину"""
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def get_product_title(self):
        """Возвращает тайтл продукта"""
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        return product_title

    def get_product_price(self):
        """Возвращает цену продукта"""
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def should_be_notifications(self):
        """Возвращает видимость уведомления о добавлении продукта в корзину"""
        assert self.is_element_present(*ProductPageLocators.NOTIFICATION), "There are no notifications"

    def get_product_title_from_notifications(self):
        """Возвращает тайтл продукта из уведомления о добавлении продукта в корзину"""
        product_title_notifications = self.browser.find_elements(*ProductPageLocators.NOTIFICATION)[0].text
        return product_title_notifications

    def get_product_price_from_notifications(self):
        """Возвращает цену продукта из уведомления о добавлении продукта в корзину"""
        product_price_notifications = self.browser.find_elements(*ProductPageLocators.NOTIFICATION)[-1].text
        return product_price_notifications
