import logging

from constants import register_page_constants as reg_const

from functions.helpers import random_valid_email
from functions.register_functions import RegisterObject


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

    logger = logging.getLogger(__name__)

    def test1_empty_fields(self, register_page):
        # all empty fields
        user = RegisterObject()

        # 1. fill all fields with empty values
        register_page.fill_register_fields(user)

        # 2. verify no error messages
        register_page.verify_error_messages(user)
        # product_page_constants.py.logger.info(f"Expected: all fields empty")

    def test2_valid_lastname(self, register_page):
        # last_name -- valid
        user = RegisterObject(last_name=reg_const.VALID_LAST_NAME)

        # 1. fill all fields with empty values
        register_page.fill_register_fields(user)

        # 2. verify 4 error messages '... is required' appears next to empty fields
        register_page.verify_error_messages(user)

    def test3_valid_firstname_and_confirmpassword_invalid_email(self, register_page):
        # first_name -- valid , email - invalid
        user = RegisterObject(first_name=reg_const.VALID_FIRST_NAME,
                              email=reg_const.INVALID_EMAIL,
                              confirm_password=reg_const.VALID_PASSWORD)
        # 1. fill all fields with empty values
        register_page.fill_register_fields(user)

        # 2. verify 'Wrong email' and "The password and confirmation password do not match." error messages appears next to appropriate fields
        register_page.verify_error_messages(user)

    def test4_valid_lastname_email_invalid_password(self, register_page):
        # last_name - valid , email - valid , confirm_password - invalid
        user = RegisterObject(last_name=reg_const.VALID_LAST_NAME,
                              email=reg_const.VALID_EMAIL,
                              confirm_password=reg_const.INVALID_PASSWORD)
        # 1. fill all fields with empty values
        register_page.fill_register_fields(user)

        # 2. verify "The password and confirmation password do not match." error message appears next to appropriate fields
        register_page.verify_error_messages(user)

    def test5_valid_firstname_password_confirmpassword(self, register_page):
        # first_name - valid , password and confirm_password -- valid
        user = RegisterObject(first_name=reg_const.VALID_FIRST_NAME,
                              password=reg_const.VALID_PASSWORD,
                              confirm_password=reg_const.VALID_PASSWORD)
        # 1. fill all fields with empty values
        register_page.fill_register_fields(user)

        # 2. verify no error messages appears next to appropriate fields
        register_page.verify_error_messages(user)

    def test6_valid_lastname_invalid_email_password_confirmpassword(self, register_page):
        # last_name - valid , email - invalid , password , confirm_password -- invalid
        user = RegisterObject(last_name=reg_const.VALID_LAST_NAME,
                              email=reg_const.INVALID_EMAIL,
                              password=reg_const.INVALID_PASSWORD,
                              confirm_password=reg_const.INVALID_PASSWORD)
        # 1. fill all fields with empty values
        register_page.fill_register_fields(user)

        # 2. verify 'Wrong email' and  "The password should have at least 6 characters." error messages  appears next to appropriate fields
        register_page.verify_error_messages(user)

    def test7_valid_firstname_email_onfirmpassword_invalid_password(self, register_page):
        # first_name_name - valid , email - valid , password - invalid , confirm_password -- valid
        user = RegisterObject(first_name=reg_const.VALID_FIRST_NAME,
                              email=reg_const.VALID_EMAIL,
                              password=reg_const.INVALID_PASSWORD,
                              confirm_password=reg_const.VALID_PASSWORD)
        # 1. fill all fields with empty values
        register_page.fill_register_fields(user)

        # 2. verify "... at least 6 characters."  and " do not match."error messages appears next to appropriate fields
        register_page.verify_error_messages(user)

    def test8_valid_lastname_password_invalid_confirmpassword(self, register_page):
        # last_name - valid ,  password - valid , confirm_password -- invalid
        user = RegisterObject(last_name=reg_const.VALID_LAST_NAME,
                              password=reg_const.VALID_PASSWORD,
                              confirm_password=reg_const.INVALID_PASSWORD)
        # 1. fill all fields
        register_page.fill_register_fields(user)

        # 2. verify "The password and confirmation password do not match." error message appears next to appropriate fields
        register_page.verify_error_messages(user)


