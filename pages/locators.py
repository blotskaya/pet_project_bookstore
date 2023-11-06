from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BOOKS_LINK = (By.CSS_SELECTOR, '[class="dropdown-submenu"]')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "[class*='btn-add-to-basket']")
    NOTIFICATION = (By.XPATH, '//div[@class="alertinner "]//strong')
    PRODUCT_TITLE = (By.XPATH, '//div[contains(@class,"product_main")]/h1')
    PRODUCT_PRICE = (By.XPATH, '//div[contains(@class,"product_main")]/p[@class="price_color"]')

class CategoryPageLocators():
    PRODUCT_LINK = (By.XPATH, '//article[@class="product_pod"]//h3/a')