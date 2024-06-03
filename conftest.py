import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    # Инициализируем экземпляр WebDriver (например, Chrome, Firefox)
    driver = webdriver.Chrome()
    yield driver
    # Завершаем работу - закрываем экземпляр WebDriver
    driver.quit()
