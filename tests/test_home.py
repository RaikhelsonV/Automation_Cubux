import allure


@allure.feature('Home Page')
class TestHome:

    @allure.story('Incomes')
    @allure.description('Verify that first name field is required')
    def test_incomes(self, driver, logged_in, incomes, add_income, home_page):
        home_page.logo()
        assert home_page.get_last_added_transaction_by_name() == 100

    @allure.story('Expenses')
    @allure.description('Verify that first name field is required')
    def test_expenses(self, driver, logged_in, incomes, add_expense, home_page):
        home_page.logo()
        assert home_page.get_expenses() == 100

    @allure.story('Balance')
    @allure.description('Verify that first name field is required')
    def test_balance(self, driver, logged_in, home_page):
        assert home_page.get_balance() == home_page.get_last_added_transaction_by_name() - home_page.get_expenses()
