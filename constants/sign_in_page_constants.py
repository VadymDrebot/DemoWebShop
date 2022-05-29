from selenium.webdriver.common.by import By

from functions import helpers
from functions.helpers import  email_iterator

VALID_EMAIL = helpers.random_valid_email()
INVALID_EMAIL = helpers.random_invalid_email()
EXISTING_EMAIL = "vadim1@yahoo.com"

VALID_PASSWORD = helpers.random_valid_password()
EXISTING_PASSWORD = "drevad"
EMAIL_ITERATOR = email_iterator()

USER_NAME_IN_HEADER_xpath = (By.XPATH, "//div[@class='header-links']//a[@class='account']")

EMAIL_INPUT_FIELD_xpath = (By.XPATH, "//form/div/input[@id='Email']")
PASSWORD_INPUT_FIELD_xpath = (By.XPATH, "//form/div/input[@id='Password']")
LOGIN_BUTTON_IN_LOGIN_PAGE_xpath = (By.XPATH, "//form/div/input[@class='button-1 login-button']")

EMAIL_VALIDATION_ERROR_xpath = (By.XPATH, "//span[@class='field-validation-error']")
EMAIL_VALIDATION_ERROR_text = "Please enter a valid email address."

LOGIN_ERROR_MESSAGE_xpath = (By.XPATH, "//div[@class='validation-summary-errors']/span")
LOGIN_ERROR_MESSAGE_text = "Login was unsuccessful. Please correct the errors and try again."

CREDENTIAL_ERROR_MESSAGE_xpath = (By.XPATH, "//div[@class='message-error']//li")
CREDENTIAL_ERROR_NO_CUSTOMER__text = "No customer account found"
CREDENTIAL_ERROR_EXISTING_EMAIL_text = "The credentials provided are incorrect"

