import time

import allure
# import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def search_element(self, locator):  # 👉 locator = (By.ID, "username") OR (By.XPATH, "//input[@id='email']")
        return self.driver.find_element(*locator)

    def click_element(self, locator):  # 👉 locator = the element you want to click
        self.search_element(locator).click()

    def send_keys(self, locator, text):  # 👉 locator = field; text = what you want to type
        self.search_element(locator).send_keys(text)

    def select_dropdown_by_index(self, locator, index=2):  # 👉 locator = dropdown element; index = dropdown item
        Select(self.search_element(locator)).select_by_index(index)

    def wait_until_clickable(self, locator, timeout=20):  # 👉 locator = element you want to wait for click
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_until_visible(self, locator, timeout=30):  # 👉 locator = element that should appear
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_until_invisible(self, locator, timeout=25):  # 👉 locator = loading icon/spinner that should disappear
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def wait_until_present(self, locator, timeout=25):  # 👉 locator = element that should be in DOM
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def move_to_element(self, locator):  # 👉 locator = element to hover on (e.g., for dropdown menus)
        ActionChains(self.driver).move_to_element(self.search_element(locator)).perform()

    def upload_file(self, locator, file_path):  # 👉 locator = input type="file"; file_path = local file path
        self.search_element(locator).send_keys(file_path)

    def is_element_enabled(self, locator, timeout=30):  # 👉 locator = element that should be enabled & visible
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: self.search_element(locator).is_enabled()
            )
            element = self.search_element(locator)
            return element.is_displayed() and element.is_enabled()
        except TimeoutException:
            raise AssertionError(f"Element {locator} not enabled in {timeout} seconds.")

    def take_screenshot(self, name="screenshot"):  # 👉 name = custom screenshot name (optional)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{name}_{timestamp}.png"
        self.driver.save_screenshot(filename)
        allure.attach.file(filename, name=filename, attachment_type=allure.attachment_type.PNG)
        print(f"Screenshot saved as: {filename}")
