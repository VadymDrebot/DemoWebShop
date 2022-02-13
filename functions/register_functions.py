import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from constants import register_page_constants as reg_const
from functions.common_functions import CommonFunctions
import textwrap

from functions.project_functions import ProjectFunction


class RegisterObject:
    """ create object for work with 'register page' """

    def __init__(self, first_name="", last_name="", email="", password="", confirm_password="",
                 first_name_error_message="", last_name_error_message="", email_error_message="", password_error_message="",
                 confirm_password_error_message=""):
        self.__email = ""
        self.__password = ""
        self.__confirm_password = ""
        self.list_of_field_names = ["FIRST_NAME", "LAST_NAME", "EMAIL", "PASSWORD", "CONFIRM_PASSWORD"]
        self.list_of_error_messages = [first_name_error_message, last_name_error_message, email_error_message,
                                       password_error_message, confirm_password_error_message]
        self.list_of_error_xpathes = [reg_const.FIRST_NAME_ERROR_xpath, reg_const.LAST_NAME_ERROR_xpath, reg_const.EMAIL_ERROR_xpath,
                                      reg_const.PASSWORD_ERROR_xpath, reg_const.CONFIRM_PASSWORD_ERROR_xpath]
        self.list_of_input_field_xpathes = [reg_const.FIRST_NAME_INPUT_FIELD_xpath, reg_const.LAST_NAME_INPUT_FIELD_xpath,
                                            reg_const.EMAIL_INPUT_FIELD_xpath, reg_const.PASSWORD_INPUT_FIELD_xpath,
                                            reg_const.CONFIRM_PASSWORD_INPUT_FIELD_xpath]
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
        if email != reg_const.VALID_EMAIL and email != "":
            self.list_of_error_messages[2] = reg_const.WRONG_EMAIL_text

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password
        if 1 < len(password) <= 6:
            self.list_of_error_messages[3] = reg_const.PASSWORD_SHOULD_HAVE_6_CHAR_text

    @property
    def confirm_password(self):
        return self.__confirm_password

    @confirm_password.setter
    def confirm_password(self, confirm_password):
        self.__confirm_password = confirm_password
        if confirm_password != "" and confirm_password != self.password:
            self.list_of_error_messages[4] = reg_const.CONFIRM_PASSWORD_MISMATCH_text


class RegisterFunctions(ProjectFunction):
    logger = logging.getLogger(__name__)

    def fill_register_fields(self, user):
        # product_page_constants.py.logger.error(f"password; {user.password}")
        self.wait_send_keys(locator=reg_const.FIRST_NAME_INPUT_FIELD_id, locator_type=By.ID, data=user.first_name)
        self.wait_send_keys(locator=reg_const.LAST_NAME_INPUT_FIELD_id, locator_type=By.ID, data=user.last_name)
        self.wait_send_keys(locator=reg_const.EMAIL_INPUT_FIELD_id, locator_type=By.ID, data=user.email)
        self.wait_send_keys(locator=reg_const.PASSWORD_INPUT_FIELD_id, locator_type=By.ID, data=user.password)
        self.wait_send_keys(locator=reg_const.CONFIRM_PASSWORD_INPUT_FIELD_id, locator_type=By.ID, data=user.confirm_password)
        self.press_keyboard_button(button=Keys.TAB)

    def verify_error_messages(self, user):
        """ if field's 'error_message' should be empty -- verify there is no any error message in field's 'error_message' xpath
            if field's 'error_messages' is NOT empty -- verify there is appropriate error message presents in its xpath

        list_of_error_messages = [first_name_error_message, last_name_error_message, email_error_message,
                                 password_error_message, confirm_password_message]
        list_of_error_xpathes = [user.FIRST_NAME_ERROR_xpath, user.LAST_NAME_ERROR_xpath, user.EMAIL_ERROR_xpath,
                                user.PASSWORD_ERROR_xpath, user.CONFIRM_PASSWORD_ERROR_xpath]
        list_of_field_names = ["FIRST_NAME", "LAST_NAME", "EMAIL", "PASSWORD", "CONFIRM_PASSWORD"]
        list_of_input_field_xpathes = [product_page_constants.py.FIRST_NAME_INPUT_FIELD_xpath, product_page_constants.py.LAST_NAME_INPUT_FIELD_xpath,
                                      product_page_constants.py.EMAIL_INPUT_FIELD_xpath, product_page_constants.py.PASSWORD_INPUT_FIELD_xpath,
                                      product_page_constants.py.CONFIRM_PASSWORD_INPUT_FIELD_xpath]"""
        for error_message, error_xpath, field_name, input_field_xpath in zip(user.list_of_error_messages, user.list_of_error_xpathes,
                                                                             user.list_of_field_names, user.list_of_input_field_xpathes):
            if error_message == "":
                assert not self.verify_presence_of_element(error_xpath)
            else:
                self.verify_message(locator=error_xpath, expected_text=error_message)
            self.logger.info(
                f" value of the {field_name:18} field: --{self.get_value_from_input_field(input_field_xpath):18}--   Error message actual result: --{self.get_text_from_locator(error_xpath)}--")

    def click_register_button(self, user):
        self.wait_click_ability_and_click(reg_const.REGISTER_BUTTON_xpath)
        i = 0
        for field in [user.first_name, user.last_name, user.email, user.password, user.confirm_password]:
            if field == "":
                user.list_of_error_messages[i] = reg_const.IS_REQUIRED_messages[i]
            i += 1

