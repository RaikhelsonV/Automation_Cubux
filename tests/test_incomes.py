from tests.test_data import data as td
import allure


@allure.feature('Incomes Page')
class TestIncomes:

    @allure.story('Add income')
    @allure.description('Make sure that the method add income works correctly.')
    def test_add_income(self, driver, logged_in, incomes, add_income, home_page):
        assert incomes.get_total_amount() == int(td.sum)
        assert incomes.get_amount_by_category(td.salary) == int(td.sum)
        delete_operation(home_page, incomes)

    @allure.story('Add income')
    @allure.description('Ensure that the income information is displayed correctly')
    def test_check_incomes(self, driver, logged_in, incomes, add_income, home_page):
        assert incomes.get_total_amount() == int(td.sum)
        assert incomes.get_amount_by_category(td.salary) == int(td.sum)
        home_page.menu_incomes()
        incomes.get_last_added_transaction_by_name(td.salary)
        assert incomes.get_category_name() == td.salary
        assert incomes.get_amount() == int(td.sum)
        delete_operation(home_page, incomes)

    @allure.story('Edit income')
    @allure.description('Make sure the method to edit income works correctly.')
    def test_edit_income(self, driver, logged_in, incomes, add_income, home_page):
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

    @allure.story('Copy income')
    @allure.description('Make sure the method to copy income works correctly.')
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

    @allure.story('Delete income')
    @allure.description('Make sure the method to delete income works correctly.')
    def test_delete_income(self, driver, logged_in, incomes, add_income, home_page):
        delete_operation(home_page, incomes)
        assert incomes.get_total_amount() == 0
        assert incomes.get_amount() == 0
        assert incomes.get_amount_by_category(td.salary) == 0


def delete_operation(home_page, incomes):
    home_page.menu_incomes()
    incomes.delete()
    incomes.click_confirm_delete()

