from time import sleep
from pages.base_page import BasePage
from pages.locators import login as loc
import allure


class RegisterForm(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Click on "Register now"')
    def click_register_link(self):
        self.click(loc.register)
        self.switch_tab(1)
        print(self.driver.title)

    @allure.step('Fill in sign up form')
    def fill_in_signup_form(self, first_name, last_name, email, password):
        self.set_text(loc.first_name, first_name)
        self.set_text(loc.last_name, last_name)
        self.set_text(loc.email, email)
        self.set_text(loc.password_register, password)

    @allure.step('Select country')
    def select_country(self, country):
        self.scroll_to_the_bottom()
        self.click(loc.select_country)
        self.set_text(loc.search_field, country)
        self.press_down_arrow(loc.search_field)

    @allure.step('Recaptcha')
    def recaptcha(self):
        self.click(loc.recaptcha)

    @allure.step('SignUp')
    def click_signup_btn(self):
        self.click(loc.sign_up)
        sleep(4000)
