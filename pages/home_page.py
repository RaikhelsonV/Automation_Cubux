from pages.base_page import BasePage
from pages.locators import home as loc
from tests.test_data import data as td
import allure


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = td.cubux

    @allure.step('Click on "Start"')
    def click_start_btn(self):
        self.click(loc.start_btn)

    def logo(self):
        self.click(loc.logo)

    @allure.step('Click on "Incomes"')
    def menu_incomes(self):
        self.click(loc.incomes_menu)

    @allure.step('Click on "Expenses"')
    def menu_expenses(self):
        self.click(loc.expenses_menu)

    @allure.step('Click on "Loans"')
    def menu_loans(self):
        self.click(loc.loans_menu)

    @allure.step('Get name')
    def get_name(self):
        return self.get_text(loc.name)

    @allure.step('Get incomes')
    def get_incomes(self):
        return self.extract_currency_from_str(self.get_text(loc.incomes))

    @allure.step('Get expenses')
    def get_expenses(self):
        return self.extract_currency_from_str(self.get_text(loc.expenses))

    @allure.step('Get balance')
    def get_balance(self):
        return self.extract_currency_from_str(self.get_text(loc.balance))

    @allure.step('Get calendar')
    def get_calendar(self):
        return self.extract_currency_from_str(self.get_text(loc.calendar))
