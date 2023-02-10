import pytest
import allure
from tests.test_data import data as td
from tests.test_data import validation_ru as val
from pages.locators import login as loc


@allure.feature('Login Page')
class TestLogin:

    @allure.story('Log In')
    @allure.description('Make sure the login works.')
    def test_login(self, driver, home_page, login):
        home_page.click_start_btn()
        login.click_login_via_browser_link()
        login.enter_email(td.email)
        login.enter_password(td.password)
        login.click_login_btn()
        assert home_page.get_name() == td.name

    @allure.story('Validation errors')
    @allure.description('Verify that email and password fields are required')
    @pytest.mark.parametrize("email,password,expected_email_err, expected_pass_err",
                             [('', '', val.email_blank_err, val.password_blank_err)])
    def test_login_blank(self, driver, home_page, login, email, password, expected_email_err, expected_pass_err):
        home_page.click_start_btn()
        login.click_login_via_browser_link()
        login.enter_email(email)
        login.tab(loc.email)
        login.enter_password(password)
        login.tab(loc.password_login)
        assert login.get_email_error() == expected_email_err
        assert login.get_password_error() == expected_pass_err

    @allure.story('Validation errors')
    @allure.description('Ensure the error message is displayed when entering an email address without an @ sign.')
    def test_invalid_email(self, driver, home_page, login):
        home_page.click_start_btn()
        login.click_login_via_browser_link()
        login.enter_email('aaaaaa')
        login.tab(loc.email)
        assert login.is_displayed_email_error() == 0
        assert login.get_invalid_email_error() == val.email_invalid_err

    @allure.story('Validation errors')
    @allure.description('Verify that an error message is displayed if an incorrect password is entered.')
    def test_incorrect_password(self, driver, home_page, login):
        home_page.click_start_btn()
        login.click_login_via_browser_link()
        login.enter_email(td.email)
        login.enter_password('3333')
        login.tab(loc.login)
        login.click(loc.login)
        assert login.get_password_error() == val.not_existing_user
