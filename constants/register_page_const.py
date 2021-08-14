class RegisterConstants:
    # input data
    VALID_FIRST_NAME = "username"
    VALID_LAST_NAME = "last_name"
    VALID_EMAIL = "vadim1@yahoo.com"
    VALID_PASSWORD = "abcdefg"
    INVALID_EMAIL = "abc"
    INVALID_PASSWORD = "abcde"

    # input fields
    GENDER_MAIL_CHECK_BOX_xpath = "//input[@id='gender-male']"
    GENDER_FEMAIL_CHECK_BOX_xpath = "//input[@id='gender-female']"

    FIRST_NAME_INPUT_FIELD_xpath = "//input[@id='FirstName']"
    LAST_NAME_INPUT_FIELD_xpath = "//input[@id='LastName']"
    EMAIL_INPUT_FIELD_xpath = "//form[@action='/register']//input[@id='Email']"
    PASSWORD_INPUT_FIELD_xpath = "//form[@action='/register']//input[@id='Password']"
    CONFIRM_PASSWORD_INPUT_FIELD_xpath = "//form[@action='/register']//input[@id='ConfirmPassword']"

    FIRST_NAME_INPUT_FIELD_id = "FirstName"
    LAST_NAME_INPUT_FIELD_id = "LastName"
    EMAIL_INPUT_FIELD_id = "Email"
    PASSWORD_INPUT_FIELD_id = "Password"
    CONFIRM_PASSWORD_INPUT_FIELD_id = "ConfirmPassword"

    # error messages
    FIELD_VALIDATION_ERROR_LIST_xpath = "//span[@class='field-validation-error']"  # list of errors after click 'register'

    FIRST_NAME_ERROR_xpath = "//span/span[@for='FirstName']"
    FIRST_NAME_IS_REQUIRED_text = "First name is required."

    LAST_NAME_ERROR_xpath = "//span/span[@for='LastName']"
    LAST_NAME_IS_REQUIRED_text = "Last name is required."

    EMAIL_ERROR_xpath = "//span/span[@for='Email']"
    EMAIL_IS_REQUIRED_text = "Email is required."
    WRONG_EMAIL_text = "Wrong email"

    PASSWORD_ERROR_xpath = "//span/span[@for='Password']"
    PASSWORD_IS_REQURED_text = "Password is required."
    PASSWORD_SHOULD_HAVE_6_CHAR_text = "The password should have at least 6 characters."

    CONFIRM_PASSWORD_ERROR_xpath = "//span/span[@for='ConfirmPassword']"
    CONFIRM_PASSWORD_MISMATCH_text = "The password and confirmation password do not match."

    REGISTER_BUTTON_xpath = "//input[@id='register-button']"

    EMAIL_ALREADY_EXISTS_xpath = "//div[@class='validation-summary-errors']"
    EMAIL_ALREADY_EXISTS_text = "The specified email already exists"
    SUCCESS_REGISTRATION_xpath = "//div[@class='result']"
    SUCCESS_REGISTRATION_text = "Your registration completed"

    EMAIL_IN_HEADER_xpath = "//a[@class='account' and contains(text(),'{email}')]"


class RegisterObject(RegisterConstants):
    """ create object for work with 'register page' """

    def __init__(self, first_name="", last_name="", email="", password="", confirm_password="",
                 first_name_error_message="", last_name_error_message="", email_error_message="", password_error_message="",
                 confirm_password_error_message=""):
        self.__email = ""
        self.__password = ""
        self.__confirm_password = ""
        self.list_of_field_names = ["FIRST_NAME      ", "LAST_NAME       ", "EMAIL           ", "PASSWORD        ", "CONFIRM_PASSWORD"]
        self.list_of_error_messages = [first_name_error_message, last_name_error_message, email_error_message,
                                       password_error_message, confirm_password_error_message]
        self.list_of_error_xpathes = [self.FIRST_NAME_ERROR_xpath, self.LAST_NAME_ERROR_xpath, self.EMAIL_ERROR_xpath, self.PASSWORD_ERROR_xpath,
                                      self.CONFIRM_PASSWORD_ERROR_xpath]
        self.list_of_input_field_xpathes = [self.FIRST_NAME_INPUT_FIELD_xpath, self.LAST_NAME_INPUT_FIELD_xpath, self.EMAIL_INPUT_FIELD_xpath,
                                            self.PASSWORD_INPUT_FIELD_xpath, self.CONFIRM_PASSWORD_INPUT_FIELD_xpath]
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def click_button(self):
        if self.first_name == "":
            self.list_of_error_messages[0] = self.FIRST_NAME_IS_REQUIRED_text
        if self.last_name == "":
            self.list_of_error_messages[1] = self.LAST_NAME_IS_REQUIRED_text
        if self.email == "":
            self.list_of_error_messages[2] = self.EMAIL_IS_REQUIRED_text
        if self.password == "":
            self.list_of_error_messages[3] = self.PASSWORD_IS_REQURED_text
        if self.confirm_password == "":
            self.list_of_error_messages[4] = self.PASSWORD_IS_REQURED_text

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
        if email != self.VALID_EMAIL and email != "":
            self.list_of_error_messages[2] = self.WRONG_EMAIL_text

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password
        if 1 < len(password) <= 6:
            self.list_of_error_messages[3] = self.PASSWORD_SHOULD_HAVE_6_CHAR_text

    @property
    def confirm_password(self):
        return self.__confirm_password

    @confirm_password.setter
    def confirm_password(self, confirm_password):
        self.__confirm_password = confirm_password
        if confirm_password != "" and confirm_password != self.password:
            self.list_of_error_messages[4] = self.CONFIRM_PASSWORD_MISMATCH_text
