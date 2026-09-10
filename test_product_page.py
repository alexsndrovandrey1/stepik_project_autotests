from selenium import webdriver
from pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket():
    browser = webdriver.Chrome()

    try:
        page = ProductPage(browser, link)
        page.open()

        page.add_product_to_basket()

        page.solve_quiz_and_get_code()

        page.should_be_correct_product_name()
        page.should_be_correct_product_price()

    finally:
        browser.quit()