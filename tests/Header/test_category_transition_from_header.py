import logging
import pytest

from constants import global_constants as global_const
from constants.global_constants import browser_list

from functions.category_page_functions import CategoryPageFunctions

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
        driver.close()

    def test1_books(self, product_page_elements):
        """ verify transaction to the "Books" page """
        product_page_elements.move_mouse_click_and_verify_category_page(product_page_elements, category_name="Books")

    def test2_computer(self, product_page_elements):
        """ verify transaction to the "Computers" page """
        product_page_elements.move_mouse_click_and_verify_category_page(product_page_elements, category_name="Computers")

    def test3_desktops(self, product_page_elements):
        """ verify transaction to the "Desktops" page """
        product_page_elements.move_mouse_click_and_verify_category_page(product_page_elements, category_name="Desktops")

    def test8(self, product_page_elements):
        """ verify transaction to the "Cell phones" page """
        product_page_elements.move_mouse_click_and_verify_category_page(product_page_elements, category_name="Cell phones")

    def test11(self, product_page_elements):
        """ verify transaction to the "Jewelry" page """
        product_page_elements.move_mouse_click_and_verify_category_page(product_page_elements, category_name="Jewelry")

    def test13(self, product_page_elements):
        """ Negative test:  verify transaction to the unexisting category: "Shoes" page """
        product_page_elements.move_mouse_click_and_verify_category_page(product_page_elements, category_name="Shoes")
