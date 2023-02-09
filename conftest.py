import time
from pages.expenses_page import ExpensesPage
from pages.loan_history_page import LoanHistoryPage
from tests.test_data import data as td
from pages.home_page import HomePage
from pages.login_form import LoginPage
from pages.register_form import RegisterForm
from pages.incomes_page import IncomesPage
from pages.loans_page import LoansPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_experimental_option('detach', True)
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def home_page(driver):
    home_page = HomePage(driver)
    home_page.open()
    return home_page


@pytest.fixture(scope='function')
def login(driver):
    login = LoginPage(driver)
    return login


@pytest.fixture(scope='function')
def register(driver):
    register = RegisterForm(driver)
    return register


@pytest.fixture(scope='function')
def incomes(driver, home_page):
    incomes = IncomesPage(driver)
    home_page.menu_incomes()
    return incomes


@pytest.fixture(scope='function')
def expenses(driver, home_page):
    expenses = ExpensesPage(driver)
    home_page.menu_expenses()
    return expenses


@pytest.fixture(scope='function')
def loans(driver, home_page):
    loans = LoansPage(driver)
    home_page.menu_loans()
    return loans


@pytest.fixture(scope='function')
def loan_history(driver, loans):
    loan = LoanHistoryPage(driver)
    loans.open_loan_page()
    return loan


@pytest.fixture(scope='function')
def logged_in(driver, home_page, login):
    home_page.click_start_btn()
    login.click_login_via_browser_link()
    login.enter_email(td.email)
    login.enter_password(td.password)
    login.click_login_btn()


@pytest.fixture(scope='function')
def add_income(driver, incomes):
    incomes.click_create_operation()
    incomes.select_account()
    incomes.cash()
    incomes.select_category()
    incomes.salary()
    incomes.open_date_picker()
    incomes.set_day_from_date_picker(td.day)
    incomes.enter_amount(td.sum)
    incomes.click_ok()
    assert incomes.get_total_amount() == int(td.sum)
    assert incomes.get_amount_by_category(td.salary) == int(td.sum)


@pytest.fixture(scope='function')
def add_expense(driver, expenses):
    expenses.click_create_operation()
    expenses.select_account()
    expenses.cash()
    expenses.select_category()
    expenses.auto()
    expenses.open_date_picker()
    expenses.set_day_from_date_picker(td.day)
    expenses.enter_amount(td.sum)
    expenses.click_ok()
    assert expenses.get_total_amount() == int(td.sum)
    assert expenses.get_amount_by_category(td.auto) == int(td.sum)


@pytest.fixture(scope='function')
def add_debt(driver, loans):
    loans.select_operation(0, 0)
    loans.select_partner()
    loans.create_partner()
    loans.select_account()
    loans.cash()
    loans.open_date_picker()
    loans.set_day_from_date_picker(td.day)
    loans.enter_amount(td.sum)
    loans.click_ok()



