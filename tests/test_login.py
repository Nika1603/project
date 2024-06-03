import pytest
import allure
from selenium import webdriver
from pages.my_account_page import MyAccountPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.feature('User Login')
class TestUserLogin:

    @allure.story('Login with registered user credentials')
    @allure.step('Login with registered user credentials')
    def test_login_registered_user(self, driver):
        my_account_page = MyAccountPage(driver)
        my_account_page.open_my_account_page()


        username = "Veronika Stelmax"
        password = "Ника1603!!!"
        my_account_page.login(username, password)


        assert my_account_page.is_user_logged_in(), "Пользователь не был успешно залогинен"
        input()
