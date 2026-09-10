import pytest
from selenium import webdriver

def pytest_addoption(parser):
    """Добавляем параметр --language в командную строку pytest"""
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language, e.g. --language=es or --language=fr"
    )

@pytest.fixture(scope="function")
def browser():
    print("\nЗапуск браузера Chrome")
    browser = webdriver.Chrome()

    yield browser

    print("\nЗакрытие браузера")
    browser.quit()