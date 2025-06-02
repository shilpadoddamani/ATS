import pytest
import allure
from utils.browser import get_driver
from pages.signup_page import SignupPage
import time

@pytest.fixture
def setup():
    driver = get_driver()
    yield driver
    driver.quit()

@allure.feature("signup")
@allure.story("Sign up with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
def test_signup(setup):
    driver = setup
    with allure.step("Open sign up page"):
        driver.get("https://recruiter.gigin.ai/signup")

    signup_page = SignupPage(driver)

    with allure.step("Perform signup with email and company"):
        signup_page.do_signup("viragi2288@dlbazi.com", "Gorge")

    with allure.step("Verify sign up was successful or take screenshot if failed"):
        try:
            assert "gigin workos" in driver.title.lower(), "Page title does not contain 'gigin workos'"
            print("Signup test passed")
        except AssertionError as e:
            print("Signup test failed - taking screenshot")
            signup_page.take_screenshot("signup_failure")
            raise e  # Reraise the error with message
 


@allure.feature("signup2")
@allure.story("Sign up with invalid credentials")
@allure.severity(allure.severity_level.CRITICAL)
def test_signup(setup):
    driver = setup
    with allure.step("Open sign up page"):
        driver.get("https://sandbox.workos.gigin.ai/signup")

    signup_page =SignupPage(driver)

    with allure.step("Perform signup with email and company"):
        signup_page.do_signup(
            "bshilpa747mail.com", "Gorge"
        )

    with allure.step("Verify sign up was successful"):
        assert "gigin workos" in driver.title.lower()
#
