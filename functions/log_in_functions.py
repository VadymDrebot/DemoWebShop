from constants import login_page_constants as login_const
from constants import header_constants as header_const

from functions.common_functions import CommonFunctions


class LogInFunctions(CommonFunctions):

    def fill_login_page_fields_and_click(self, email_data, password_data):
        self.wait_send_keys(locator=login_const.EMAIL_INPUT_FIELD_xpath, data=email_data)
        # self.logger.info(email_data)
        self.wait_send_keys(locator=login_const.PASSWORD_INPUT_FIELD_xpath, data=password_data)
        # self.logger.info(password_data)

        self.wait_click_ability_and_click(login_const.LOGIN_BUTTON_IN_LOGIN_PAGE_xpath)

    def login(self, email_data, password_data):
        self.wait_click_ability_and_click(locator=header_const.LOGIN_BUTTON_IN_HEADER_xpath)
        self.fill_login_page_fields_and_click(email_data, password_data)

    def logout(self):
        self.wait_click_ability_and_click(locator=header_const.LOGOUT_BUTTON_IN_HEADER_xpath)

    def logout_and_login(self, email_data=login_const.VALID_EMAIL, password_data=login_const.VALID_PASSWORD):
        self.logout()
        self.login(email_data=email_data, password_data=password_data)

    def fill_login_fields_click_verify_partial_text(self, message_locator, expected_text, email_data="", password_data=""):
        self.fill_login_page_fields_and_click(email_data=email_data, password_data=password_data)
        self.verify_text_partly_present_in_locator(message_locator, expected_text)

    def fill_login_fields_click_verify_message(self, message_locator, expected_text, comments="", email_data="", password_data=""):
        self.fill_login_page_fields_and_click(email_data=email_data, password_data=password_data)
        self.verify_message(locator=message_locator, expected_text=expected_text, comments=comments)
