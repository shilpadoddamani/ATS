
# to run specific file
# pytest tests/test_login.py --alluredir=allure-results

# to run all file
# pytest --alluredir=allure-results

# to get visual reports
# allure serve allure-results


 # Add Allure to your test code
# 👉 Add step-wise reporting
# mention this line below function creation line
# with allure.step("message)

# Mark tests with metadata
# @allure.title("Test Signup Flow")
# @allure.description("This test verifies the signup process and activation via email")
# @allure.severity(allure.severity_level.CRITICAL)
# @allure.story("User Signup and Account Activation")
# def test_signup():



