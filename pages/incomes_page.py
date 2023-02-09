from pages.budget_entry import BudgetEntry
from pages.locators import budget as loc


class IncomesPage(BudgetEntry):

    def __init__(self, driver):
        super().__init__(driver)

    def select_category(self):
        self.click_from_list(loc.options, 1)

    def select_account(self):
        self.click_from_list(loc.options, 0)

    def cash(self):
        self.click_from_list(loc.under_options, 1)

    def credit_card(self):
        self.click_from_list(loc.under_options, 2)

    def add_account(self):
        self.click_from_list(loc.under_options, 0)

    def add_category(self):
        self.click_from_list(loc.under_options, 0)

    def salary(self):
        self.click_from_list(loc.under_options, 0)
