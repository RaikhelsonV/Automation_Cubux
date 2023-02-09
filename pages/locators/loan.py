from selenium.webdriver.common.by import By

partner_name = (By.CSS_SELECTOR, '.modal-hex-title span')
edit_partner = (By.CSS_SELECTOR, '.modal-hex-title>span>:nth-child(1)')
remove_partner = (By.CSS_SELECTOR, '.modal-hex-title>span>:nth-child(2)')
actions_debt = (By.CSS_SELECTOR, ".Grid_col__NSAHt.Grid_span_auto__MRWBY>button")
export_excel = (By.CSS_SELECTOR, "[title='Export to Excel']")
amount_status_form = (By.CSS_SELECTOR, '.sub-title>button')
status = (By.CSS_SELECTOR, '.Grid_col__NSAHt.Grid_span_only_sm_4__ApUuT>span')
status_sub = (By.CSS_SELECTOR, '.extra-margin1 .color-grey')
total_account_debt = (By.CSS_SELECTOR, '.Grid_col__NSAHt.Grid_span_only_sm_4__ApUuT>:nth-child(2)')
save_btn = (By.CSS_SELECTOR, '.btn')
delete_btns = (By.CSS_SELECTOR, '.rc-dialog-footer .color-danger')
one_hundred_percent = (By.CSS_SELECTOR, '.ProcPending_percent__3dujJ')
close_btn = (By.CSS_SELECTOR, '.rc-dialog-close')
