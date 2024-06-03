from selenium.webdriver.common.by import By
import random

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://pizzeria.skillbox.cc/cart"
        self.apply_promo_code_button = (By.ID, "promo_code_button")
        self.checkout_button = (By.ID, "checkout_button")
        self.order_total_locator = (By.ID, "order_total")
        self.promo_code_input = (By.ID, "promo_code")

    def open(self):
        self.driver.get(self.url)

    def apply_promo_code(self, promo_code):
        promo_code_input = self.driver.find_element(*self.promo_code_input)
        promo_code_input.clear()
        promo_code_input.send_keys(promo_code)
        apply_button = self.driver.find_element(*self.apply_promo_code_button)
        apply_button.click()

    def get_order_total(self):
        order_total_element = self.driver.find_element(*self.order_total_locator)
        return float(order_total_element.text.strip('$'))

    def get_available_items(self):
        return self.driver.find_elements(By.CLASS_NAME, "product-item")

    def add_item_to_cart(self, item):
        add_to_cart_button = item.find_element(By.CLASS_NAME, "add-to-cart")
        add_to_cart_button.click()

    def add_random_items_to_cart(self):
        items = self.get_available_items()
        if items:
            random_items = random.sample(items, k=random.randint(1, len(items)))
            for item in random_items:
                self.add_item_to_cart(item)
        else:
            print("Список товаров пустой. Невозможно добавить товары в корзину.")

    def proceed_to_checkout(self):
        checkout_button = self.driver.find_element(*self.checkout_button)
        checkout_button.click()

    def verify_order_total_with_discount(self, discount_percent):
        order_total = self.get_order_total()
        expected_total = order_total * (1 - discount_percent / 100)
        return round(expected_total, 2) == round(self.get_order_total(), 2)

