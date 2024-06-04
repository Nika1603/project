from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyAccountPage:
    URL = "http://pizzeria.skillbox.cc/my-account/"

    def __init__(self, driver):
        self.driver = driver

    def open_my_account_page(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        username_field = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
        password_field = self.driver.find_element(By.ID, "password")

        username_field.send_keys(username)
        password_field.send_keys(password)

        login_button = self.driver.find_element(
            By.CSS_SELECTOR, "button.woocommerce-button"
        )
        login_button.click()

    def is_user_logged_in(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".woocommerce-MyAccount-content")
                )
            )
            return True
        except:
            return False
