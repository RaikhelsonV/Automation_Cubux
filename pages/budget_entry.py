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

    def click_create_operation(self):
        self.click(loc.execute_operation_btn)

    def open_date_picker(self):
        self.click_from_list(loc.options, 2)

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

    def enter_amount(self, amount):
        self.set_text(loc.amount, amount)

    def select_repetition(self, rate):
        self.scroll_to_the_bottom()
        self.select_by_value(loc.repetition, rate)

    def click_ok(self):
        self.scroll_to_the_bottom()
        self.click(loc.ok_btn)
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(loc.ok_btn))

    def get_total_amount(self):
        self.scroll_to_the_top(loc.total_amount)
        return self.extract_digits_from_str(self.get_text(loc.total_amount))

    def get_amount_by_category(self, selected_cat):
        categories = self.find_all(loc.categories)
        amounts = self.find_all(loc.amounts)
        for category in range(len(categories)):
            WebDriverWait(self.driver, 20).until(EC.visibility_of(categories[category]))
            if categories[category].text == selected_cat:
                return self.extract_digits_from_str(amounts[category].text)

    def get_transaction_by_name(self, name):
        self.scroll_to_the_bottom()
        list_transactions = self.find_all(loc.transactions)
        for transaction in range(len(list_transactions)):
            WebDriverWait(self.driver, 20).until(EC.visibility_of(list_transactions[transaction]))
            if list_transactions[transaction].text.__contains__(name):
                self.result = str(transaction + 1)

    def get_category_name(self):
        category = (By.CSS_SELECTOR, '.TransactionsTable_root__ehmR3 tr:nth-child(' + self.result + ') .list')
        return self.get_text(category)

    def get_amount(self):
        amount = (By.CSS_SELECTOR, '.TransactionsTable_root__ehmR3 tr:nth-child(' + self.result + ') .list-value')
        return self.extract_digits_from_str(self.get_text(amount))

    def create_copy(self):
        self.click_from_list(loc.operations, 0)

    def edit(self):
        self.click_from_list(loc.operations, 1)

    def delete(self):
        self.click_from_list(loc.operations, 2)

    def click_confirm_delete(self):
        self.click_from_list(loc.confirm_dialog, 0)
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(loc.confirm_dialog))
