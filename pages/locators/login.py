from selenium.webdriver.common.by import By

login_via_browser = (By.CSS_SELECTOR, '.btn-lg .content')
register = (By.CSS_SELECTOR, '.text-success')
email = (By.CSS_SELECTOR, "[placeholder='E-mail']")
email_error = (By.CSS_SELECTOR, '.validate-input.field-loginform-username .validation-error')
password_login = (By.CSS_SELECTOR, "[name='LoginForm[password]']")
password_error = (By.CSS_SELECTOR, '.validate-input.field-loginform-password .validation-error')
password_register = (By.CSS_SELECTOR, "[name='RegisterForm[pass]']")
login = (By.CSS_SELECTOR, '.login100-form-btn')
first_name = (By.CSS_SELECTOR, "[name='RegisterForm[name]']")
last_name = (By.CSS_SELECTOR, "[name='RegisterForm[family]']")
select_country = (By.CSS_SELECTOR, "#select2-signup-country-select-container")
search_field = (By.CSS_SELECTOR, '.select2-search__field')
recaptcha = (By.CSS_SELECTOR, '#recaptcha-anchor')
sign_up = (By.CSS_SELECTOR, '.button-loading-content')

