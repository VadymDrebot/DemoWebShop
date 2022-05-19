import pytest

from constants import login_page_constants as log_const
from functions.common_functions import CommonFunctions
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from functions.helpers import CHROME, FIREFOX, create_driver
from functions.log_in_functions import LogInFunctions
from constants import login_page_constants as login_const
from constants import header_constants as header_const
from constants import global_constants as global_const
from functions import helpers


@pytest.mark.parametrize("browser_name", [CHROME, FIREFOX])
class TestLogIn:
    """ Test cases for 'Log In' page.
    Log in data:
    1. email - empty,  password - empty
    2. email - empty,  password - valid
    3. email - empty,  password - invalid

    4. email - invalid,  password - empty
    5. email - invalid,  password - valid
    6. email - invalid,  password - invalid

    7. email - valid,  password - empty
    8. email - valid,  password - invalid
    9. email - valid,  password - valid
    """

    def test1_empty_email_and_empty_password(self, login_page):
        """ Summary: login with empty 'email' field
            Preconditions: get in "Log in" page
            Steps:
                   1. verify 'email' field is empty
                   2. verify 'password' field is empty
                   3. click 'log in' button in 'log in' page
                   4. verify log in error message 'Login was unsuccessful. Please...' appears
        """
        login_page.fill_login_page_fields_and_click(email_data="", password_data="")

        login_page.verify_text_partly_present_in_locator(message_locator=log_const.LOGIN_ERROR_MESSAGE_xpath,
                                                         expected_text=log_const.LOGIN_ERROR_MESSAGE_text)

    def test2_empty_email_and_valid_password(self, login_page):
        # 2. email - empty,  password - valid
        login_page.fill_login_page_fields_and_click(email_data="", password_data=log_const.VALID_PASSWORD)

        login_page.verify_text_partly_present_in_locator(message_locator=log_const.LOGIN_ERROR_MESSAGE_xpath,
                                                         expected_text=log_const.LOGIN_ERROR_MESSAGE_text)

    def test4_invalid_email_and_empty_password(self, login_page):
        # 4. email - invalid,  password - empty
        login_page.fill_login_page_fields_and_click(email_data=log_const.INVALID_EMAIL, password_data="")

        login_page.verify_message(locator=log_const.EMAIL_VALIDATION_ERROR_xpath,
                                  expected_text=log_const.EMAIL_VALIDATION_ERROR_MESSAGE_text)

    def test9_valid_email_and_valid_password(self, login_page):
        # 9. email - valid,  password - valid
        login_page.fill_login_page_fields_and_click(email_data=log_const.VALID_EMAIL,
                                                    password_data=log_const.VALID_PASSWORD)
        login_page.verify_message(locator=log_const.USER_NAME_IN_HEADER_xpath,
                                  expected_text=log_const.VALID_EMAIL, comments="username")
