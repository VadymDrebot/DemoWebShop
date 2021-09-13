import logging
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from constants import start_page_const

from constants.start_page_const import ProductCategoryPageConstants

from functions.common_functions import CommonFunctions


class ProductPageFunctions(CommonFunctions, ProductCategoryPageConstants):
    logger = logging.getLogger(__name__)

    def verify_correct_transition_to_page(self, product):
        # verify URL
        expected_url = self.take_attribute(locator=product.mouse_movement_locators_list[-1], attribute='href')
        # start_page_const.py.logger.info(f"ACTUAL   url: -{start_page_const.py.driver.current_url}-")
        # start_page_const.py.logger.info(f"EXPECTED url: -{expected_url}-")
        assert self.driver.current_url == expected_url

        self.verify_page_name(product)

        self.verify_breadcrumb(list_locator_of_breadcrumb_elements=self.LIST_OF_PRODUCT_BREADCRUMB_xpath,
                               list_of_expected_breadcrumb_items=["HOME"] + product.mouse_movement_names_list)

    def verify_ui_elements(self, product):
        if product.product_sub_menu_list:
            # start_page_const.py.logger.info(f" Actual  list: -{start_page_const.py.get_list_of_texts(start_page_const.py.LIST_OF_SUBCATEGORY_ON_PAGE_xpath)}-")
            # start_page_const.py.logger.info(f"Expected list: -{product.product_sub_menu_list}-")
            assert self.get_list_of_texts(self.LIST_OF_SUBCATEGORY_ON_PAGE_xpath) == product.product_sub_menu_list
        else:
            assert self.verify_presence_of_element(locator=self.DROP_DOWN_SORT_BY_LIST_xpath)
            assert self.verify_presence_of_element(locator=self.DROP_DOWN_DISPLAY_PER_PAGE_LIST_xpath)
            assert self.verify_presence_of_element(locator=self.DROP_DOWN_VIEW_AS_LIST_xpath)

    def verify_page_name(self, product):
        actual_page_name = self.get_text_from_locator(locator=self.PAGE_TITLE_class, locator_type=By.CLASS_NAME)
        expected_page_name = product.product_name
        # start_page_const.py.logger.info(f"ACTUAL   name of the page: -{actual_page_name}-")
        # start_page_const.py.logger.info(f"EXPECTED name of the page: -{expected_page_name}-")
        assert actual_page_name == expected_page_name, f"{actual_page_name}, {expected_page_name}"
