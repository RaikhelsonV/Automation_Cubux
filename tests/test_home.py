import allure
from tests.test_data import data as td


@allure.feature('Home Page')
class TestHome:

    @allure.story('Add income')
    @allure.description('Make sure that the amount is displayed in the income section '
                        'and in the form of transfers after the method add income was executed')
    def test_incomes(self, driver, logged_in, incomes, add_income, home_page):
        home_page.logo()
        assert home_page.get_incomes() == int(td.sum)
        home_page.get_last_added_transaction_by_name(td.salary)
        assert home_page.get_category_name() == td.salary
        assert home_page.get_amount() == int(td.sum)
        delete_income(home_page, incomes)

    @allure.story('Add Expense')
    @allure.description('Make sure that the amount is displayed in the expense section'
                        ' and in the form of transfers after the method add expense was executed')
    def test_expenses(self, driver, logged_in, expenses, add_expense, home_page):
        home_page.logo()
        assert home_page.get_expenses() == int(td.sum)
        home_page.get_last_added_transaction_by_name(td.auto)
        assert home_page.get_category_name() == td.auto
        assert home_page.get_amount() == int(td.sum)
        delete_expense(home_page, expenses)

    @allure.story('Balance')
    @allure.description('Make sure that the amount of balance is displayed correctly')
    def test_balance(self, driver, logged_in, incomes, add_income, expenses, add_expense, home_page):
        home_page.logo()
        assert home_page.get_balance() == home_page.get_incomes() - home_page.get_expenses()


def delete_income(home_page, incomes):
    home_page.menu_incomes()
    incomes.delete()
    incomes.click_confirm_delete()


def delete_expense(home_page, expenses):
    home_page.menu_expenses()
    expenses.delete()
    expenses.click_confirm_delete()
