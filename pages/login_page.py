
import time
import allure
from selenium.webdriver.common.by import By
from utils.waits import wait_for_element
from utils.base_page import BasePage

class LoginPage(BasePage):
    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver
    username_input = (By.XPATH, "//input[@id='emailOrPhone']")
    password_input = (By.XPATH, "//input[@data-testid='password']")
    login_button = (By.XPATH, "//button[@data-testid='submitBtn']")

    @allure.step("Log in with username: {username}")
    def do_login(self, username, password):
        wait_for_element(self.driver, self.username_input).send_keys(username)
        wait_for_element(self.driver, self.login_button).click()
        wait_for_element(self.driver, self.password_input).send_keys(password)
        wait_for_element(self.driver, self.login_button).click()
        time.sleep(5)  # Ideally use WebDriverWait here

        # def do_login(self, username, password):
        #  #        self.send_keys(self.username_input, username)   # ✅ uses BasePage's send_keys
        #  #        self.send_keys(self.password_input, password)   # ✅ uses BasePage's send_keys
        #  #        self.click_element(self.login_button)           # ✅ uses BasePage's click_element

    @allure.step("Get login error message")
    def get_error_message(self):
        error_locator = (By.XPATH, '//p[contains(text(), "Email or Password is incorrect")]')
        return wait_for_element(self.driver, error_locator).text

