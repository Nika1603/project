import logging
import logging.config
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
import allure
import time


logging.config.fileConfig("../logging.conf")
logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def browser():

    driver = webdriver.Chrome()
    yield driver

    time.sleep(10)
    driver.quit()


def test_slider_presence(browser):
    try:

        url = "https://pizzeria.skillbox.cc/"
        logger.info(f"Открытие страницы: {url}")
        browser.get(url)
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Main Page",
            attachment_type=AttachmentType.PNG,
        )

        slider_selector = "div[class*='slick-slider']"
        logger.info("Поиск элемента слайдера с пиццами")
        slider = browser.find_element(By.CSS_SELECTOR, slider_selector)

        assert (
            slider.is_displayed()
        ), "Слайдер с пиццами не отображается на главной странице"
        logger.info("Слайдер с пиццами отображается на главной странице")
    except Exception as e:
        logger.error(f"Ошибка в тесте: {e}")
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
