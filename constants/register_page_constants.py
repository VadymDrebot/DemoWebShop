from selenium.webdriver.common.by import By
from functions import helpers

VALID_FIRST_NAME = "valid username"
VALID_LAST_NAME = "valid last_name"
VALID_EMAIL = helpers.random_valid_email()
VALID_PASSWORD = helpers.random_valid_password()
VALID_CONFIRM_PASSWORD = VALID_PASSWORD

EXISTING_EMAIL = "vadim1@yahoo.com"

INVALID_EMAIL = helpers.random_invalid_email()
INVALID_PASSWORD = helpers.random_invalid_password()
INVALID_CONFIRM_PASSWORD = VALID_PASSWORD + "abc"

# input fields
GENDER_MAIL_CHECK_BOX_xpath = (By.XPATH, "//input[@id='gender-male']")
GENDER_FEMAIL_CHECK_BOX_xpath = (By.XPATH, "//input[@id='gender-female']")

FIRST_NAME_INPUT_FIELD_xpath = (By.XPATH, "//input[@id='FirstName']")
LAST_NAME_INPUT_FIELD_xpath = (By.XPATH, "//input[@id='LastName']")
EMAIL_INPUT_FIELD_xpath = (By.XPATH, "//form[@action='/register']//input[@id='Email']")
PASSWORD_INPUT_FIELD_xpath = (By.XPATH, "//form[@action='/register']//input[@id='Password']")
CONFIRM_PASSWORD_INPUT_FIELD_xpath = (By.XPATH, "//form[@action='/register']//input[@id='ConfirmPassword']")

FIRST_NAME_INPUT_FIELD_id = (By.ID, "FirstName")
LAST_NAME_INPUT_FIELD_id = (By.ID, "LastName")
EMAIL_INPUT_FIELD_id = (By.ID, "Email")
PASSWORD_INPUT_FIELD_id = (By.ID, "Password")
CONFIRM_PASSWORD_INPUT_FIELD_id = (By.ID, "ConfirmPassword")

# error messages
FIELD_VALIDATION_ERROR_LIST_xpath = (By.XPATH, "//span[@class='field-validation-error']")  # list of errors after click 'register'

FIRST_NAME_ERROR_xpath = (By.XPATH, "//span/span[@for='FirstName']")
FIRST_NAME_IS_REQUIRED_text = "First name is required."

LAST_NAME_ERROR_xpath = (By.XPATH, "//span/span[@for='LastName']")
LAST_NAME_IS_REQUIRED_text = "Last name is required."

EMAIL_ERROR_xpath = (By.XPATH, "//span/span[@for='Email']")
EMAIL_IS_REQUIRED_text = "Email is required."
WRONG_EMAIL_text = "Wrong email"

PASSWORD_ERROR_xpath = (By.XPATH, "//span/span[@for='Password']")
PASSWORD_IS_REQURED_text = "Password is required."
PASSWORD_SHOULD_HAVE_6_CHAR_text = "The password should have at least 6 characters."

CONFIRM_PASSWORD_ERROR_xpath = (By.XPATH, "//span/span[@for='ConfirmPassword']")
CONFIRM_PASSWORD_MISMATCH_text = "The password and confirmation password do not match."

REGISTER_BUTTON_xpath = (By.XPATH, "//input[@id='register-button']")

EMAIL_ALREADY_EXISTS_xpath = (By.XPATH, "//div[@class='validation-summary-errors']")
EMAIL_ALREADY_EXISTS_text = "The specified email already exists"
SUCCESS_REGISTRATION_xpath = (By.XPATH, "//div[@class='result']")
SUCCESS_REGISTRATION_text = "Your registration completed"
EMAIL_IN_HEADER_xpath = (By.XPATH, "//div[@class='header-links']//a[@class='account']")
# EMAIL_IN_HEADER_xpath = (By.XPATH, "//a[@class='account' and contains(text(),'{email}')]")

IS_REQUIRED_messages = {"first_name": FIRST_NAME_IS_REQUIRED_text,
                        "last_name": LAST_NAME_IS_REQUIRED_text,
                        "email": EMAIL_IS_REQUIRED_text,
                        "password": PASSWORD_IS_REQURED_text,
                        "confirm_password": PASSWORD_IS_REQURED_text}

params_for_first_name_object = ("first_name", "", FIRST_NAME_INPUT_FIELD_xpath, FIRST_NAME_ERROR_xpath, "")
params_for_last_name_object = ("last_name", "", LAST_NAME_INPUT_FIELD_xpath, LAST_NAME_ERROR_xpath, "")
params_for_email_object = ("email", "", EMAIL_INPUT_FIELD_id, EMAIL_ERROR_xpath, "")
params_for_password_object = ("password", "", PASSWORD_INPUT_FIELD_xpath, PASSWORD_ERROR_xpath, "")
params_for_confirm_password_object = ("confirm_password", "", CONFIRM_PASSWORD_INPUT_FIELD_xpath, CONFIRM_PASSWORD_ERROR_xpath, "")
