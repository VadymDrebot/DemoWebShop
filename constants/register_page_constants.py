# input data
VALID_FIRST_NAME = "valid username"
VALID_LAST_NAME = "valid last_name"
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

IS_REQUIRED_messages = [FIRST_NAME_IS_REQUIRED_text, LAST_NAME_IS_REQUIRED_text, EMAIL_IS_REQUIRED_text, PASSWORD_IS_REQURED_text,
                        PASSWORD_IS_REQURED_text]
