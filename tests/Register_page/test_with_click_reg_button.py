import logging

from constants import register_page_constants as reg_const

from functions.register_functions import RegisterObject


class TestRegisterPageClick:
    logger = logging.getLogger()

    """
    Values for input fields: e- empty ,  v - valid ,  i - invalid  , ex - already exists  , rv - random valid
    Error messages:
        1. 'Wrong email'
        2. {field name} is required
        3. "The password should have at least 6 characters."
        4. "The password and confirmation password do not match."
        5. "The specified email already exists"
        6. "Your registration completed
"

    tests №   :             9  10  11  12  13  14  15  16  17  18          valid        invalid

    first_name          :   e   e   v   e   v   e   v   e   v   v           any           --
    last_name           :   e   v   e   v   e   v   e   v   v   v           any           --
    email               :   e   e   i   v   e   i   v   e  ex  rv          *@*.*       not *@*.*
    password            :   e   e   e   e   v   i   i   v   v   v         >=6 char      <6 char
    conf_passw          :   e   e   v   i   v   i   v   i   v   v        ==password    !=password

    first_name_error_mes:   2   2   -   2   -   2   -   2   -   -
    last_name_error_mes :   2   -   2   -   2   -   2   -   -   -
    email_error_mes     :   2   2   1   -   2   1   -   2   -   -
    password_error_mes  :   2   2   2   2   -   3   3   -   -   -
    conf_passw_error_mes:   2   2   4   4   -   -   4   4   -   -
    email_already_exists:   -   -   -   -   -   -   -   -   5   -
    registration_complet:   -   -   -   -   -   -   -   -   -   6
    """

    def test9_empty_fields(self, register_page):
        """
        Summary: registering user with all empty fields
        Steps:  1. fill all fields with empty values
                2. click 'Register' button
                3. verify error messages
        Expected result: all error messages == ' ... is required'  """

        register_page.fill_register_fields_click_and_verify_error_messages(register_page=register_page)

    def test10_valid_lastname(self, register_page, first_name="", last_name="", email="", password="", confirm_password=""):
        """
        Summary: registering user with valid last_name , rest fields are empty
        Steps:  1. fill all fields
                2. click 'Register' button
                3. verify error messages
        Expected result: last_name error message - empty , rest error message fields -- ' ... is required'  """
        register_page.fill_register_fields_click_and_verify_error_messages(register_page=register_page,
                                                                           last_name=reg_const.VALID_LAST_NAME)

    def test11_valid_firstname_password_invalid_email(self, register_page):
        """
        Summary: registering user with valid first_name and password, invalid email, rest fields are empty
        Steps:  1. fill all fields
                2. click 'Register' button
                3. verify error messages
        Expected result: last_name error message - empty , rest error message fields -- ' ... is required'  """
        register_page.fill_register_fields_click_and_verify_error_messages(register_page=register_page,
                                                                           first_name=reg_const.VALID_FIRST_NAME,
                                                                           email=reg_const.INVALID_EMAIL,
                                                                           confirm_password=reg_const.VALID_PASSWORD)

    def test12_valid_lastname_email_invalid_confirm_password(self, register_page):
        """
        Summary: registering user with valid last_name and email, invalid confirm_password, rest fields are empty
        Steps:  1. fill all fields
                2. click 'Register' button
                3. verify error messages
        Expected result: last_name error message - empty , rest error message fields -- ' ... is required'  """

        register_page.fill_register_fields_click_and_verify_error_messages(register_page=register_page,
                                                                           last_name=reg_const.VALID_LAST_NAME,
                                                                           email=reg_const.VALID_EMAIL,
                                                                           confirm_password=reg_const.INVALID_PASSWORD)

    def test13_valid_firstname_password_confirm_password(self, register_page):
        """
        Summary: registering user with valid first_name and password and confirm_password, rest fields are empty
        Steps:  1. fill all fields
                2. click 'Register' button
                3. verify error messages
       Expected result: last_name error message - empty , rest error message fields -- ' ... is required'  """

        register_page.fill_register_fields_click_and_verify_error_messages(register_page=register_page,
                                                                           first_name=reg_const.VALID_FIRST_NAME,
                                                                           password=reg_const.VALID_PASSWORD,
                                                                           confirm_password=reg_const.VALID_PASSWORD)

    def test14_valid_lastname_invalid_email_password_confirm_password(self, register_page):
        """
        Summary: registering user with valid last_name , invalid email and password and confirm_password, rest fields are empty
        Steps:  1. fill all fields
                2. click 'Register' button
                3. verify error messages
        Expected result: last_name error message - empty , rest error message fields -- ' ... is required'  """
        register_page.fill_register_fields_click_and_verify_error_messages(register_page=register_page,
                                                                           last_name=reg_const.VALID_LAST_NAME,
                                                                           email=reg_const.INVALID_EMAIL,
                                                                           password=reg_const.INVALID_PASSWORD,
                                                                           confirm_password=reg_const.INVALID_PASSWORD)

    def test15_valid_first_name_email_confirm_password_invalid_password(self, register_page):
        # 1. first_name_name - valid , email - valid , password - invalid , confirm_password -- valid
        register_page.fill_register_fields_click_and_verify_error_messages(register_page=register_page,
                                                                           first_name=reg_const.VALID_FIRST_NAME,
                                                                           email=reg_const.VALID_EMAIL,
                                                                           password=reg_const.INVALID_PASSWORD,
                                                                           confirm_password=reg_const.VALID_PASSWORD)

    def test16_valid_first_name_email_password_invalid_confirm_password(self, register_page):
        # 1. first_name_name - valid , email - valid , password - valid , confirm_password -- invalid
        register_page.fill_register_fields_click_and_verify_error_messages(register_page=register_page,
                                                                           first_name=reg_const.VALID_FIRST_NAME,
                                                                           email=reg_const.VALID_EMAIL,
                                                                           password=reg_const.VALID_PASSWORD,
                                                                           confirm_password=reg_const.INVALID_PASSWORD)

    def test17_valid_first_name_last_name_password_confirm_password_existing_email(self, register_page):
        # 1. first_name,last_name  - valid , email - existing , password - valid , confirm_password -- valid
        register_page.fill_register_fields_click_and_verify_error_messages(register_page=register_page,
                                                                           first_name=reg_const.VALID_FIRST_NAME,
                                                                           last_name=reg_const.VALID_LAST_NAME,
                                                                           email=reg_const.EXISTING_EMAIL,
                                                                           password=reg_const.VALID_PASSWORD,
                                                                           confirm_password=reg_const.VALID_PASSWORD)

    def test18_valid_all_fields(self, register_page):
        # first_name,last_name  - valid , email - valid , password - valid , confirm_password -- valid
        email = reg_const.VALID_EMAIL
        user = RegisterObject(first_name=reg_const.VALID_FIRST_NAME,
                              last_name=reg_const.VALID_LAST_NAME,
                              email=email,
                              password=reg_const.VALID_PASSWORD,
                              confirm_password=reg_const.VALID_PASSWORD)

        # 1. fill all fields
        register_page.fill_register_fields(user)

        # 2. verify error messages
        register_page.verify_error_messages(user)

        # 3. click 'Register' button
        register_page.click_register_button(user)

        # 4. verify  message "Your registration completed"
        register_page.verify_message(locator=reg_const.SUCCESS_REGISTRATION_xpath,
                                     expected_text=reg_const.SUCCESS_REGISTRATION_text)
        self.logger.info(f"Observe message:  --{register_page.get_text_from_locator(reg_const.SUCCESS_REGISTRATION_xpath)}--")

        # 4. verify just inputed email in header
        register_page.verify_message(locator=reg_const.EMAIL_IN_HEADER_xpath, expected_text=email)
        self.logger.info(
            f"Observe username in header:  --{register_page.get_text_from_locator(reg_const.EMAIL_IN_HEADER_xpath)}--")
