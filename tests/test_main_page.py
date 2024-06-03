import pytest
import logging
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.main_page import MainPage

logging.basicConfig(level=logging.INFO, format='[%(levelname)s][%(name)s] %(message)s')
logger = logging.getLogger(__name__)


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.feature('Main Page')
class TestMainPage:

    @allure.story('View pizza description')
    @allure.step('Click on pizza image in slider')
    def test_click_on_pizza_image(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        # Шаги
        main_page.click_on_pizza_image()

        # Ожидаемый результат: Пользователь переходит на страницу с описанием выбранной пиццы
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".product_title"))
        )
        current_url = driver.current_url
        logger.info(f"Текущий URL: {current_url}")
        assert "product" in current_url, "Пользователь не перешел на страницу с описанием пиццы"
