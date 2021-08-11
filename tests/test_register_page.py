import logging

import pytest

from constants import start_page_const
from constants.login_page_const import LogInConstants
from constants.register_page_const import RegisterConstants, RegisterObject
from constants.start_page_const import REGISTER_BUTTON_IN_HEADER_xpath
from functions import helpers

# from functions.common_functions import GeneratedConstants
from functions.common_functions import CommonFunctions
from functions.helpers import CHROME, FIREFOX, create_driver
from functions.register_functions import RegisterFunctions


# @pytest.mark.parametrize("browser_name", [FIREFOX, CHROME])
# class TestRegisterPageNoClick:
#     """
#     e- empty , v - valid , i - invalid              valid        invalid
#
#     tests №   :  1  2  3  4  5  6  7  8
#     first_name:  e  e  v  e  v  e  v  e                any         --
#     last_name :  e  v  e  v  e  v  e  v                any         --
#     email     :  e  e  i  v  e  i  v  e               *@*.*      not *@*.*
#     password  :  e  e  e  e  v  i  i  v              >=6 char    <6 char
#     conf_passw:  e  e  v  i  v  i  v  i            ==password    !=password
#
#     Tests 1-8 without click 'Register' button. Tests 8- with click 'Register' button
#     1. all empty fields. Expected result: no error message
#     2. last_name -- valid, rest fields --  empty. Expected result: no error message
#     3. 'first name', 'confirm_password' -- valid, 'email'  -- invalid, rest - empty, Expected result:error messages: 'Wrong email' and '"The password and confirmation password do not match."
#     4. 'last name', 'email' -- valid,'confirm password' - invalid, rest -- empty. Expected result:"The password and confirmation password do not match."
#     5. 'password==confirm password' <5 characters , without click 'Register' button
#     6. 'password==confirm password' <5 characters , with click 'Register' button
#     7. 'password' != 'confirm password' , without click 'Register' button
#     8. all fields are valid
#     """
#
#     @pytest.fixture()
#     def start_page(self, browser_name):
#         driver = create_driver(browser_name)
#         driver.get(start_page_const.START_PAGE_url)
#         driver.implicitly_wait(time_to_wait=10)
#         yield CommonFunctions(driver)
#         driver.close()
#
#     @pytest.fixture()
#     def register_page(self, start_page):
#         start_page.wait_click_ability_and_click(REGISTER_BUTTON_IN_HEADER_xpath)
#         return RegisterFunctions(start_page.driver)
#
#     logger = logging.getLogger(__name__)
#
#     def test1(self, register_page):
#         # all empty fields
#         user = RegisterObject()
#
#         # 1. fill all fields with empty values
#         register_page.fill_register_fields(user)
#
#         # 2. verify no error messages
#         register_page.verify_error_messages(user)
#         # self.logger.info(f"Expected: all fields empty")
#
#     def test2(self, register_page):
#         # last_name -- valid
#         user = RegisterObject(last_name=register_page.random_word(5))
#
#         # 1. fill all fields with empty values
#         register_page.fill_register_fields(user)
#
#         # 2. verify 4 error messages '... is required' appears next to empty fields
#         register_page.verify_error_messages(user)
#
#     def test3(self, register_page):
#         # first_name -- valid , email - invalid
#         user = RegisterObject(first_name=register_page.random_word(3),
#                               email=register_page.random_word(3),
#                               confirm_password=register_page.random_word(7))
#         # 1. fill all fields with empty values
#         register_page.fill_register_fields(user)
#
#         # 2. verify 5 error messages '... is required' appears next to appropriate fields
#         register_page.verify_error_messages(user)
#
#     def test4(self, register_page):
#         # last_name - valid , email - valid , confirm_password - invalid
#         user = RegisterObject(last_name=register_page.random_word(3),
#                               email=LogInConstants.VALID_EMAIL,
#                               confirm_password=register_page.random_word(4))
#         # 1. fill all fields with empty values
#         register_page.fill_register_fields(user)
#
#         # 2. verify 5 error messages '... is required' appears next to appropriate fields
#         register_page.verify_error_messages(user)
#
#     def test5(self, register_page):
#         # first_name - valid , password and confirm_password -- valid
#         passw = register_page.random_word(7)
#         user = RegisterObject(first_name=register_page.random_word(5),
#                               password=passw,
#                               confirm_password=passw)
#         # 1. fill all fields with empty values
#         register_page.fill_register_fields(user)
#
#         # 2. verify 5 error messages '... is required' appears next to appropriate fields
#         register_page.verify_error_messages(user)
#
#     def test6(self, register_page):
#         # last_name - valid , password - valid ,  confirm_password -- invalid
#         passw = register_page.random_word(3)
#         user = RegisterObject(last_name=register_page.random_word(5),
#                               email=register_page.random_word(5),
#                               password=passw,
#                               confirm_password=passw)
#         # 1. fill all fields with empty values
#         register_page.fill_register_fields(user)
#
#         # 2. verify 5 error messages '... is required' appears next to appropriate fields
#         register_page.verify_error_messages(user)
#
#     def test7(self, register_page):
#         # first_name_name - valid , email - valid , password - invalid , confirm_password -- invalid
#         user = RegisterObject(first_name=register_page.random_word(3),
#                               email=LogInConstants.VALID_EMAIL,
#                               password=register_page.random_word(3),
#                               confirm_password=register_page.random_word(7))
#         # 1. fill all fields with empty values
#         register_page.fill_register_fields(user)
#
#         # 2. verify 5 error messages '... is required' appears next to appropriate fields
#         register_page.verify_error_messages(user)
#
#     def test8(self, register_page):
#         # first_name_name - valid , email - valid , password - invalid , confirm_password -- invalid
#         user = RegisterObject(first_name=register_page.random_word(3),
#                               email=LogInConstants.VALID_EMAIL,
#                               password=register_page.random_word(7),
#                               confirm_password=register_page.random_word(3))
#         # 1. fill all fields
#         register_page.fill_register_fields(user)
#
#         # 2. verify 5 error messages '... is required' appears next to appropriate fields
#         register_page.verify_error_messages(user)


