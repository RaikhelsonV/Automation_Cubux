from pages.locators import budget as loc
from pages.locators import loans as loc_l
from pages.locators import loan as loc_ll
from tests.test_data import data as td
from pages.budget_entry import BudgetEntry
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import glob
import os


class LoanHistoryPage(BudgetEntry):
    def __init__(self, driver):
        super().__init__(driver)

    def get_partner_name(self):
        return self.get_text(loc_ll.partner_name)

    def get_total_amount_loan_status_form(self):
        return self.extract_digits_from_str(self.get_text(loc_ll.amount_status_form))

    def get_total_account_debt(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.transactions_form))
        return self.extract_digits_from_str(self.get_text(loc_ll.total_account_debt))

    def edit_partner_name(self, new_name):
        self.click(loc_ll.edit_partner)
        self.set_text(loc_l.name_field, new_name)
        self.click(loc_l.add_btn)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(loc_l.add_btn))

    def delete_partner_and_transactions(self):
        self.click(loc_ll.remove_partner)
        self.delete_partner_with_transactions()
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(loc_l.add_btn))
        assert self.get_one_hundred_percent() == '100%'
        self.click(loc_ll.close_btn)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(loc_ll.close_btn))

    def delete_partner_and_keep_transactions(self):
        self.click(loc_ll.remove_partner)
        self.delete_partner_but_save_transactions()
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(loc_l.add_btn))
        assert self.get_one_hundred_percent() == '100%'
        self.click(loc_ll.close_btn)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(loc_ll.close_btn))

    def select_account(self, index):
        self.click_from_list(loc.options, index)

    def cash(self):
        self.click_from_list(loc.under_options, 1)

    def credit_card(self):
        self.click_from_list(loc.under_options, 2)

    def increase_debt(self, sum):
        self.click_from_list(loc_ll.actions_debt, 0)
        self.select_account(1)
        self.cash()
        self.open_date_picker()
        self.set_day_from_date_picker(td.day)
        self.enter_amount(sum)
        self.click_ok()

    def reduce_debt(self, sum):
        self.click_from_list(loc_ll.actions_debt, 1)
        self.select_account(0)
        self.cash()
        self.open_date_picker()
        self.set_day_from_date_picker(td.day)
        self.enter_amount(sum)
        self.click_ok()

    def pay_off(self, total_sum):
        self.click_from_list(loc_ll.actions_debt, 1)
        self.select_account(0)
        self.cash()
        self.open_date_picker()
        self.set_day_from_date_picker(td.day)
        self.enter_amount_of_debt(total_sum)
        assert self.get_total_amount_of_debt_due() == total_sum
        self.click_ok()

    def get_status_of_repaid_debt(self):
        return self.get_text(loc_ll.status)

    def get_status_of_repaid_debt_sub(self):
        return self.get_text(loc_ll.status_sub)

    def enter_amount_of_debt(self, amount):
        self.find_all(loc.amount)[0].send_keys(amount)

    def get_total_amount_of_debt_due(self):
        return self.find_all(loc.amount)[0].get_property("value")

    def selected_transaction(self, name):
        self.get_last_added_transaction_by_name(name)

    def get_date(self):
        date = (By.CSS_SELECTOR, '.TransactionsTable_root__ehmR3 tr:nth-child(' + self.result + ') time')
        return self.get_text(date)

    def get_category(self):
        category = (By.CSS_SELECTOR, '.TransactionsTable_root__ehmR3 tr:nth-child(' + self.result + ')>:nth-child(2)')
        return self.get_text(category)

    def get_transfer_amount(self):
        sums = (By.CSS_SELECTOR, '.TransactionsTable_root__ehmR3 tr:nth-child(' + self.result + ') .list-value')
        print(self.find_all(sums)[0].text)
        return self.extract_digits_from_str(self.find_all(sums)[0].text)

    def get_balance(self):
        sums = (By.CSS_SELECTOR, '.TransactionsTable_root__ehmR3 tr:nth-child(' + self.result + ') .list-value')
        return self.extract_digits_from_str(self.find_all(sums)[1].text)

    def click_save(self):
        self.click(loc_ll.save_btn)

    def delete_only_loan(self):
        self.click_from_list(loc_ll.delete_btns, 0)
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(loc_ll.delete_btns))

    def delete_transaction(self):
        self.click_from_list(loc_ll.delete_btns, 1)
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(loc_ll.delete_btns))

    def delete_partner_with_transactions(self):
        self.click_from_list(loc_ll.save_btn, 0)
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(loc_ll.save_btn))

    def get_one_hundred_percent(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc_ll.one_hundred_percent))
        return self.get_text(loc_ll.one_hundred_percent)

    def delete_partner_but_save_transactions(self):
        self.click_from_list(loc_ll.save_btn, 1)
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(loc_ll.save_btn))

    def download_excel_file_and_check_debt_information(self, debt_sum, partner):
        self.click_from_list(loc.operations, 0)
        list_of_files = glob.glob('C:/Users/Valerie/Downloads/*.xlsx')
        latest_file = max(list_of_files, key=os.path.getctime)
        e = pd.read_excel(latest_file, sheet_name='Worksheet')
        assert e.values.__contains__(debt_sum)
        assert e.values.__contains__(partner)
