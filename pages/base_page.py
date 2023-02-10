import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from price_parser import Price
import re


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.page_url = ''

    def open(self):
        if self.page_url:
            self.driver.get(self.page_url)
        else:
            raise NotImplementedError

    def find(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def find_nested_el(self, locator_list, index, locator_sub_list, sub_index):
        nested_list = self.find_all(locator_list)
        return nested_list[index].find_elements(*locator_sub_list)[sub_index]

    def click(self, locator):
        element = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        element.click()

    def click_from_list(self, locator, option):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(locator))
        list_elements = self.driver.find_elements(*locator)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(list_elements[option]))
        list_elements[option].click()

    def set_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(text)

    def get_text(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element.text

    def get_attribute(self, locator, attr):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element.get_attribute(attr)

    def is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def is_selected(self, locator):
        element = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_selected(element))
        return element.is_selected()

    def switch_tab(self, tab):
        self.driver.switch_to.window(self.driver.window_handles[tab])

    def accept_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        Alert(self.driver).accept()

    def scroll_to_the_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)

    def scroll_to_the_top(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)

    def get_alert_message(self, locator):
        element = self.driver.find_element(*locator)
        return self.driver.execute_script("return arguments[0].validationMessage;", element)

    def get_alert_state(self, locator):
        element = self.driver.find_element(*locator)
        return self.driver.execute_script("return arguments[0].checkValidity();", element)

    def get_current_url(self):
        return self.driver.current_url

    def select_by_value(self, locator, value):
        select = Select(self.driver.find_element(*locator))
        select.select_by_value(value)

    def press_down_arrow(self, locator):
        element = self.driver.find_element(*locator)
        element.send_keys(Keys.DOWN)
        element.send_keys(Keys.ENTER)

    def refresh(self):
        self.driver.refresh()
        time.sleep(10)

    @staticmethod
    def extract_digits_from_str(value):
        return int(re.findall(r'\d+', value)[0])

    @staticmethod
    def extract_currency_from_str(value):
        price = Price.fromstring(value)
        if value.__contains__('-'):
            return int(price.amount) * (-1)
        else:
            return int(price.amount)
