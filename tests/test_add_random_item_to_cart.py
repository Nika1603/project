import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_add_random_item_to_cart(driver):

    driver.get("http://pizzeria.skillbox.cc/")
    time.sleep(2)

    driver.get("http://pizzeria.skillbox.cc/product-category/menu/")
    time.sleep(2)

    products = driver.find_elements(By.CLASS_NAME, "product")
    random_product = random.choice(products)
    add_to_cart_button = random_product.find_element(
        By.CLASS_NAME, "add_to_cart_button"
    )
    add_to_cart_button.click()
    time.sleep(2)

    driver.get("http://pizzeria.skillbox.cc/cart/")
    time.sleep(2)

    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) > 0, "Корзина пуста, товар не был добавлен"

    time.sleep(5)
