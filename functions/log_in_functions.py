import constants.login_page_const
from constants.login_page_const import LogInConstants
from functions.common_functions import CommonFunctions


class LogInFunctions(CommonFunctions, LogInConstants):

    def fill_login_page_fields_and_click(self, email_data, password_data):

        self.wait_send_keys(locator=LogInConstants.EMAIL_INPUT_FIELD_xpath, data=email_data)
        # self.logger.info(email_data)
        self.wait_send_keys(locator=LogInConstants.PASSWORD_INPUT_FIELD_xpath, data=password_data)
        # self.logger.info(password_data)
        self.wait_click_ability_and_click(locator=LogInConstants.LOGIN_BUTTON_IN_LOGIN_PAGE_xpath)
