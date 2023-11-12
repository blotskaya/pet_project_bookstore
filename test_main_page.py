from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from pages.product_card_component import ProductCardComponent
from pytest import skip

def test_guest_should_see_login_link(browser, base_url):
    page = MainPage(browser, base_url)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser, base_url):
    page = MainPage(browser, base_url)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_can_add_product_to_basket(browser, base_url):
    page = MainPage(browser, base_url)
    page.open()
    page.open_book_page()
    category_page = CategoryPage(browser, browser.current_url)
    category_page.should_be_category_url()
    product_card_component = ProductCardComponent(browser, browser.current_url)
    product_card_component.go_to_product()
    product_page = ProductPage(browser, browser.current_url)
    product_page.product_page_is_opened()
    product_title = product_page.get_product_title()
    if product_page.is_product_unavailable():
        message = 'Product is unavailable'
        skip(message)
    product_price = product_page.get_product_price()
    product_page.add_product_to_basket()
    product_page.should_be_notifications()
    product_title_notification = product_page.get_product_title_from_notifications()
    product_price_notification = product_page.get_product_price_from_notifications()
    assert product_title == product_title_notification and product_price == product_price_notification, \
    f"Expected product title in notifications {product_title}, got {product_title_notification}," \
    f"expected product price in notifications {product_price_notification}, got {product_price}"