import logging
from constants import register_page_constants as reg_const


class TestRegisterPageNoClick:
    """
    Values for input fields: e- empty ,  v - valid ,  i - invalid
    Expected error messages:
        er1: 'Wrong email'
        er2: {field name} is required
        er3: "The password should have at least 6 characters."
        er4: "The password and confirmation password do not match."

    tests №   :             1   2   3   4   5   6   7   8               valid       invalid

    first_name:             e   e   v   e   v   e   v   e                any          --
    last_name :             e   v   e   v   e   v   e   v                any          --
    email     :             e   e   i   v   e   i   v   e               *@*.*      not *@*.*
    password  :             e   e   e   e   v   i   i   v              >=6 char    <6 char
    conf_passw:             e   e   v   i   v   i   v   i            ==password    !=password

    first_name_error_mes:   -   -   -   -   -   -   -   -
    last_name_error_mes :   -   -   -   -   -   -   -   -
    email_error_mes     :   -   -  er1  -   -  er1  -   -
    password_error_mes  :   -   -   -   -   -  er3 er3  -
    conf_passw_error_mes:   -   -  er4 er4  -   -  er4 er4
    """

    logger = logging.getLogger()

    def test1_empty_fields(self, register_page):
        # all empty fields
        register_page.fill_register_fields_and_verify_error_messages(register_page=register_page)

    def test2_valid_lastname(self, register_page):
        # last_name -- valid
        register_page.fill_register_fields_and_verify_error_messages(register_page=register_page,
                                                                     last_name=reg_const.VALID_LAST_NAME)

    def test3_valid_firstname_and_confirm_password_invalid_email(self, register_page):
        # # first_name -- valid , email - invalid
        register_page.fill_register_fields_and_verify_error_messages(register_page=register_page,
                                                                     first_name=reg_const.VALID_FIRST_NAME,
                                                                     email=reg_const.INVALID_EMAIL,
                                                                     confirm_password=reg_const.VALID_PASSWORD)

    def test4_valid_lastname_email_invalid_password(self, register_page):
        # last_name - valid , email - valid , confirm_password - invalid
        register_page.fill_register_fields_and_verify_error_messages(register_page=register_page,
                                                                     last_name=reg_const.VALID_LAST_NAME,
                                                                     email=reg_const.VALID_EMAIL,
                                                                     confirm_password=reg_const.INVALID_PASSWORD)

    def test5_valid_firstname_password_confirm_password(self, register_page):
        # first_name - valid , password and confirm_password -- valid
        register_page.fill_register_fields_and_verify_error_messages(register_page=register_page,
                                                                     first_name=reg_const.VALID_FIRST_NAME,
                                                                     password=reg_const.VALID_PASSWORD,
                                                                     confirm_password=reg_const.VALID_PASSWORD)

    def test6_valid_lastname_invalid_email_password_confirm_password(self, register_page):
        # last_name - valid , email - invalid , password , confirm_password -- invalid
        register_page.fill_register_fields_and_verify_error_messages(register_page=register_page,
                                                                     last_name=reg_const.VALID_LAST_NAME,
                                                                     email=reg_const.INVALID_EMAIL,
                                                                     password=reg_const.INVALID_PASSWORD,
                                                                     confirm_password=reg_const.INVALID_PASSWORD)

    def test7_valid_firstname_email_confirm_password_invalid_password(self, register_page):
        # first_name_name - valid , email - valid , password - invalid , confirm_password -- valid
        register_page.fill_register_fields_and_verify_error_messages(register_page=register_page,
                                                                     first_name=reg_const.VALID_FIRST_NAME,
                                                                     email=reg_const.VALID_EMAIL,
                                                                     password=reg_const.INVALID_PASSWORD,
                                                                     confirm_password=reg_const.VALID_PASSWORD)

    def test8_valid_lastname_password_invalid_confirm_password(self, register_page):
        # last_name - valid ,  password - valid , confirm_password -- invalid
        register_page.fill_register_fields_and_verify_error_messages(register_page=register_page,
                                                                     last_name=reg_const.VALID_LAST_NAME,
                                                                     password=reg_const.VALID_PASSWORD,
                                                                     confirm_password=reg_const.INVALID_PASSWORD)
