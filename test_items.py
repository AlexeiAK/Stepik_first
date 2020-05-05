import time
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_is_present(browser):
    try:
        browser.get(link)
        button = browser.find_element_by_css_selector("#add_to_basket_form > butto").get_attribute('value')
        time.sleep(10)
    except NoSuchElementException:
        assert False, 'Button "add to card" not found'
        
    