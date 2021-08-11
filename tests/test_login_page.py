import pytest, logging
from constants.start_page_const import LOGIN_BUTTON_IN_HEADER_xpath
from functions.common_functions import CommonFunctions
from constants.login_page_const import LogInConstants


class TestLoginPage:
    """ tests for 'Log In' page.
    Log in with:
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

    def test1_empty_fields(self, login_page):
        """ Summary: login with empty 'email' field
            Preconditions: get in "Log in" page
            Steps:
                   1. verify 'email' field is empty
                   2. verify 'password' field is empty
                   3. click 'log in' button in 'log in' page
                   4. verify log in error message 'Login was unsuccessful. Please...' appears
        """
        login_page.fill_login_page_fields_and_click(email_data="", password_data="")

        login_page.verify_text_presence_in_message(message_locator=LogInConstants.LOGIN_ERROR_MESSAGE_xpath,
                                                   expected_text=LogInConstants.LOGIN_ERROR_MESSAGE_text)
        # login_page.logger.info(f"\nactual message:'{LogInConstants.LOGIN_ERROR_MESSAGE_text}' \n"
        #                        f"is in expected message: '{login_page.get_text_from_xpath(LogInConstants.LOGIN_ERROR_MESSAGE_xpath)}'")

    def test2_email_empty_passw_valid(self, login_page):
        # 2. email - empty,  password - valid
        login_page.fill_login_page_fields_and_click(email_data="", password_data=LogInConstants.VALID_PASSWORD)

        login_page.verify_text_presence_in_message(message_locator=LogInConstants.LOGIN_ERROR_MESSAGE_xpath,
                                                   expected_text=LogInConstants.LOGIN_ERROR_MESSAGE_text)
        # login_page.logger.info(f"\nactual message:'{LogInConstants.LOGIN_ERROR_MESSAGE_text}' \n"
        #                        f"is in expected message: '{login_page.get_text_from_xpath(LogInConstants.LOGIN_ERROR_MESSAGE_xpath)}'")

    def test4_invalid_email__empty_password(self, login_page):
        # 4. email - invalid,  password - empty
        login_page.fill_login_page_fields_and_click(email_data=login_page.random_word(), password_data="")
        login_page.verify_message(locator="//span[@class='field-validation-error']",
                                  expected_text=LogInConstants.EMAIL_VALIDATION_ERROR_MESSAGE_text)

    def test9_valid_email__valid_password(self, login_page):
        # 9. email - valid,  password - valid
        login_page.fill_login_page_fields_and_click(email_data=LogInConstants.VALID_EMAIL,
                                                    password_data=LogInConstants.VALID_PASSWORD)
        login_page.verify_message(locator=LogInConstants.USER_NAME_IN_HEADER_xpath,
                                  expected_text=LogInConstants.VALID_EMAIL)
        # login_page.logger.info(f"\n       username in header: -{login_page.get_text_from_xpath(LogInConstants.USER_NAME_IN_HEADER_xpath)}-"
        #                        f"\n matches inputed username: -{LogInConstants.VALID_EMAIL}-")
