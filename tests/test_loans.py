from pages.home_page import HomePage
from pages.incomes_page import IncomesPage
from tests.test_data import data as td
import allure


@allure.feature('Loans Page')
class TestLoans:

    @allure.story('Go into debt')
    @allure.description('Make sure that the method of going into debt works correctly.')
    def test_go_into_debt(self, driver, logged_in, loans, add_debt, loan_history):
        assert loan_history.get_partner_name() == td.partner_name
        assert loan_history.get_total_account_debt() == int(td.sum)
        assert loan_history.get_total_amount_loan_status_form() == int(td.sum)
        delete_partner_with_transactions(loan_history)

    @allure.story('Go into debt')
    @allure.description('Ensure that the debt information is displayed correctly on the debt history page.')
    def test_compare_data_loan_history_page(self, driver, logged_in, loans, add_debt, loan_history):
        assert loan_history.get_partner_name() == td.partner_name
        assert loan_history.get_total_account_debt() == int(td.sum)
        assert loan_history.get_total_amount_loan_status_form() == int(td.sum)
        loan_history.get_last_added_transaction_by_name(td.account)
        assert loan_history.get_category() == td.account
        assert loan_history.get_date() == td.date
        assert loan_history.get_transfer_amount() == int(td.sum)
        assert loan_history.get_balance() == int(td.sum)
        delete_partner_with_transactions(loan_history)

    @allure.story('Go into debt')
    @allure.description('Ensure that the debt information is displayed correctly on the loaded PDF file.')
    def test_check_data_in_excel(self, driver, logged_in, loans, add_debt, loan_history):
        debt_amount = td.sum + ',00 ₪'
        loan_history.download_excel_file_and_check_debt_information(debt_amount, td.partner_name)
        delete_partner_with_transactions(loan_history)

    @allure.story('Edit debt')
    @allure.description('Make sure the method to edit debt parameters works correctly.')
    def test_edit_debt_parameters(self, driver, logged_in, loans, add_debt, loan_history):
        loan_history.get_last_added_transaction_by_name(td.account)
        loan_history.edit()
        loan_history.enter_amount('200')
        loan_history.click_save()
        loan_history.refresh()
        assert loan_history.get_total_account_debt() == 200
        assert loan_history.get_total_amount_loan_status_form() == 200
        loan_history.get_last_added_transaction_by_name(td.account)
        assert loan_history.get_transfer_amount() == 200
        assert loan_history.get_balance() == 200
        delete_partner_with_transactions(loan_history)

    @allure.story('Edit partner')
    @allure.description('Make sure that you can change the name of the partner.')
    def test_edit_partner(self, driver, logged_in, loans, add_debt, loan_history):
        loan_history.edit_partner_name("Alex")
        assert loan_history.get_partner_name() == "Alex"
        delete_partner_with_transactions(loan_history)

    @allure.story('Increase debt')
    @allure.description('Make sure the debt increase is working correctly.')
    def test_increase_debt(self, driver, logged_in, loans, add_debt, loan_history):
        loan_history.increase_debt('15')
        assert loan_history.get_total_account_debt() == 115
        assert loan_history.get_total_amount_loan_status_form() == 115
        loan_history.refresh()
        loan_history.get_last_added_transaction_by_name(td.account)
        assert loan_history.get_transfer_amount() == 15
        assert loan_history.get_balance() == 115
        delete_partner_with_transactions(loan_history)

    @allure.story('Reduce debt')
    @allure.description('Make sure the debt reduction is working correctly.')
    def test_reduce_debt(self, driver, logged_in, loans, add_debt, loan_history):
        loan_history.reduce_debt('15')
        assert loan_history.get_total_account_debt() == 85
        assert loan_history.get_total_amount_loan_status_form() == 85
        loan_history.refresh()
        loan_history.get_last_added_transaction_by_name(td.account)
        assert loan_history.get_transfer_amount() == 15
        assert loan_history.get_balance() == 85
        delete_partner_with_transactions(loan_history)

    @allure.story('Pay debt')
    @allure.description('Make sure debt payment is working correctly.')
    def test_pay_debt_off(self, driver, logged_in, loans, add_debt, loan_history):
        loan_history.pay_off(td.sum)
        assert loan_history.get_status_of_repaid_debt() == td.status
        assert loan_history.get_status_of_repaid_debt_sub() == td.status
        assert loan_history.get_total_amount_loan_status_form() == 0
        loan_history.refresh()
        loan_history.get_last_added_transaction_by_name(td.account)
        assert loan_history.get_transfer_amount() == int(td.sum)
        assert loan_history.get_balance() == 0

        home_page = HomePage(driver)
        home_page.menu_loans()
        assert loans.is_finish_debt()
        assert loans.get_name_finish_debt() == td.partner_name

        loans.open_loan_page()
        delete_partner_with_transactions(loan_history)

    @allure.story('Delete partner with transactions')
    @allure.description('Make sure that the deletion of the partner with transactions was successful')
    def test_delete_partner_with_transaction(self, driver, logged_in, loans, add_debt, loan_history, home_page):
        loan_history.delete_partner_and_transactions()
        assert loan_history.get_title() == td.loans
        assert loans.get_total_debt(0) == 0

        home_page.logo()
        assert home_page.get_incomes() == 0

    @allure.story('Delete partner')
    @allure.description('Make sure that the deletion of the partner but keep transactions were successful, '
                        'and the amount turned into income and displayed on the home page and incomes page')
    def test_delete_partner_save_transaction(self, driver, logged_in, loans, add_debt, loan_history, home_page):
        loan_history.delete_partner_and_transactions()
        assert loan_history.get_title() == td.loans
        assert loans.get_total_debt(0) == 0

        home_page.logo()
        assert home_page.get_incomes() == int(td.sum)

        incomes = IncomesPage(driver)
        home_page.menu_incomes()
        incomes.get_last_added_transaction_by_name(td.loans)
        assert incomes.get_category_name() == td.loans
        assert incomes.get_amount() == int(td.sum)
        incomes.delete()
        incomes.click_confirm_delete()

    @allure.story('Delete loan')
    @allure.description(
        'Make sure that the deletion of the loan only was successful, '
        'and the amount turned into income and displayed on the home page and incomes page')
    def test_delete_only_loan(self, driver, logged_in, loans, add_debt, loan_history, home_page):
        loan_history.delete()
        loan_history.delete_only_loan()
        assert loan_history.get_status_of_repaid_debt() == td.status
        assert loan_history.get_status_of_repaid_debt_sub() == td.status
        assert loan_history.get_total_amount_loan_status_form() == 0

        home_page.logo()
        assert home_page.get_incomes() == int(td.sum)

        incomes = IncomesPage(driver)
        home_page.menu_incomes()
        incomes.get_last_added_transaction_by_name(td.loans)
        assert incomes.get_category_name() == td.loans
        assert incomes.get_amount() == int(td.sum)
        incomes.delete()
        incomes.click_confirm_delete()

        home_page.menu_loans()
        assert loans.is_finish_debt()
        assert loans.get_name_finish_debt() == td.partner_name

        loans.open_loan_page()
        delete_partner_with_transactions(loan_history)

    @allure.story('Delete loan with transactions')
    @allure.description(
        'Make sure that the deletion of the loan with transactions was successful')
    def test_delete_transaction(self, driver, logged_in, loans, add_debt, loan_history, home_page):
        loan_history.delete()
        loan_history.delete_transaction()
        assert loan_history.get_status_of_repaid_debt() == td.status
        assert loan_history.get_status_of_repaid_debt_sub() == td.status
        assert loan_history.get_total_amount_loan_status_form() == 0

        home_page.logo()
        assert home_page.get_incomes() == 0

        home_page.menu_loans()
        assert loans.is_finish_debt()
        assert loans.get_name_finish_debt() == td.partner_name

        loans.open_loan_page()
        delete_partner_with_transactions(loan_history)


def delete_partner_with_transactions(loan_history):
    loan_history.delete_partner_and_transactions()
