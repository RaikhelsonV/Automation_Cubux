from pages.base_page import BasePage
from pages.locators import login as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Click on "Login via the browser"')
    def click_login_via_browser_link(self):
        self.click(loc.login_via_browser)
        self.switch_tab(1)

    @allure.step('Enter email')
    def enter_email(self, email):
        self.set_text(loc.email, email)

    @allure.step('Enter password')
    def enter_password(self, password):
        self.set_text(loc.password_login, password)

    @allure.step('Click on "Login"')
    def click_login_btn(self):
        self.click(loc.login)
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(loc.login))

    @allure.step('Get email error')
    def get_email_error(self):
        return self.get_text(loc.email_error)

    @allure.step('Get password error')
    def get_password_error(self):
        return self.get_text(loc.password_error)

    @allure.step('Get email error')
    def get_invalid_email_error(self):
        return self.get_alert_message(loc.email)

    @allure.step('Get email error')
    def is_displayed_email_error(self):
        return self.get_alert_state(loc.email)


