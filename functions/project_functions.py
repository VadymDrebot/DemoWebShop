from random import choice
from selenium.webdriver.common.by import By

from constants.header_constants import product_dict
from constants import header_constants as header_const
from constants.product_page_constants import PAGE_TITLE_class
from constants.shopping_cart_constants import PAGE_TITLE_SHOPPING_CART_text, SHOPPING_CART_EMPTY_CONTENT_class, SHOPPING_CART_EMPTY_CONTENT_text
from functions.common_functions import CommonFunctions


class ProjectFunction(CommonFunctions):
    """ functions which used throughout the project (cart_object page , shopping cart, ..."""

    def get_list_of_dom_indexes(self, products_list_locator, condition_list_locator="", locator_type=By.XPATH):
        """
        products_list_locator -- list of ITEMS on a page(shopping cart,products page, etc...)
        condition_list_locator -- list of existing parameters of each item (like: 'add to cart' button, price, ....)
        return: [] -- list of DOM indexes
        """
        product_amount_on_page = len(self.driver.find_elements(by=locator_type, value=products_list_locator))  # f.e. len=5

        if condition_list_locator:
            list_of_dom_indexes = [index for index in range(1, product_amount_on_page + 1) if self.verify_presence_of_element(
                locator=condition_list_locator.format(index=index))]
        else:
            list_of_dom_indexes = [index for index in range(1, product_amount_on_page + 1)]  # lst= [1,2,3,4,5]

        return list_of_dom_indexes

    def verify_breadcrumb(self, list_locator_of_breadcrumb_elements, list_of_expected_breadcrumb_items):
        """ 'actual_list_of_breadcrumb_elements' concatenation of texts of elements of breadcrumb FROM DOM
        'expected_breadcrumb' is taken from manually given 'names'  """
        actual_list_of_breadcrumb_texts = self.get_list_of_texts(list_locator=list_locator_of_breadcrumb_elements)
        actual_breadcrumb = "".join(actual_list_of_breadcrumb_texts).upper()

        expected_breadcrumb = " /".join(list_of_expected_breadcrumb_items).upper()

        self.logger.info(f"ACTUAL   breadcrumb: -{actual_breadcrumb}-")
        self.logger.info(f"EXPECTED breadcrumb: -{expected_breadcrumb}-")
        assert actual_breadcrumb == expected_breadcrumb

    def open_random_product_category_page_and_get_url(self):
        """ open random END POINT category page (with list of PRODUCTS , not with SUBCATEGORIES)
        return: URL, open category page"""
        mouse_movement_locators_list = []
        while not mouse_movement_locators_list:
            item = choice(list(product_dict.values()))
            if "sub_menu" not in item:
                mouse_movement_names_list = item["mouse_movement"]  # f.e.: ["Computers", "Desktops"]
                mouse_movement_locators_list = [product_dict[name]["xpath"] for name in mouse_movement_names_list]
        self.move_mouse_through_list_of_locators_and_click_last(movement_list_locator=mouse_movement_locators_list)
        return self.driver.current_url

    def verify_empty_shopping_cart(self):
        self.verify_message(locator=PAGE_TITLE_class, locator_type=By.CLASS_NAME,
                            expected_text=PAGE_TITLE_SHOPPING_CART_text)
        self.verify_message(locator=SHOPPING_CART_EMPTY_CONTENT_class, locator_type=By.CLASS_NAME,
                            expected_text=SHOPPING_CART_EMPTY_CONTENT_text)
