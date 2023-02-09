from tests.test_data import data as td
import allure


@allure.feature('Incomes Page')
class TestIncomes:

    @allure.story('Validation errors')
    @allure.description('Verify that first name field is required')
    def test_create_op(self, driver, logged_in, incomes, add_income, home_page):
        delete_operation(home_page, incomes)

    @allure.story('Validation errors')
    @allure.description('Verify that first name field is required')
    def test_check_incomes(self, driver, logged_in, incomes, add_income, home_page):

        home_page.menu_incomes()
        incomes.get_last_added_transaction_by_name(td.salary)
        assert incomes.get_category_name() == td.salary
        assert incomes.get_amount() == int(td.sum)
        delete_operation(home_page, incomes)

    @allure.story('Validation errors')
    @allure.description('Verify that first name field is required')
    def test_edit(self, driver, logged_in, incomes, add_income, home_page):

        home_page.menu_incomes()
        incomes.get_last_added_transaction_by_name(td.salary)
        assert incomes.get_category_name() == td.salary
        assert incomes.get_amount() == int(td.sum)

        incomes.edit()
        incomes.enter_amount('200')
        incomes.click_ok()
        assert incomes.get_amount() == 200
        assert incomes.get_total_amount() == 200
        assert incomes.get_amount_by_category(td.salary) == 200
        delete_operation(home_page, incomes)

    @allure.story('Validation errors')
    @allure.description('Verify that first name field is required')
    def test_copy(self, driver, logged_in, incomes, add_income, home_page):
        home_page.menu_incomes()
        incomes.get_last_added_transaction_by_name(td.salary)
        assert incomes.get_category_name() == td.salary
        assert incomes.get_amount() == int(td.sum)

        incomes.create_copy()
        incomes.click_ok()
        assert incomes.get_total_amount() == 200
        assert incomes.get_amount_by_category(td.salary) == 200
        delete_operation(home_page, incomes)

    @allure.description('Verify that first name field is required')
    def test_delete_op(self, driver, logged_in, incomes, add_income, home_page):
        delete_operation(home_page, incomes)
        assert incomes.get_amount() == 0
        assert incomes.get_amount_by_category(td.salary) == 0


def delete_operation(home_page, incomes):
    home_page.menu_incomes()
    incomes.delete()
    incomes.click_confirm_delete()
    assert incomes.get_total_amount() == 0
