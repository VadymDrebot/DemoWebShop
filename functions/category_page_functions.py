import logging

from selenium.common.exceptions import TimeoutException

from constants.header_constants import categories
from constants import product_page_constants as prod_page_const

from functions.project_functions import ProjectFunction


class Category:
    """ instance -- name/item of the category(in header) """

    def __init__(self, category):
        self.mouse_movement_categories_list = []
        self.__category_name = ""
        self.category_name = category

    @property
    def category_name(self):
        return self.__category_name

    @category_name.setter
    def category_name(self, category):  # product_name => "Desktops"
        self.__category_name = category
        for item in categories.keys():
            if item == category:  # checked_product item => "Desktops"
                self.mouse_movement_categories_list = categories[category]["mouse_movement"]  # => ["Computers", "Desktops"],
                self.sub_menu_list = categories[category].get("sub_menu")  # => ""
                self.mouse_movement_locators_list = [categories[item]["xpath_for_click"] for item in categories[category]["mouse_movement"]]
                return


class CategoryPageFunctions(ProjectFunction):
    """ throughout category pages"""
    logger = logging.getLogger()

    def verify_correct_transition_to_new_url(self, category):
        expected_url = self.take_attribute(locator=category.mouse_movement_locators_list[-1], attribute='href')
        # self.logger.info(f"ACTUAL   url: --{self.driver.current_url}--")
        # self.logger.info(f"EXPECTED url: --{expected_url}--")
        assert self.driver.current_url == expected_url

    def verify_ui_elements(self, category):
        self.verify_page_name(category)
        self.verify_breadcrumb(category)

        if category.sub_menu_list:
            self.logger.info(f" ACTUAL  submenu list: -{self.get_list_of_texts(prod_page_const.LIST_OF_SUBCATEGORY_ON_PAGE_xpath)}-")
            self.logger.info(f"EXPECTED submenu list: -{category.sub_menu_list}-")
            assert self.get_list_of_texts(prod_page_const.LIST_OF_SUBCATEGORY_ON_PAGE_xpath) == category.sub_menu_list
        else:
            assert self.check_presence_of_element(locator=prod_page_const.DROP_DOWN_SORT_BY_LIST_BLOCK_xpath)
            assert self.check_presence_of_element(locator=prod_page_const.DROP_DOWN_DISPLAY_PER_PAGE_BLOCK_xpath)
            assert self.check_presence_of_element(locator=prod_page_const.DROP_DOWN_VIEW_AS_BLOCK_xpath)

    def verify_page_name(self, category):
        actual_page_name = self.get_text_from_locator(locator=prod_page_const.PAGE_TITLE_xpath)
        expected_page_name = category.category_name
        # self.logger.info(f"ACTUAL   name of the page: --{actual_page_name}--")
        # self.logger.info(f"EXPECTED name of the page: --{expected_page_name}--")
        assert actual_page_name == expected_page_name, f"{actual_page_name}, {expected_page_name}"

    def verify_elements_to_be_sorted_from_whole_dropdown_menu(self, locator):
        """ verify if page elements are sorted for EACH value from drop down menu"""
        for name in self.get_list_of_drop_down_values(locator):
            self.click_concrete_value_from_drop_down_list(value=name, locator=locator)
            self.verify_elements_to_be_sorted_by_single_value(name)

    def verify_elements_to_be_sorted_by_single_value(self, text):
        """ verify if page elements are sorted as ONE GIVEN (as text) value from drop down menu"""

        if text == "Position":
            sorted_list = "Was chosen 'Position'. Sorting passed..."
            assert True

        elif text == "Name: A to Z":
            sorted_list = self.get_list_of_texts(list_locator=prod_page_const.LIST_OF_TITLES)
            assert sorted(sorted_list) == sorted_list

        elif text == "Name: Z to A":
            sorted_list = self.get_list_of_texts(list_locator=prod_page_const.LIST_OF_TITLES)
            assert sorted(sorted_list, reverse=True) == sorted_list

        elif text == "Price: Low to High":
            sorted_list = self.get_list_of_texts(list_locator=prod_page_const.LIST_OF_PRICES)
            assert sorted(sorted_list) == sorted_list

        elif text == "Price: High to Low":
            sorted_list = self.get_list_of_texts(list_locator=prod_page_const.LIST_OF_PRICES)
            assert sorted(sorted_list, reverse=True) == sorted_list

        elif text == "Created on":
            sorted_list = "Was chosen 'Created on'. Sorting passed..."
            assert True

        else:
            raise AssertionError("Unknown position in drop list menu")
        # logging.info(f"Sorting type: --{text}--, Sorted result: --{sorted_list}--")

    def verify_number_of_products_on_page(self, locator):
        """ verify if the number of elements on the page no more then value from drop down menu"""
        for name in self.get_list_of_drop_down_values(locator=locator):
            self.click_concrete_value_from_drop_down_list(value=name, locator=locator)
            actual_list_of_numbers_on_page = self.driver.find_elements(*prod_page_const.LIST_OF_PRODUCTS_ON_PAGE_GRID_VIEW_xpath)
            # logging.info(
            #     f"ACTUAL number on page: --{len(actual_list_of_numbers_on_page):2}-- is less or equal then number from dropdown box: --{name}--")
            assert int(name) >= len(actual_list_of_numbers_on_page)

    def verify_products_type_view_on_page(self, locator):
        """ verify if the type of view of elements on the page is the same as it is in drop down menu"""
        for name in self.get_list_of_drop_down_values(locator=locator):
            self.click_concrete_value_from_drop_down_list(value=name, locator=locator)
            if name == "Grid":
                list_of_products_locator = prod_page_const.LIST_OF_PRODUCTS_ON_PAGE_GRID_VIEW_xpath
            elif name == "List":
                list_of_products_locator = prod_page_const.LIST_OF_PRODUCTS_ON_PAGE_LIST_VIEW_xpath
            else:
                raise ValueError("Wrong value")
            assert self.wait_find_element(locator=list_of_products_locator)
            # logging.info(f"ACTUAL view type: --{list_of_products_locator}--, EXPECTED view type: --{name}--")

    def verify_filter_by_price_functionality(self, locator):
        """ verify functionality of the 'Filter by price' filter  (drop down menu)"""
        # logging.info(f"Values from 'Filter by': --{self.get_list_of_texts(locator)}--")

        for index in range(len(self.wait_find_elements(locator))):
            web_element = self.wait_find_elements(list_locator=locator)[index]
            filter_value = web_element.text
            web_element.click()
            try:
                actual_price_list = self.get_list_of_texts(list_locator=prod_page_const.LIST_OF_PRICES)
            except TimeoutException:
                logging.info(f"There are no elements for filter:   --{filter_value}--")
            else:
                self.verify_filtered_elements_on_page(filter_value, actual_price_list)
            self.wait_click_ability_and_click(prod_page_const.REMOVE_FILTER_BUTTON)

    def verify_filtered_elements_on_page(self, filter_value, actual_price_list):
        """ verify if the product prices appropriate to the ONE chosen filter (drop down menu)"""
        over_value, under_value = "", ""
        sorted_actual_price_list = sorted(actual_price_list)
        if "Under" in filter_value:
            under_value = filter_value[6:].strip()
        elif "Over" in filter_value:
            over_value = filter_value[5:].strip()
        elif "-" in filter_value:
            temp_list = filter_value.split("-")
            over_value = temp_list[0].strip()
            under_value = temp_list[-1].strip()

        if over_value:
            assert float(sorted_actual_price_list[0]) >= float(over_value)
        if under_value:
            assert float(sorted_actual_price_list[-1]) <= float(under_value)
        # logging.info(f"Filter values: --{over_value=:20}--,--{under_value=:20}-- . Actual price list: --{actual_price_list}--")
