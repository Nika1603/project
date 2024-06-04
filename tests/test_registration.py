import pytest
import allure
from selenium import webdriver
from pages.my_account_page import MyAccountPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.feature("User Registration")
class TestUserRegistration:

    @allure.story("Register a new user")
    @allure.step("Register a new user with valid details")
    def test_register_new_user(self, driver):
        my_account_page = MyAccountPage(driver)
        my_account_page.open_my_account_page()

        my_account_page.click_register_button()

        username = "Veronika Stelmax"
        email = "stelmax.nika@mail.ru"
        password = "Ника1603!!!"
        my_account_page.register_new_user(username, email, password)

        confirmation_message = my_account_page.get_registration_confirmation()
        assert (
            "Thank you for registering" in confirmation_message
        ), "Регистрация не была успешной"
