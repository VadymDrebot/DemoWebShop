import pytest

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from constants import login_page_constants as login_const
from constants import header_constants as header_const
from constants import global_constants as global_const
from constants.login_page_constants import VALID_EMAIL, VALID_EMAIL2, VALID_EMAIL3

from functions.common_functions import CommonFunctions

from functions.log_in_functions import LogInFunctions
from functions.register_functions import RegisterFunctions
from functions.category_page_functions import CategoryPageFunctions
from functions.shopping_cart_functions import ShoppingCartObject


@pytest.fixture()
def start_page():
    options = Options()

    options.headless = True
    driver = webdriver.Chrome(options=options, executable_path=global_const.PATH_TO_CHROME_WEBDRIVER)
    driver.get(global_const.START_PAGE_url)
    driver.implicitly_wait(time_to_wait=10)
    yield CommonFunctions(driver)
    driver.close()


@pytest.fixture()
def login_page(start_page):
    start_page.click_button_and_verify_new_url(button=header_const.LOGIN_BUTTON_IN_HEADER_xpath,
                                               url=global_const.LOGIN_PAGE_url)
    return LogInFunctions(start_page.driver)


@pytest.fixture()
def register_page(start_page):
    start_page.click_button_and_verify_new_url(button=header_const.REGISTER_BUTTON_IN_HEADER_class,
                                               url=global_const.REGISTER_PAGE_url)
    return RegisterFunctions(start_page.driver)


@pytest.fixture()
def product_page_elements(start_page):
    return CategoryPageFunctions(start_page.driver)


@pytest.fixture(scope="class")
def get_next_valid_email():
    iterator = iter([VALID_EMAIL, VALID_EMAIL2, VALID_EMAIL3])
    return iterator


@pytest.fixture()
def email(request, login_page):
    get_email = request.node.get_closest_marker('marker_email').args[0]
    login_page.fill_login_page_fields_and_click(email_data=get_email, password_data=login_const.VALID_PASSWORD)
    return get_email


@pytest.fixture()
def cart_object(start_page):
    return ShoppingCartObject(start_page.driver)
