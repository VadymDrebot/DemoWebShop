import logging

from selenium.webdriver.common.keys import Keys

from constants import register_page_constants as reg_const

from functions.helpers import verify_email
from functions.project_functions import ProjectFunction


class Fields:
    def __init__(self, field_name, input_value, input_field_xpath, error_xpath, error_message=""):
        self.field_name = field_name
        self.input_value = input_value
        self.input_field_xpath = input_field_xpath
        self.error_xpath = error_xpath
        self.error_message = error_message


class RegisterObject:
    """ create object for work with 'register page' """

    def __init__(self, first_name, last_name, email, password, confirm_password):
        self.__first_name = Fields(*reg_const.params_for_first_name_object)
        self.__last_name = Fields(*reg_const.params_for_last_name_object)
        self.__email = Fields(*reg_const.params_for_email_object)
        self.__password = Fields(*reg_const.params_for_password_object)
        self.__confirm_password = Fields(*reg_const.params_for_confirm_password_object)

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.obj_attributes = "first_name", "last_name", "email", "password", "confirm_password"

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name.input_value = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name.input_value = last_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email.input_value = email
        if email:
            if not verify_email(email):
                self.__email.error_message = reg_const.WRONG_EMAIL_text
            elif email == reg_const.EXISTING_EMAIL:
                self.__email.error_xpath = reg_const.EMAIL_ALREADY_EXISTS_xpath
                self.__email.error_message = reg_const.EMAIL_ALREADY_EXISTS_text

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password.input_value = password
        if 1 < len(password) <= 6:
            self.__password.error_message = reg_const.PASSWORD_SHOULD_HAVE_6_CHAR_text

    @property
    def confirm_password(self):
        return self.__confirm_password

    @confirm_password.setter
    def confirm_password(self, confirm_password):
        self.__confirm_password.input_value = confirm_password
        if confirm_password != "" and confirm_password != self.__password.input_value:
            self.__confirm_password.error_message = reg_const.CONFIRM_PASSWORD_MISMATCH_text


class RegisterFunctions(ProjectFunction):
    logger = logging.getLogger()

    def fill_register_fields(self, user):
        for atr in user.obj_attributes:
            user_atr = eval("object." + atr, {"object": user})
            self.wait_send_keys(locator=user_atr.input_field_xpath, data=user_atr.input_value)
        self.press_keyboard_button(button=Keys.TAB)

    def verify_error_messages(self, user):
        """ if field's 'error_message' should be empty -- verify there is no any error message in field's 'error_message' xpath
            if field's 'error_messages' is NOT empty -- verify there is appropriate error message presents in its xpath """
        for atr in user.obj_attributes:
            user_atr = eval("object." + atr, {"object": user})
            if not user_atr.error_message:
                assert not self.check_presence_of_element(user_atr.error_xpath)
            else:
                self.verify_message(locator=user_atr.error_xpath, expected_text=user_atr.error_message)

            self.logger.info(
                f" value of the {user_atr.field_name:18} field: --{self.get_value_from_input_field(user_atr.input_field_xpath):18}--  Error message actual result: --{self.get_text_from_locator(user_atr.error_xpath)}")

    def click_register_button(self, user):
        self.wait_click_ability_and_click(reg_const.REGISTER_BUTTON_xpath)
        for atr in user.obj_attributes:
            user_atr = eval("object." + atr, {"object": user})
            if user_atr.input_value == "":
                user_atr.error_message = reg_const.IS_REQUIRED_messages[atr]
