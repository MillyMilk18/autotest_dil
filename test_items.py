import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_add_to_basket_button(browser):
    browser.get(link)
    #time.sleep(10)
    assert browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')


