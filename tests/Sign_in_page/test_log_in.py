import logging

import pytest
from constants import register_page_constants as reg_const

from constants import sign_in_page_constants as sign_const


class TestLogIn:
    """ Tests for Log In page"""
    # logger = logging.getLogger(__name__)

    @pytest.mark.parametrize("email", [sign_const.VALID_EMAIL, sign_const.EXISTING_EMAIL, sign_const.INVALID_EMAIL, ""])
    @pytest.mark.parametrize("password", [sign_const.VALID_PASSWORD, sign_const.EXISTING_PASSWORD, ""])
    def test1_fill_email_password_without_click_login_button(self, login_page, email, password):
        """ Summary: login with empty 'email' field
            Preconditions: get in "Log in" page
            Steps:
                   1. fill 'email' field
                   2. fill 'password' field
                   3. verify  error messages
        """
        login_page.fill_login_page_fields(email_data=email, password_data=password)
        login_page.verify_login_error_messages_no_click(email)

    @pytest.mark.parametrize("email", [reg_const.VALID_EMAIL, reg_const.EXISTING_EMAIL, sign_const.INVALID_EMAIL, ""])
    @pytest.mark.parametrize("password", [reg_const.VALID_PASSWORD, sign_const.EXISTING_PASSWORD, ""])
    def test2_fill_email_password_with_click_login_button(self, login_page, email, password):
        """ Summary: login with empty 'email' field
            Preconditions: get in "Log in" page
               Steps:
                    1. fill 'email' field
                    2. fill 'password' field
                    3. click 'log in' button in 'log in' page
                    4. verify error messages
        """
        login_page.fill_login_page_fields(email_data=email, password_data=password)
        login_page.verify_login_error_messages_no_click(email, password)

        login_page.wait_click_ability_and_click(sign_const.LOGIN_BUTTON_IN_LOGIN_PAGE_xpath)
        login_page.verify_login_error_messages_after_click(email, password)
