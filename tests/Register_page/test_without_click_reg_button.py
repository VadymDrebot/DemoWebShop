import logging
import pytest

from constants import register_page_constants as reg_const


class TestRegisterPageNoClick:
    """
    Valid values for
        first_name -- not empty
        last_name -- not empty
        email -- * @ * . *
        password -- 6 or more characters
        confirm_password -- equal to password
    """

    logger = logging.getLogger()

    @pytest.mark.parametrize("first_name", [reg_const.VALID_FIRST_NAME, ""])
    @pytest.mark.parametrize("last_name", [reg_const.VALID_LAST_NAME, ""])
    @pytest.mark.parametrize("email", [reg_const.INVALID_EMAIL, reg_const.EXISTING_EMAIL, ""])  # reg_const.VALID_EMAIL,
    @pytest.mark.parametrize("password", [reg_const.VALID_PASSWORD, reg_const.INVALID_PASSWORD, ""])
    @pytest.mark.parametrize("confirm_password", [reg_const.VALID_CONFIRM_PASSWORD, reg_const.INVALID_CONFIRM_PASSWORD, ""])
    def test1_fill_input_fields_without_click_register_button(self, register_page_obj, first_name, last_name, email, password, confirm_password):
        logging.info(f"Input data: \n{first_name=},  {last_name=},  {email=},  {password=},  {confirm_password=}\n")

        register_page_obj.fill_register_fields_with_tab_click(first_name_value=first_name,
                                                              last_name_value=last_name,
                                                              email_value=email,
                                                              password_value=password,
                                                              confirm_password_value=confirm_password)
        register_page_obj.verify_error_messages()
