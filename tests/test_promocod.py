import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import allure


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.feature("Add and Remove from Cart")
@allure.story("Add and remove random item from cart with applying promo code")
def test_add_and_remove_with_promo_code(driver):
    with allure.step("Open main page"):
        driver.get("http://pizzeria.skillbox.cc/")
        time.sleep(2)

    with allure.step("Go to menu page"):
        driver.get("http://pizzeria.skillbox.cc/product-category/menu/")
        time.sleep(2)

    with allure.step("Add random item to cart"):
        products = driver.find_elements(By.CLASS_NAME, "product")
        random_product = random.choice(products)
        add_to_cart_button = random_product.find_element(
            By.CLASS_NAME, "add_to_cart_button"
        )
        add_to_cart_button.click()
        time.sleep(2)

    with allure.step("Go to cart page"):
        driver.get("http://pizzeria.skillbox.cc/cart/")
        time.sleep(2)

    with allure.step("Apply promo code"):
        promo_code_input = driver.find_element(By.ID, "coupon_code")
        promo_code_input.clear()
        promo_code_input.send_keys("DC120")
        apply_coupon_button = driver.find_element(
            By.CSS_SELECTOR, ".button[name='apply_coupon']"
        )
        apply_coupon_button.click()
        time.sleep(2)

    with allure.step("Remove item from cart"):
        remove_buttons = driver.find_elements(By.CLASS_NAME, "remove")
        assert len(remove_buttons) > 0, "Cart is empty, nothing to remove"
        remove_buttons[0].click()
        time.sleep(2)

    with allure.step("Verify cart is empty"):
        empty_cart_message = driver.find_element(By.CSS_SELECTOR, ".cart-empty")
        assert (
            empty_cart_message.is_displayed()
        ), "Cart is not empty, item was not removed"
        time.sleep(2)
