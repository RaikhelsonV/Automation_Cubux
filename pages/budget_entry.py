import allure

from pages.base_page import BasePage
from pages.locators import budget as loc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BudgetEntry(BasePage):
    result = ''

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        return self.get_text(loc.title)

    @allure.step('Clock on "add operation"')
    def click_create_operation(self):
        self.click(loc.execute_operation_btn)

    @allure.step('Open date picker')
    def open_date_picker(self):
        self.click_from_list(loc.options, 2)

    @allure.step('Click on the selected day')
    def set_day_from_date_picker(self, selected_day):
        days = self.find_all(loc.date_picker)
        for day in range(len(days)):
            if days[day].text == selected_day:
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(days[day]))
                days[day].click()
                break

    def select_day_of_monthly_income(self, selected_day):
        days = self.find_all(loc.days_of_month)
        for day in range(len(days)):
            if days[day].text == selected_day:
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(days[day]))
                days[day].click()
                break

    @allure.step('Enter amount')
    def enter_amount(self, amount):
        self.set_text(loc.amount, amount)

    def select_repetition(self, rate):
        self.scroll_to_the_bottom()
        self.select_by_value(loc.repetition, rate)

    def click_ok(self):
        self.scroll_to_the_bottom()
        self.click(loc.ok_btn)
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(loc.ok_btn))

    @allure.step('Get the total amount')
    def get_total_amount(self):
        return self.extract_digits_from_str(self.get_text(loc.total_amount))
    @allure.step('Get the total amount by category in categories form')
    def get_amount_by_category(self, selected_cat):
        categories = self.find_all(loc.categories)
        amounts = self.find_all(loc.amounts)
        for category in range(len(categories)):
            WebDriverWait(self.driver, 20).until(EC.visibility_of(categories[category]))
            if categories[category].text == selected_cat:
                return self.extract_digits_from_str(amounts[category].text)

    @allure.step('Get details of the last completed transaction')
    def get_last_added_transaction_by_name(self, name):
        self.scroll_to_the_bottom()
        list_transactions = self.find_all(loc.transactions)
        transactions_by_name = []
        for tr in range(len(list_transactions)):
            WebDriverWait(self.driver, 20).until(EC.visibility_of(list_transactions[tr]))
            transactions_by_name = self.get_transactions_by_name(list_transactions, name)
            break
        if len(transactions_by_name) == 1:
            self.result = str(2)
        else:
            self.result = str(len(transactions_by_name))

    @staticmethod
    def get_transactions_by_name(all_transactions_list, name):
        list_by_name = []
        try:
            for tr in range(len(all_transactions_list)):
                if all_transactions_list[tr].text.__contains__(name):
                    list_by_name.append(all_transactions_list[tr])
            return list_by_name
        except ValueError:
            print(f'Transaction {name} does not exist')

    @allure.step('Get category in transaction table')
    def get_category_name(self):
        category = (By.CSS_SELECTOR, '.TransactionsTable_root__ehmR3 tr:nth-child(' + self.result + ') .list')
        return self.get_text(category)
    @allure.step('Get amount in transaction table')
    def get_amount(self):
        amount = (By.CSS_SELECTOR, '.TransactionsTable_root__ehmR3 tr:nth-child(' + self.result + ') .list-value')
        return self.extract_digits_from_str(self.get_text(amount))

    @allure.step('Click on "create copy"')
    def create_copy(self):
        self.click_from_list(loc.operations, 0)

    @allure.step('Click on "edit"')
    def edit(self):
        self.click_from_list(loc.operations, 1)

    @allure.step('Click on "delete"')
    def delete(self):
        self.click_from_list(loc.operations, 2)

    def click_confirm_delete(self):
        self.click_from_list(loc.confirm_dialog, 0)
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(loc.confirm_dialog))
