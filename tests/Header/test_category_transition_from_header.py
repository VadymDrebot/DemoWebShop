import logging
import pytest

from constants import global_constants as global_const
from constants.global_constants import browser_list
from constants.header_constants import categories

from functions.category_page_functions import CategoryPageFunctions, Category

from functions.helpers import create_driver


@pytest.mark.parametrize("browser_name", browser_list)
class TestCategoryTransitionFromHeader:
    """ verify correct categories and subcategories transitions  after choose and click on it in the header menu:
    check for: breadcrumbs,page name,existing of 'display/sort by/view as' tools for end-point category OR category list for subcategory"""
    logger = logging.getLogger()

    @pytest.fixture(scope="function")
    def product_page_elements(self, browser_name):
        driver = create_driver(browser_name)
        driver.implicitly_wait(time_to_wait=10)
        driver.get(global_const.START_PAGE_url)
        yield CategoryPageFunctions(driver)
        # logging.info(f"Was verified {len(list(categories.keys()))} categories in {len(browser_name)} browsers")
        driver.close()

    @pytest.mark.parametrize("category_name", list(categories.keys()))
    def test1_category_transaction_from_header(self, product_page_elements, category_name):
        category = Category(category=category_name)
        product_page_elements.move_mouse_through_list_of_locators_and_click_last(mouse_movement_locators_list=category.mouse_movement_locators_list)
        product_page_elements.verify_correct_transition_to_new_url(category)
        product_page_elements.verify_ui_elements(category)
