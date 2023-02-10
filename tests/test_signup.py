import allure
from tests.test_data import data as td
from tests.test_data import validation_ru as val


@allure.feature('Sign Up Page')
class TestLogin:

    @allure.story('Validation errors')
    @allure.description('Verify that first name, last name, email, password and country fields are required')
    def test_sign_up_blank(self, driver, home_page, register):
        home_page.click_start_btn()
        register.click_register_link()
        register.fill_in_signup_form('', '', '', '')
        register.click_signup_btn()
        assert register.get_first_name_error() == val.first_name_err
        assert register.get_last_name_error() == val.last_name_err
        assert register.get_email_error() == val.email_blank_err
        assert register.get_password_error() == val.password_blank_err
        assert register.get_country_error() == val.country_err

    @allure.story('Validation errors')
    @allure.description('Verify that the first name  and last name field should not contains symbols')
    def test_sign_up_incorrect_names(self, driver, home_page, register):
        home_page.click_start_btn()
        register.click_register_link()
        register.fill_in_signup_form('/', '/', td.email, td.password)
        register.select_country(td.country)
        register.click_signup_btn()
        assert register.get_first_name_error() == val.name_invalid_err
        assert register.get_last_name_error() == val.name_invalid_err

    @allure.story('Validation errors')
    @allure.description('Verify error message is displayed if the first name and last name fields'
                        ' contain more than three words separate with space.')
    def test_sign_up_names_max_words(self, driver, home_page, register):
        home_page.click_start_btn()
        register.click_register_link()
        register.fill_in_signup_form('aaa aaa aaa aaa', 'aaa aaa aaa aaa', td.email, td.password)
        register.select_country(td.country)
        register.click_signup_btn()
        assert register.get_first_name_error() == val.name_max_words
        assert register.get_last_name_error() == val.name_max_words

    @allure.story('Validation errors')
    @allure.description('Ensure the error message is displayed when entering an email address without an @ sign.')
    def test_sign_up_invalid_email(self, driver, home_page, register):
        home_page.click_start_btn()
        register.click_register_link()
        register.fill_in_signup_form(td.first_name, td.last_name, 'aaaaaa', td.password)
        register.select_country(td.country)
        register.click_signup_btn()
        assert register.get_invalid_email_error() == val.email_invalid_err

    @allure.story('Validation errors')
    @allure.description('Make sure that when entering a passport with less than 8 characters, '
                        'an error message appears')
    def test_sign_up_password_min_length(self, driver, home_page, register):
        home_page.click_start_btn()
        register.click_register_link()
        register.fill_in_signup_form(td.first_name, td.last_name, td.email, '1111111')
        register.select_country(td.country)
        register.click_signup_btn()
        assert register.get_password_error() == val.password_min_length
