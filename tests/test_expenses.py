from tests.test_data import data as td
import allure


@allure.feature('Expenses Page')
class TestExpenses:

    @allure.story('Validation errors')
    @allure.description('Verify that first name field is required')
    def test_create_op(self, driver, logged_in, expenses, add_expense, home_page):
        delete_operation(home_page, expenses)

    @allure.story('Validation errors')
    @allure.description('Verify that first name field is required')
    def test_check_expenses(self, driver, logged_in, expenses, add_expense, home_page):
        home_page.menu_expenses()
        expenses.get_transaction_by_name(td.auto)
        assert expenses.get_category_name() == td.auto
        assert expenses.get_amount() == int(td.sum)
        delete_operation(home_page, expenses)

    @allure.story('Validation errors')
    @allure.description('Verify that first name field is required')
    def test_edit(self, driver, logged_in, add_expense, home_page, expenses):
        home_page.menu_expenses()
        expenses.get_transaction_by_name(td.auto)
        assert expenses.get_category_name() == td.auto
        assert expenses.get_amount() == int(td.sum)

        expenses.edit()
        expenses.enter_amount('200')
        expenses.click_ok()
        assert expenses.get_amount() == 200
        assert expenses.get_total_amount() == 200
        assert expenses.get_amount_by_category(td.auto) == 200
        delete_operation(home_page, expenses)

    @allure.story('Validation errors')
    @allure.description('Verify that first name field is required')
    def test_copy(self, driver, logged_in, add_expense, home_page, expenses):

        home_page.menu_expenses()
        expenses.get_transaction_by_name(td.auto)
        assert expenses.get_category_name() == td.auto
        assert expenses.get_amount() == int(td.sum)

        expenses.create_copy()
        expenses.click_ok()
        assert expenses.get_total_amount() == 200
        assert expenses.get_amount_by_category(td.auto) == 200
        delete_operation(home_page, expenses)

    @allure.description('Verify that first name field is required')
    def test_delete_op(self, driver, logged_in, add_expense, home_page, expenses):
        delete_operation(home_page, expenses)
        assert expenses.get_amount() == 0
        assert expenses.get_amount_by_category(td.auto) == 0


def delete_operation(home_page, incomes):
    home_page.menu_expenses()
    incomes.delete()
    incomes.click_confirm_delete()
    assert incomes.get_total_amount() == 0
