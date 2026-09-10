from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_correct_product_name(self, expected_name):
        actual_name = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE
        ).text

        assert actual_name == expected_name, (
            f"Название товара не совпадает.\n"
            f"Ожидалось: '{expected_name}'\n"
            f"Получено: '{actual_name}'"
        )


    def should_be_correct_product_price(self, expected_price):
        actual_price = self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE
        ).text

        assert actual_price == expected_price, (
            f"Стоимость товара не совпадает.\n"
            f"Ожидалось: '{expected_price}'\n"
            f"Получено: '{actual_price}'"
        )
    
    def get_product_name(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text


    def get_product_price(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text
        