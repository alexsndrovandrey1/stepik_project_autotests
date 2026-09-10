from selenium.webdriver.common.by import By


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages .alert-info strong")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")