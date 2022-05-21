import pytest

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from constants import login_page_constants as login_const
from constants import header_constants as header_const
from constants import global_constants as global_const
from constants.global_constants import PATH_TO_CHROME_WEBDRIVER, PATH_TO_FIREFOX_WEBDRIVER

from functions.common_functions import CommonFunctions
from functions.helpers import CHROME, FIREFOX
from functions.log_in_functions import LogInFunctions
from functions.register_functions import RegisterFunctions
from functions.category_page_functions import CategoryPageFunctions
from functions.shopping_cart_functions import ShoppingCartFunctions



# @pytest.fixture()
# def start_page():

#     options = Options()
#
#     # options.headless = True
#     driver = webdriver.Chrome(options=options, executable_path=global_const.PATH_TO_CHROME_WEBDRIVER)
#     driver.get(global_const.START_PAGE_url)
#     driver.implicitly_wait(time_to_wait=10)
#     yield CommonFunctions(driver)
#     driver.close()
#


# @pytest.fixture()
# def login_page(start_page):
#     start_page.click_button_and_verify_new_url(button=header_const.LOGIN_BUTTON_IN_HEADER_xpath,
#                                                url=global_const.LOGIN_PAGE_url)
#     return LogInFunctions(start_page.driver)


# @pytest.fixture()
# def register_page(start_page):
#     start_page.click_button_and_verify_new_url(button=header_const.REGISTER_BUTTON_IN_HEADER_class,
#                                                url=global_const.REGISTER_PAGE_url)
#     return RegisterFunctions(start_page.driver)


# @pytest.fixture()
# def product_page_elements(start_page):
#     return CategoryPageFunctions(start_page.driver)


# @pytest.fixture()
# def shopping_cart_unreg(start_page):
#     return ShoppingCartFunctions(start_page.driver)


# @pytest.fixture()
# def shopping_cart_reg(login_page):
#     # login_page.wait_click_ability_and_click(header_const.LOGIN_BUTTON_IN_HEADER_xpath)
#     login_page.fill_login_page_fields_and_click(email_data=login_const.VALID_EMAIL, password_data=login_const.VALID_PASSWORD)
#     login_page.verify_message(locator=login_const.USER_NAME_IN_HEADER_xpath, expected_text=login_const.VALID_EMAIL)
#     return LogInFunctions.fill_login_page_fields_and_click(email_data=login_const.VALID_EMAIL, password_data=login_const.VALID_PASSWORD)
#         CommonFunctions.verify_message(locator=login_const.USER_NAME_IN_HEADER_xpath, expected_text=login_const.VALID_EMAIL)
