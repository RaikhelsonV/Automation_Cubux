from tests.test_data import data as td
from tests.test_data import validation_ru as val
import pytest
import allure


@allure.feature('Login Page')
class TestLogin:

    @allure.story('Validation errors')
    @allure.description('Verify that first name field is required')
    def test_login(self, driver, home_page, login):
        home_page.click_start_btn()
        login.click_login_via_browser_link()
        login.enter_email(td.email)
        login.enter_password(td.password)
        login.click_login_btn()
        assert home_page.get_name() == td.name

    @allure.story('Validation errors')
    @allure.description('Verify that first name field is required')
    @pytest.mark.parametrize("email,password,expected_email_err, expected_pass_err",
                             [('', '', val.email_blank_err, val.password_blank_err)])
    def test_login_blank(self, driver, home_page, login, email, password, expected_email_err, expected_pass_err):
        home_page.click_start_btn()
        login.click_login_via_browser_link()
        login.enter_email(email)
        login.enter_password(password)
        login.click_login_btn()
        assert login.get_email_error() == expected_email_err
        assert login.get_password_error() == expected_pass_err

    @allure.story('Validation errors')
    @allure.description('Verify that first name field is required')
    def test_login_invalid(self, driver, home_page, login):
        home_page.click_start_btn()
        login.click_login_via_browser_link()
        login.enter_email('aaaaaa')
        login.enter_password('3333')
        login.click_login_btn()
        assert login.is_displayed_email_error() == 0
        assert login.get_invalid_email_error() == val.email_invalid_err

    @allure.story('Validation errors')
    @allure.description('Verify that first name field is required')
    def test_login_exist(self, driver, home_page, login):
        home_page.click_start_btn()
        login.click_login_via_browser_link()
        login.enter_email('val@dan.test')
        login.enter_password('3333')
        login.click_login_btn()
        assert login.get_password_error() == val.not_existing_user
