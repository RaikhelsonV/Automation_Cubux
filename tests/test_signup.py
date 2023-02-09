from tests.test_data import data as td
import allure


@allure.feature('SignUp form')
@allure.story('Validation errors')
@allure.description('Verify that first name field is required')
def test_sign_up(driver, home_page, register):
    home_page.click_start_btn()
    register.click_register_link()
    register.fill_in_signup_form(td.first_name, td.last_name, td.email, td.password)
    register.select_country(td.country)
    register.recaptcha()
    register.click_signup_btn()


