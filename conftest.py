from selenium import webdriver
import pytest
from selenium.webdriver.firefox.options import Options

from constants import start_page_const
# from constants.register_page_const import RegisterConstants
from constants.start_page_const import LOGIN_BUTTON_IN_HEADER_xpath, REGISTER_BUTTON_IN_HEADER_xpath
from functions.common_functions import CommonFunctions
from functions.log_in_functions import LogInFunctions
from functions.register_functions import RegisterFunctions


# @pytest.fixture()
# def start_page():
#     options = Options()
#     options.headless = True
#     driver = webdriver.Firefox(options=options,executable_path=start_page_const.PATH_TO_FIREFOX__WEBDRIVER)
#     driver.get(start_page_const.START_PAGE_url)
#     driver.implicitly_wait(time_to_wait=10)
#     yield CommonFunctions(driver)
#     driver.close()
#
#
# @pytest.fixture()
# def login_page(start_page):
#     start_page.wait_click_ability_and_click(LOGIN_BUTTON_IN_HEADER_xpath)
#     return LogInFunctions(start_page.driver)
#
#
# @pytest.fixture()
# def register_page(start_page):
#     start_page.wait_click_ability_and_click(REGISTER_BUTTON_IN_HEADER_xpath)
#     return RegisterFunctions(start_page.driver)
