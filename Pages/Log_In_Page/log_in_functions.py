import logging

from selenium.webdriver.common.keys import Keys

from Helpers.logging_functions import create_logger, log
from Pages.Log_In_Page import log_in_page_constants as sign_const
from Pages.Header import header_constants as header_const

from Helpers.helpers import verify_email
from Helpers.common_functions import CommonFunctions


class LoginFunctions(CommonFunctions):

    @log
    def verify_login_error_messages_no_click(self, email, logger, test_name):

        # email INVALID and NOT EMPTY (no matter, LogIn button clicked or not)
        if email and not verify_email(email):
            self.verify_message(locator=sign_const.EMAIL_VALIDATION_ERROR_xpath, expected_text=sign_const.EMAIL_VALIDATION_ERROR_text)
        else:

            assert not self.check_presence_of_element(locator=sign_const.EMAIL_VALIDATION_ERROR_xpath)
            assert not self.check_presence_of_element(locator=sign_const.LOGIN_ERROR_MESSAGE_xpath)
            assert not self.check_presence_of_element(locator=sign_const.CREDENTIAL_ERROR_MESSAGE_xpath)

    @log
    def verify_login_error_messages_after_click(self, email, password, logger, test_name):
        if email and not verify_email(email):
            # self.verify_login_error_messages_no_click(email, logger, test_name)
            self.verify_message(locator=sign_const.EMAIL_VALIDATION_ERROR_xpath, expected_text=sign_const.EMAIL_VALIDATION_ERROR_text)

        # email EXISTING
        elif email == sign_const.EXISTING_EMAIL:
            # and password INVALID
            if password != sign_const.EXISTING_PASSWORD:
                self.verify_message(locator=sign_const.LOGIN_ERROR_MESSAGE_xpath, expected_text=sign_const.LOGIN_ERROR_MESSAGE_text)
                self.verify_message(locator=sign_const.CREDENTIAL_ERROR_MESSAGE_xpath, expected_text=sign_const.CREDENTIAL_ERROR_EXISTING_EMAIL_text)
            # and password EXISTING
            if password == sign_const.EXISTING_PASSWORD:
                self.verify_message(locator=sign_const.USER_NAME_IN_HEADER_xpath, expected_text=email)

        # email VALID
        elif verify_email(email):
            self.verify_message(locator=sign_const.LOGIN_ERROR_MESSAGE_xpath, expected_text=sign_const.LOGIN_ERROR_MESSAGE_text)
            self.verify_message(locator=sign_const.CREDENTIAL_ERROR_MESSAGE_xpath, expected_text=sign_const.CREDENTIAL_ERROR_NO_CUSTOMER__text)

        self.logging_errors("after  click")

    def logging_errors(self, text):
        self.logger.debug(f"\n     Email error --{text}--  :  --{self.get_text_from_locator(locator=sign_const.EMAIL_VALIDATION_ERROR_xpath)}--\n"
                          f"  Password error --{text}--  :  --{self.get_text_from_locator(locator=sign_const.CREDENTIAL_ERROR_MESSAGE_xpath)}--\n"
                          f"     Login error --{text}--  :  --{self.get_text_from_locator(locator=sign_const.LOGIN_ERROR_MESSAGE_xpath)}--")

    def fill_login_page_fields(self, email_data, password_data):
        self.wait_send_keys_and_click_button(locator=sign_const.EMAIL_INPUT_FIELD_xpath, data=email_data, button=Keys.TAB)
        self.wait_send_keys_and_click_button(locator=sign_const.PASSWORD_INPUT_FIELD_xpath, data=password_data, button=Keys.TAB)
        self.logger.info(f"\nField values:  email: --{self.get_value_from_input_field(locator=sign_const.EMAIL_INPUT_FIELD_xpath)}--\n"
                         f"            password: --{self.get_value_from_input_field(locator=sign_const.PASSWORD_INPUT_FIELD_xpath)}--")
        self.logging_errors("before click")

    def login(self, email_data, password_data):
        self.wait_click_ability_and_click(locator=header_const.LOGIN_BUTTON_IN_HEADER_xpath)
        self.fill_login_page_fields(email_data, password_data)

    def logout(self):
        self.wait_click_ability_and_click(locator=header_const.LOGOUT_BUTTON_IN_HEADER_xpath)

    def logout_and_login(self, email_data=sign_const.VALID_EMAIL, password_data=sign_const.EXISTING_PASSWORD):
        self.logout()
        self.login(email_data=email_data, password_data=password_data)