@pytest.mark.parametrize("browser_name", [FIREFOX, CHROME])
class TestRegisterPageClick():
    logger = logging.getLogger(__name__)

    """
    e- empty , v - valid , i - invalid                      valid        invalid

    tests №   :  9  10  11  12  13  14  15  16
    first_name:  e  e   v   e   v   e   v   e                any         --
    last_name :  e  v   e   v   e   v   e   v                any         --
    email     :  e  e   i   v   e   i   v   e               *@*.*      not *@*.*
    password  :  e  e   e   e   v   i   i   v              >=6 char    <6 char
    conf_passw:  e  e   v   i   v   i   v   i            ==password    !=password
    """

    @pytest.fixture()
    def start_page(self, browser_name):
        driver = create_driver(browser_name)
        driver.get(start_page_const.START_PAGE_url)
        driver.implicitly_wait(time_to_wait=10)
        yield CommonFunctions(driver)
        driver.close()

    @pytest.fixture()
    def register_page(self,start_page):
        start_page.wait_click_ability_and_click(REGISTER_BUTTON_IN_HEADER_xpath)
        return RegisterFunctions(start_page.driver)

    def test9(self, register_page):
        """
        Summary: registering user with all empty fields
        Steps:  1. fill all fields with empty values
                2. click 'Register' button
                3. verify error messages
        Expected result: all error messages == ' ... is required'  """
        # create 'user' object with empty values
        user = RegisterObject()
        # 1. fill all fields
        register_page.fill_register_fields(user)
        # 2. click 'Register' button
        register_page.click_register_button(user)
        # 3. verify error messages
        register_page.verify_error_messages(user)

    def test10(self, register_page):
        """
        Summary: registering user with valid last_name , rest fields are empty
        Steps:  1. fill all fields
                2. click 'Register' button
                3. verify error messages
        Expected result: last_name error message - empty , rest error message fields -- ' ... is required'  """
        # create 'user' object with last_name -- valid
        user = RegisterObject(last_name=register_page.VALID_LAST_NAME)
        # 1. fill all fields
        register_page.fill_register_fields(user)
        # 2. click 'Register' button
        register_page.click_register_button(user)
        # 3. verify 4 error messages
        register_page.verify_error_messages(user)

    def test11(self, register_page):
        # 1. first_name -- valid , email - invalid , confirm_password - valid
        user = RegisterObject(first_name=register_page.VALID_FIRST_NAME,
                              email=register_page.INVALID_EMAIL,
                              confirm_password=register_page.VALID_PASSWORD)
        # 2. fill all fields with empty values
        register_page.fill_register_fields(user)

        # 3. click 'Register' button
        register_page.click_register_button(user)

        # 4. verify error messages: 'last_name',password - '... is required', 'email' - 'Wrong email', 'confirm_password' - ' ...do not match.'
        register_page.verify_error_messages(user)

    def test12(self, register_page):
        # 1. last_name - valid , email - valid , confirm_password - invalid
        user = RegisterObject(last_name=register_page.VALID_LAST_NAME,
                              email=LogInConstants.VALID_EMAIL,
                              confirm_password=register_page.INVALID_PASSWORD)
        # 2. fill all fields with empty values
        register_page.fill_register_fields(user)

        # 3. click 'Register' button
        register_page.click_register_button(user)

        # 4. verify error messages: 'first_name', 'password' - '... is required' , 'confirm_password' - ' ...do not match.'
        register_page.verify_error_messages(user)

    def test13(self, register_page):
        # 1. first_name - valid , password and confirm_password -- valid
        user = RegisterObject(first_name=register_page.VALID_FIRST_NAME,
                              password=register_page.VALID_PASSWORD,
                              confirm_password=register_page.VALID_PASSWORD)

        # 2. fill all fields with empty values
        register_page.fill_register_fields(user)

        # 3. click 'Register' button
        register_page.click_register_button(user)

        # 4. verify error messages 'last_name','email' - '... is required'
        register_page.verify_error_messages(user)

    def test14(self, register_page):
        # 1. last_name - valid , email - invalid , password and confirm_password -- invalid
        user = RegisterObject(last_name=register_page.VALID_LAST_NAME,
                              email=register_page.INVALID_EMAIL,
                              password=register_page.INVALID_PASSWORD,
                              confirm_password=register_page.INVALID_PASSWORD)
        # 2. fill all fields with empty values
        register_page.fill_register_fields(user)

        # 3. click 'Register' button
        register_page.click_register_button(user)

        # 2. verify error messages: 'first_name' - '... is required' , 'email' - 'Wrong email' , 'password' - '...at least 6 characters.'
        register_page.verify_error_messages(user)

    def test15(self, register_page):
        # 1. first_name_name - valid , email - valid , password - invalid , confirm_password -- valid
        user = RegisterObject(first_name=register_page.VALID_FIRST_NAME,
                              email=LogInConstants.VALID_EMAIL,
                              password=register_page.INVALID_PASSWORD,
                              confirm_password=register_page.VALID_PASSWORD)
        # 2. fill all fields with empty values
        register_page.fill_register_fields(user)

        # 3. click 'Register' button
        register_page.click_register_button(user)

        # 4. verify error messages: 'last_name' - '... is required' , 'password' - '...at least 6 characters.' , 'confirm_password' - ' ...do not match.'
        register_page.verify_error_messages(user)

    def test16(self, register_page):
        # 1. first_name_name - valid , email - valid , password - valid , confirm_password -- invalid
        user = RegisterObject(first_name=register_page.VALID_FIRST_NAME,
                              email=LogInConstants.VALID_EMAIL,
                              password=register_page.VALID_PASSWORD,
                              confirm_password=register_page.INVALID_PASSWORD)
        # 1. fill all fields
        register_page.fill_register_fields(user)

        # 3. click 'Register' button
        register_page.click_register_button(user)

        # 2. verify error messages 'last_name' -'... is required' ,  'confirm_password' - ' ...do not match.
        register_page.verify_error_messages(user)
