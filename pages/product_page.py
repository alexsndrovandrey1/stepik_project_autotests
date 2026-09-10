from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_correct_product_name(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text

        success_name = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE
        ).text

        assert product_name == success_name, \
            "Название товара не совпадает"

    def should_be_correct_product_price(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text

        basket_price = self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE
        ).text

        assert product_price == basket_price, \
            "Стоимость корзины не совпадает"