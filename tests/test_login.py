
import pytest
import allure
from utils.browser import get_driver
from pages.login_page import LoginPage

@pytest.fixture
def setup():
    driver = get_driver()
    yield driver
    driver.quit()

@allure.feature("Login")
@allure.story("Login with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_with_username_and_password(setup):
    driver = setup
    with allure.step("Open login page"):
        driver.get("https://recruiter.gigin.ai/login")

    login_page = LoginPage(driver)

    with allure.step("Perform login with valid credentials"):
        login_page.do_login("viragi2288@dlbazi.com", "Shilpa@1234567890")

    with allure.step("Verify login was successful"):
        # Example assertion (customize as per your app behavior)
        assert "dashboard" in driver.current_url.lower()


@allure.feature("Login")
@allure.story("Login with invalid password")
@allure.severity(allure.severity_level.NORMAL)
def test_login_with_invalid_password(setup):
    driver = setup
    with allure.step("Open login page"):
        driver.get("https://recruiter.gigin.ai/login")

    login_page = LoginPage(driver)

    with allure.step("Perform login with invalid password"):
        login_page.do_login("bshilpa747@gmail.com", "WrongPassword123")

    with allure.step("Get and verify error message"):
        error_message = login_page.get_error_message()
        assert "Email or Password is incorrect" in error_message

