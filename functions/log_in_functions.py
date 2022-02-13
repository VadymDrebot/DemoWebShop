from constants import login_page_constants as login_const
from functions.common_functions import CommonFunctions
from constants import header_constants as header_const
from functions.waitings import Waitings


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

        # self.verify_message(locator=login_const.USER_NAME_IN_HEADER_xpath, expected_text=login_const.VALID_EMAIL)

    # def logs_to_console(self,message_locator,expected_text):
    #     self.logger.info(f"\nactual message:'{expected_text}' \n"
    #                            f"is in expected message: '{self.get_text_from_locator(message_locator)}'")
