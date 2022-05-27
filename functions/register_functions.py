from selenium.webdriver.common.keys import Keys

from constants import register_page_constants as reg_const

from functions.project_functions import ProjectFunction
from functions import helpers


class Fields:
    def __init__(self, field_name, input_value, input_field_xpath, error_xpath, error_message=""):
        self.field_name = field_name
        self.input_value = input_value
        self.input_field_xpath = input_field_xpath
        self.error_xpath = error_xpath
        self.error_message = error_message


class RegisterObject(ProjectFunction):
    """ create object for work with 'register page' """

    def __init__(self, driver):
        super().__init__(driver)

        self.__first_name = Fields(*reg_const.params_for_first_name_object)
        self.__last_name = Fields(*reg_const.params_for_last_name_object)
        self.__email = Fields(*reg_const.params_for_email_object)
        self.__password = Fields(*reg_const.params_for_password_object)
        self.__confirm_password = Fields(*reg_const.params_for_confirm_password_object)

        self.obj_field_names = "first_name", "last_name", "email", "password", "confirm_password"

        self.__clicked_register_button = False
        self.empty_error_messages_flag = False

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
    def email(self, email_value):
        self.__email.input_value = email_value
        if email_value and not helpers.verify_email(email_value):
            self.__email.error_message = reg_const.WRONG_EMAIL_text

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password_value):
        self.__password.input_value = password_value
        if not helpers.verify_password(password_value):
            self.__password.error_message = reg_const.PASSWORD_SHOULD_HAVE_6_CHAR_text

    @property
    def confirm_password(self):
        return self.__confirm_password

    @confirm_password.setter
    def confirm_password(self, confirm_password_value):
        self.__confirm_password.input_value = confirm_password_value
        if confirm_password_value != self.__password.input_value and confirm_password_value:
            self.__confirm_password.error_xpath = reg_const.CONFIRM_PASSWORD_ERROR_xpath
            self.__confirm_password.error_message = reg_const.CONFIRM_PASSWORD_MISMATCH_text

    @property
    def clicked_register_button(self):
        return self.__clicked_register_button

    @clicked_register_button.setter
    def clicked_register_button(self, value):
        if not self.__first_name.input_value:
            self.__first_name.error_message = reg_const.FIRST_NAME_IS_REQUIRED_text

        if not self.__last_name.input_value:
            self.__last_name.error_message = reg_const.LAST_NAME_IS_REQUIRED_text

        if not helpers.verify_email(self.__email.input_value):
            self.__email.error_message = reg_const.WRONG_EMAIL_text
            if not self.__email.input_value:
                self.__email.error_message = reg_const.EMAIL_IS_REQUIRED_text

        if not helpers.verify_password(self.__password.input_value):
            self.__password.error_message = reg_const.PASSWORD_SHOULD_HAVE_6_CHAR_text
        if not self.__password.input_value:
            self.__password.error_message = reg_const.PASSWORD_IS_REQURED_text

        if self.__confirm_password.input_value != self.__password.input_value and self.__confirm_password.input_value:
            self.__confirm_password.error_message = reg_const.CONFIRM_PASSWORD_MISMATCH_text
        if not self.__confirm_password.input_value:
            self.__confirm_password.error_message = reg_const.PASSWORD_IS_REQURED_text

        if not self.__first_name.error_message and \
                not self.__last_name.error_message and \
                not self.__email.error_message and \
                not self.__password.error_message and \
                not self.__confirm_password.error_message:
            if self.__email.input_value == reg_const.EXISTING_EMAIL:
                self.__email.error_xpath = reg_const.EMAIL_ALREADY_EXISTS_xpath
                self.__email.error_message = reg_const.EMAIL_ALREADY_EXISTS_text
            else:
                # set flag if email != OUR existing email
                self.empty_error_messages_flag = True

    def verify_error_messages(self):
        """ if field's 'error_message' should be empty -- verify there is no any error message in field's 'error_message' xpath
            if field's 'error_messages' is NOT empty -- verify there is appropriate error message presents in its xpath """
        if self.empty_error_messages_flag and not self.check_presence_of_element(reg_const.EMAIL_ALREADY_EXISTS_xpath):
            # verify OUR existing email by flag AND somebody's else existing email
            self.verify_message(locator=reg_const.SUCCESS_REGISTRATION_xpath, expected_text=reg_const.SUCCESS_REGISTRATION_text)
            self.logger.info(f"{self.get_text_from_locator(locator=reg_const.SUCCESS_REGISTRATION_xpath)}")
        else:
            for field_name in self.obj_field_names:
                self_dot_field_name = eval("object." + field_name, {"object": self})
                if not self_dot_field_name.error_message:
                    assert not self.check_presence_of_element(self_dot_field_name.error_xpath)
                    actual_error_message = ""
                else:
                    self.verify_message(locator=self_dot_field_name.error_xpath, expected_text=self_dot_field_name.error_message)
                    actual_error_message = self.get_text_from_locator(self_dot_field_name.error_xpath)
                    self.empty_error_messages_flag = True
                self.logger.info(
                    f"Field: --{self_dot_field_name.field_name:16}--   Value: --{self.get_value_from_input_field(self_dot_field_name.input_field_xpath):16}--   ACTUAL error message: --{actual_error_message:24}-- EXPECTED error message: --{self_dot_field_name.error_message:24}--")

    def fill_register_fields_with_tab_click(self, first_name_value, last_name_value, email_value, password_value, confirm_password_value):
        # fill 'first_name' field
        self.wait_send_keys_and_click_button(locator=self.first_name.input_field_xpath, data=first_name_value, button=Keys.TAB)
        self.first_name = first_name_value

        # fill 'last_name' field
        self.wait_send_keys_and_click_button(locator=self.last_name.input_field_xpath, data=last_name_value, button=Keys.TAB)
        self.last_name = last_name_value

        # fill 'email' field
        self.wait_send_keys_and_click_button(locator=self.email.input_field_xpath, data=email_value, button=Keys.TAB)
        self.email = email_value

        # fill 'password' field
        self.wait_send_keys_and_click_button(locator=self.password.input_field_xpath, data=password_value, button=Keys.TAB)
        self.password = password_value

        # fill 'confirm_password' field
        self.wait_send_keys_and_click_button(locator=self.confirm_password.input_field_xpath, data=confirm_password_value, button=Keys.TAB)
        self.confirm_password = confirm_password_value

    def click_register_button_and_change_error_messages(self):
        self.wait_click_ability_and_click(locator=reg_const.REGISTER_BUTTON_xpath)
        self.clicked_register_button = True
