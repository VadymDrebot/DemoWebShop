import constants.login_page_const
from constants.login_page_const import LogInConstants
from functions.neutral_functions import NeutralFunctions


class LogInFunctions(NeutralFunctions, LogInConstants):

    def fill_login_page_fields_and_click(self, email_data, password_data):
        self.wait_send_keys(locator=LogInConstants.EMAIL_INPUT_FIELD_xpath, data=email_data)
        # start_page_const.py.logger.info(email_data)
        self.wait_send_keys(locator=LogInConstants.PASSWORD_INPUT_FIELD_xpath, data=password_data)
        # start_page_const.py.logger.info(password_data)
        self.wait_click_ability_and_click(locator=LogInConstants.LOGIN_BUTTON_IN_LOGIN_PAGE_xpath)

    def logout_and_login(self, email_data=LogInConstants.VALID_EMAIL, password_data=LogInConstants.VALID_PASSWORD):
        self.wait_click_ability_and_click(locator=self.LOGOUT_BUTTON_IN_HEADER_xpath)
        self.wait_click_ability_and_click(locator=self.LOGIN_BUTTON_IN_HEADER_xpath)

        self.fill_login_page_fields_and_click(email_data, password_data)
        self.verify_message(locator=self.USER_NAME_IN_HEADER_xpath, expected_text=self.VALID_EMAIL)
