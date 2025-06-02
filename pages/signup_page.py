from selenium.webdriver.common.by import By
from utils.base_page import BasePage
from utils.waits import wait_for_element
import time

class SignupPage(BasePage):
    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver
    EMAIL_INPUT = (By.XPATH, '//input[@data-testid="workEmail"]')# ✅ Email input
    COMPANY_INPUT = (By.XPATH, '//input[@spellcheck="false"]') # ✅ Company name input
    SIGNUP_BUTTON = (By.XPATH, '//button[@data-testid="submitBtn"]')# ✅ Signup button

    def do_signup(self, email, company_name):
        wait_for_element(self.driver, self.EMAIL_INPUT).send_keys(email)
        wait_for_element(self.driver, self.SIGNUP_BUTTON).click()
        # wait_for_element(self.driver, self.COMPANY_INPUT).send_keys(company_name)
        # wait_for_element(self.driver, self.SIGNUP_BUTTON).click()
        time.sleep(5)  # Ideally use WebDriverWait here
