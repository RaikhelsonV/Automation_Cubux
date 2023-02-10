import allure

from pages.budget_entry import BudgetEntry
from pages.locators import budget as loc


class IncomesPage(BudgetEntry):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Click on "category"')
    def select_category(self):
        self.click_from_list(loc.options, 1)

    @allure.step('Click on "account"')
    def select_account(self):
        self.click_from_list(loc.options, 0)

    @allure.step('Select "cash"')
    def cash(self):
        self.click_from_list(loc.under_options, 1)

    @allure.step('Select "CC"')
    def credit_card(self):
        self.click_from_list(loc.under_options, 2)

    @allure.step('Add account')
    def add_account(self):
        self.click_from_list(loc.under_options, 0)

    @allure.step('Add category')
    def add_category(self):
        self.click_from_list(loc.under_options, 0)

    @allure.step('Select "salary"')
    def salary(self):
        self.click_from_list(loc.under_options, 0)
