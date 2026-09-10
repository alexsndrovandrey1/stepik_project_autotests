import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nЗапуск браузера Chrome")
    browser = webdriver.Chrome()

    yield browser

    print("\nЗакрытие браузера")
    browser.quit()