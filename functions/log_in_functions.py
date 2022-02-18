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

    def login(self, email_data=login_const.VALID_EMAIL, password_data=login_const.VALID_PASSWORD):
        self.wait_click_ability_and_click(locator=header_const.LOGIN_BUTTON_IN_HEADER_xpath)
        self.fill_login_page_fields_and_click(email_data, password_data)

    def logout(self):
        self.wait_click_ability_and_click(locator=header_const.LOGOUT_BUTTON_IN_HEADER_xpath)

    def logout_and_login(self):
        self.logout()
        self.login(email_data=login_const.VALID_EMAIL, password_data=login_const.VALID_PASSWORD)
