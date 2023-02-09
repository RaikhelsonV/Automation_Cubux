import time
from pages.locators import budget as loc
from pages.locators import loans as loc_l
from tests.test_data import data as td
from pages.budget_entry import BudgetEntry
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoansPage(BudgetEntry):
    def __init__(self, driver):
        super().__init__(driver)

    def select_operation(self, type_operation, option):
        self.find_nested_el(loc.operations_list, type_operation, loc.execute_operation_btn, option).click()
        self.scroll_to_the_top(loc.title)
        if type_operation == 0:
            assert self.debt_options() == td.borrow
        else:
            assert self.debt_options() == td.reimburse

    def debt_options(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc_l.loans_list))
        return self.get_text(loc_l.loans_list)

    def select_partner(self):
        self.click_from_list(loc.options, 0)

    def select_account(self):
        self.click_from_list(loc.options, 1)

    def create_partner(self):
        self.click(loc_l.create_partner_btn)
        self.set_text(loc_l.name_field, td.partner_name)
        self.click(loc_l.add_btn)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(loc_l.add_btn))

    def cash(self):
        self.click_from_list(loc.under_options, 1)

    def credit_card(self):
        self.click_from_list(loc.under_options, 2)

    def get_total_debt(self, index):
        self.scroll_to_the_top(loc.total_amount)
        return self.extract_digits_from_str(self.find_all(loc.total_amount)[index].text)

    def get_account_amount(self):
        return self.extract_digits_from_str(self.get_text(loc_l.account_amount))

    def get_partner_name(self):
        return self.get_text(loc_l.partner_name)

    def open_loan_page(self):
        self.click(loc_l.loan_page)
        time.sleep(10)

    def is_finish_debt(self):
        return self.is_displayed(loc_l.loan_page)

    def get_name_finish_debt(self):
        return self.get_text(loc_l.partner_name)



