from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element(driver, locator, timeout=10):
    """
    Wait until the element located by `locator` is visible on the page.

    :param driver: WebDriver instance
    :param locator: tuple like (By.ID, 'element_id')
    :param timeout: max wait time in seconds (default 10)
    :return: WebElement if found within timeout
    """
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )
