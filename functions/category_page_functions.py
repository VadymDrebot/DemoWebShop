import logging

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
        self.logger.info(f"ACTUAL   url: --{self.driver.current_url}--")
        self.logger.info(f"EXPECTED url: --{expected_url}--")
        assert self.driver.current_url == expected_url

    def verify_ui_elements(self, category):
        self.verify_page_name(category)
        self.verify_breadcrumb(category)

        if category.sub_menu_list:
            self.logger.info(f" ACTUAL  submenu list: -{self.get_list_of_texts(prod_page_const.LIST_OF_SUBCATEGORY_ON_PAGE_xpath)}-")
            self.logger.info(f"EXPECTED submenu list: -{category.sub_menu_list}-")
            assert self.get_list_of_texts(prod_page_const.LIST_OF_SUBCATEGORY_ON_PAGE_xpath) == category.sub_menu_list
        else:
            assert self.check_presence_of_element(locator=prod_page_const.DROP_DOWN_SORT_BY_LIST_xpath)
            assert self.check_presence_of_element(locator=prod_page_const.DROP_DOWN_DISPLAY_PER_PAGE_LIST_xpath)
            assert self.check_presence_of_element(locator=prod_page_const.DROP_DOWN_VIEW_AS_LIST_xpath)

    def verify_page_name(self, category):
        actual_page_name = self.get_text_from_locator(locator=prod_page_const.PAGE_TITLE_xpath)
        expected_page_name = category.category_name
        self.logger.info(f"ACTUAL   name of the page: --{actual_page_name}--")
        self.logger.info(f"EXPECTED name of the page: --{expected_page_name}--")
        assert actual_page_name == expected_page_name, f"{actual_page_name}, {expected_page_name}"
