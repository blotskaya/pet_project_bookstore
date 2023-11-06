import pytest
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.open_book_page()
    category_page = CategoryPage(browser, browser.current_url)
    category_page.should_be_category_url()
    category_page.go_to_product()
    product_page = ProductPage(browser, browser.current_url)
    product_page.product_page_is_opened()
    product_title = product_page.get_product_title()
    product_price = product_page.get_product_price()
    product_page.add_product_to_basket()
    product_page.should_be_notifications()
    product_title_notification = product_page.get_product_title_from_notifications()
    product_price_notification = product_page.get_product_price_from_notifications()
    assert product_title == product_title_notification, \
    f"Product title in notifications {product_title_notification} differs from {product_title}"
    assert product_price == product_price_notification, \
        f"Product title in notifications {product_price_notification} differs from {product_price}"