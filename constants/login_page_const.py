class LogInConstants:
    VALID_EMAIL = "vadim1@yahoo.com"
    VALID_PASSWORD = "drevad"
    USER_NAME_IN_HEADER_xpath = "//div[@class='header-links']//a[@class='account']"

    EMAIL_INPUT_FIELD_xpath = "//form/div/input[@id='Email']"
    PASSWORD_INPUT_FIELD_xpath = "//form/div/input[@id='Password']"
    LOGIN_BUTTON_IN_LOGIN_PAGE_xpath = "//form/div/input[@class='button-1 login-button']"

    EMAIL_VALIDATION_ERROR_xpath = "//span[@class='field-validation-error']"
    EMAIL_VALIDATION_ERROR_MESSAGE_text = "Please enter a valid email address."

    LOGIN_ERROR_MESSAGE_xpath = "//div[@class='validation-summary-errors']"
    LOGIN_ERROR_MESSAGE_text = "Login was unsuccessful. Please correct the errors and try again."
