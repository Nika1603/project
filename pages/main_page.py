from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import logging


class MainPage:
    URL = "https://pizzeria.skillbox.cc/"

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def open_main_page(self):
        self.logger.info("Открытие главной страницы")
        self.driver.get(self.URL)

    def click_on_pizza_image(self):
        self.logger.info("Ожидание загрузки главной страницы")
        WebDriverWait(self.driver, 30).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        self.logger.info("Ожидание видимости изображения пиццы в слайдере")
        pizza_image = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='']"))
        )

        self.logger.info("Наведение мыши на изображение пиццы")
        ActionChains(self.driver).move_to_element(pizza_image).perform()

        self.logger.info("Ожидание, что изображение пиццы станет кликабельным")
        pizza_image = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='']"))
        )

        self.logger.info("Клик на изображение пиццы")
        pizza_image.click()
