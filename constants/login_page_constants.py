from selenium.webdriver.common.by import By

from functions.helpers import random_word

VALID_EMAIL = "vadim1@yahoo.com"
VALID_PASSWORD = "drevad"

INVALID_EMAIL = random_word()
INVALID_PASSWORD = "invalid" + random_word()

USER_NAME_IN_HEADER_xpath = (By.XPATH,"//div[@class='header-links']//a[@class='account']")

EMAIL_INPUT_FIELD_xpath = (By.XPATH, "//form/div/input[@id='Email']")
PASSWORD_INPUT_FIELD_xpath = (By.XPATH, "//form/div/input[@id='Password']")
LOGIN_BUTTON_IN_LOGIN_PAGE_xpath = (By.XPATH, "//form/div/input[@class='button-1 login-button']")

EMAIL_VALIDATION_ERROR_xpath = (By.XPATH, "//span[@class='field-validation-error']")
EMAIL_VALIDATION_ERROR_MESSAGE_text = "Please enter a valid email address."

LOGIN_ERROR_MESSAGE_xpath = (By.XPATH, "//div[@class='validation-summary-errors']")
LOGIN_ERROR_MESSAGE_text = "Login was unsuccessful. Please correct the errors and try again."
