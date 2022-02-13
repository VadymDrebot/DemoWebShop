import logging
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from constants import product_page_constants
from constants.header_constants import product_dict
from constants import product_page_constants as prod_page_const

from functions.common_functions import CommonFunctions
from functions.project_functions import ProjectFunction


class Product:
    def __init__(self, product_name):
        self.__product_name = ""
        self.product_name = product_name

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, product_name):  # product_name == "Desktops"
        self.__product_name = product_name
        for item in product_dict.keys():
            if item == product_name:  # checking_product_item = "Desktops"
                self.mouse_movement_names_list = product_dict[item]["mouse_movement"]  # == ["Computers", "Desktops"],
                self.product_sub_menu_list = product_dict[item].get("sub_menu")  # == ["Desktops", "Notebooks", "Accessories"]
                self.mouse_movement_locators_list = [product_dict[name]["xpath"] for name in product_dict[product_name]["mouse_movement"]]
                break
        else:
            # self.logger.info( "There is no such element -{product_name}-")
            self.mouse_movement_names_list = []


class ProductPageFunctions(ProjectFunction):
    logger = logging.getLogger(__name__)

    def verify_correct_transition_to_page(self, product):
        # verify URL
        expected_url = self.take_attribute(locator=product.mouse_movement_locators_list[-1], attribute='href')
        self.logger.info(f"ACTUAL   url: -{self.driver.current_url}-")
        self.logger.info(f"EXPECTED url: -{expected_url}-")
        assert self.driver.current_url == expected_url

        self.verify_page_name(product)

        self.verify_breadcrumb(list_locator_of_breadcrumb_elements=prod_page_const.LIST_OF_PRODUCT_BREADCRUMB_xpath,
                               list_of_expected_breadcrumb_items=["HOME"] + product.mouse_movement_names_list)

    def verify_ui_elements(self, product):
        if product.product_sub_menu_list:
            # self.logger.info(f" Actual  list: -{product_page_constants.py.get_list_of_texts(product_page_constants.py.LIST_OF_SUBCATEGORY_ON_PAGE_xpath)}-")
            # self.logger.info(f"Expected list: -{cart_object.product_sub_menu_list}-")
            assert self.get_list_of_texts(prod_page_const.LIST_OF_SUBCATEGORY_ON_PAGE_xpath) == product.product_sub_menu_list
        else:
            assert self.verify_presence_of_element(locator=prod_page_const.DROP_DOWN_SORT_BY_LIST_xpath)
            assert self.verify_presence_of_element(locator=prod_page_const.DROP_DOWN_DISPLAY_PER_PAGE_LIST_xpath)
            assert self.verify_presence_of_element(locator=prod_page_const.DROP_DOWN_VIEW_AS_LIST_xpath)

    def verify_page_name(self, product):
        actual_page_name = self.get_text_from_locator(locator=prod_page_const.PAGE_TITLE_class, locator_type=By.CLASS_NAME)
        expected_page_name = product.product_name
        self.logger.info(f"ACTUAL   name of the page: -{actual_page_name}-")
        self.logger.info(f"EXPECTED name of the page: -{expected_page_name}-")
        assert actual_page_name == expected_page_name, f"{actual_page_name}, {expected_page_name}"
