import allure
from tests.test_data import data as td


@allure.feature('Expenses Page')
class TestExpenses:

    @allure.story('Add expense')
    @allure.description('Make sure that the method add expense works correctly.')
    def test_add_expense(self, driver, logged_in, expenses, add_expense, home_page):
        assert expenses.get_total_amount() == int(td.sum)
        assert expenses.get_amount_by_category(td.auto) == int(td.sum)
        delete_operation(home_page, expenses)

    @allure.story('Add expense')
    @allure.description('Ensure that the expense information is displayed correctly')
    def test_check_expenses(self, driver, logged_in, expenses, add_expense, home_page):
        assert expenses.get_total_amount() == int(td.sum)
        assert expenses.get_amount_by_category(td.auto) == int(td.sum)
        home_page.menu_expenses()
        expenses.get_last_added_transaction_by_name(td.auto)
        assert expenses.get_category_name() == td.auto
        assert expenses.get_amount() == int(td.sum)
        delete_operation(home_page, expenses)

    @allure.story('Edit expense')
    @allure.description('Make sure the method to edit expense works correctly.')
    def test_edit_expense(self, driver, logged_in, add_expense, home_page, expenses):
        home_page.menu_expenses()
        expenses.get_last_added_transaction_by_name(td.auto)
        assert expenses.get_category_name() == td.auto
        assert expenses.get_amount() == int(td.sum)

        expenses.edit()
        expenses.enter_amount('200')
        expenses.click_ok()
        assert expenses.get_amount() == 200
        assert expenses.get_total_amount() == 200
        assert expenses.get_amount_by_category(td.auto) == 200
        delete_operation(home_page, expenses)

    @allure.story('Copy expense')
    @allure.description('Make sure the method to copy expense works correctly.')
    def test_copy(self, driver, logged_in, add_expense, home_page, expenses):
        home_page.menu_expenses()
        expenses.get_last_added_transaction_by_name(td.auto)
        assert expenses.get_category_name() == td.auto
        assert expenses.get_amount() == int(td.sum)

        expenses.create_copy()
        expenses.click_ok()
        assert expenses.get_total_amount() == 200
        assert expenses.get_amount_by_category(td.auto) == 200
        delete_operation(home_page, expenses)

    @allure.story('Delete expense')
    @allure.description('Make sure the method to delete expense works correctly.')
    def test_delete_expense(self, driver, logged_in, add_expense, home_page, expenses):
        delete_operation(home_page, expenses)
        assert expenses.get_total_amount() == 0
        assert expenses.get_amount() == 0
        assert expenses.get_amount_by_category(td.auto) == 0


def delete_operation(home_page, expenses):
    home_page.menu_expenses()
    expenses.delete()
    expenses.click_confirm_delete()
