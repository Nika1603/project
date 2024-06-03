import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_bonus_system(driver):
    driver.get("http://pizzeria.skillbox.cc/bonus/")


    time.sleep(2)


    name_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "bonus_username"))
    )
    name_input.send_keys("Veronika Stelmax")


    phone_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "bonus_phone"))
    )
    phone_input.send_keys("74232497778")


    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'woocommerce-form-register__submit')]"))
    )
    submit_button.click()


    success_message = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[@class='woocommerce-bonus-notice woocommerce-bonus-notice--success']"))
    )


    assert success_message.is_displayed(), "Failed to activate bonus data"


    time.sleep(5)

