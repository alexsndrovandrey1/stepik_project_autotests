from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS
        ), "В корзине присутствуют товары"

    def should_be_empty_message(self):
        assert "Your basket is empty" in self.browser.page_source, (
            "Не найден текст о том, что корзина пуста"
        )