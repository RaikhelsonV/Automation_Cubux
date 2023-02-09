from selenium.webdriver.common.by import By

logo = (By.CSS_SELECTOR, "[alt='CUBUX Logo']")
start_btn = (By.CSS_SELECTOR, '.txt')
menu = (By.CSS_SELECTOR, '.PageHeader_toolbarLarge__OXhVD')
incomes_menu = (By.CSS_SELECTOR, '.PageHeader_toolbarLarge__OXhVD .color-income')
expenses_menu = (By.CSS_SELECTOR, '.PageHeader_toolbarLarge__OXhVD .color-expense')
loans_menu = (By.CSS_SELECTOR, '.PageHeader_toolbarLarge__OXhVD .color-debt')
name = (By.CSS_SELECTOR, '.main-team-name')
incomes = (By.CSS_SELECTOR, '.hex-index-income .hex-value>span')
expenses = (By.CSS_SELECTOR, '.hex-index-expense .hex-value>span')
balance = (By.CSS_SELECTOR, '.hex-index-balance .hex-value>span')
calendar = (By.CSS_SELECTOR, '.hex-index-calendar .hex-value>span')
