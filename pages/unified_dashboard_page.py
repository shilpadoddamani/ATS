from selenium.webdriver.common.by import By
from utils.base_page import BasePage
from utils.waits import wait_for_element

class UnifiedDashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # 👉 Replace these with the actual locators from your dashboard page
        self.ATS_Card = (By.XPATH, '//p[contains(text(),"AI-Powered Hiring Workspace")]')
        self.BGV_Card= (By.XPATH, '//p[contains(text(),"Background Verification")]')
        self.GHP_Card = (By.XPATH, '//p[contains(text(),"Guarantee Hiring Program")]')
        self.header_title = (By.XPATH, '//title[contains(text(),"Gigin WorkOS")]')

    def verify_dashboard_loaded(self):
        #Wait for a unique element on the dashboard to appear
        return wait_for_element(self.driver, self.header_title).is_displayed()

    def ats_card (self):
        self.click_element(self.ATS_Card)

    def ghp_card(self):
        self.click_element(self.GHP_Card)

    def bgv_card(self):
        self.click_element(self.BGV_Card)
