import logging

from constants.register_page_const import RegisterConstants as RegConst
from functions.common_functions import CommonFunctions
import textwrap


class RegisterFunctions(CommonFunctions, RegConst):
    logger = logging.getLogger(__name__)

    def fill_register_fields(self, user):
        # self.logger.error(f"password; {user.password}")
        self.wait_send_keys(locator=user.FIRST_NAME_INPUT_FIELD_xpath, data=user.first_name)
        self.wait_send_keys(locator=user.LAST_NAME_INPUT_FIELD_xpath, data=user.last_name)
        self.wait_send_keys(locator=user.EMAIL_INPUT_FIELD_xpath, data=user.email)
        self.wait_send_keys(locator=user.PASSWORD_INPUT_FIELD_xpath, data=user.password)
        self.wait_send_keys(locator=user.CONFIRM_PASSWORD_INPUT_FIELD_xpath, data=user.confirm_password)
        self.tab_click()

    # def verify_email(self, email):
    #     if email.index("@") > 0:
    #         if email.index(".") - email.index("@") > 1:
    #             return True
    #         else:
    #             return False

    def verify_error_messages(self, user):
        """ if field's 'error_message' should be empty -- verify there is no any error message in field's 'error_message' xpath
            if field's 'error_messages' is NOT empty -- verify there is appropriate error message presents in its xpath"""
        # list_of_error_messages =
        #                   [first_name_error_message, last_name_error_message, email_error_message, password_error_message, confirm_password_message]
        # list_of_xpathes = [user.FIRST_NAME_ERROR_xpath, user.LAST_NAME_ERROR_xpath, user.EMAIL_ERROR_xpath, user.PASSWORD_ERROR_xpath,
        #                    user.CONFIRM_PASSWORD_ERROR_xpath]
        # list_of_field_names = ["FIRST_NAME", "LAST_NAME", "EMAIL", "PASSWORD", "CONFIRM_PASSWORD"]
        for error_message, xpath, field_name in zip(user.list_of_error_messages, user.list_of_xpathes, user.list_of_field_names):
            if error_message == "":
                assert not self.verify_presence_of_element(xpath)
                # self.logger.info(f" {field_name} error message field:   -empty-")
            else:
                self.verify_message(locator=xpath, expected_text=error_message)
                # self.logger.info(f" {field_name} error message field:  Actual result: -{self.get_text_from_xpath(xpath)}-")

        # self.logger.info(" -----------END OF THE TEST---------")

    def click_register_button(self, user):
        self.wait_click_ability_and_click(user.REGISTER_BUTTON_xpath)
        user.click_button()
