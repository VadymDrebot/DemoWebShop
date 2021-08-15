from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from constants import start_page_const
# from constants.register_page_const import RegisterConstants
from constants.register_page_const import RegisterObject
from constants.start_page_const import LOGIN_BUTTON_IN_HEADER_xpath, REGISTER_BUTTON_IN_HEADER_xpath, REGISTER_BUTTON_IN_HEADER_class, REGISTER_PAGE_url
from functions.common_functions import CommonFunctions
from functions.log_in_functions import LogInFunctions
from functions.register_functions import RegisterFunctions
from functions.shopping_cart_functions import ShoppingCartFunctions


@pytest.fixture()
def start_page():
    driver = webdriver.Chrome(executable_path=start_page_const.PATH_TO_CHROME_WEBDRIVER)
    driver.get(start_page_const.START_PAGE_url)
    driver.implicitly_wait(time_to_wait=10)
    yield CommonFunctions(driver)
    driver.close()


@pytest.fixture()
def login_page(start_page):
    start_page.wait_click_ability_and_click(LOGIN_BUTTON_IN_HEADER_xpath)
    return LogInFunctions(start_page.driver)


@pytest.fixture()
def register_page(start_page):
    start_page.click_button_and_verify_new_url(button_locator_type=By.CLASS_NAME, button_locator=REGISTER_BUTTON_IN_HEADER_class, url=REGISTER_PAGE_url)
    return RegisterFunctions(start_page.driver)


@pytest.fixture()
def shopping_cart_page(start_page):
    return ShoppingCartFunctions(start_page.driver)
