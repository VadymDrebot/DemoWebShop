import logging

from functions.category_page_functions import Category


class TestCategoryTransitionFromHeader:
    """ verify correct categories and subcategories transitions  after choose and click on it in the header menu:
    check for: breadcrumbs,page name,existing of 'display/sort by/view as' tools for end-point category OR category list for subcategory"""
    logger = logging.getLogger()

    def move_mouse_click_and_verify_transition(self, product_page_elements, category_name):
        category = Category(category=category_name)
        if not category.mouse_movement_categories_list:
            self.logger.info(f"There is no such category -{category.category_name}-")
            return
        product_page_elements.move_mouse_through_list_of_locators_and_click_last(mouse_movement_locators_list=category.mouse_movement_locators_list)
        product_page_elements.verify_correct_transition_to_new_url(category)
        product_page_elements.verify_ui_elements(category)

    def test1_books(self, product_page_elements):
        self.move_mouse_click_and_verify_transition(product_page_elements, category_name="Books")

    def test2_computer(self, product_page_elements):
        self.move_mouse_click_and_verify_transition(product_page_elements, category_name="Computers")

    def test3_desktops(self, product_page_elements):
        self.move_mouse_click_and_verify_transition(product_page_elements, category_name="Desktops")

    def test8(self, product_page_elements):
        self.move_mouse_click_and_verify_transition(product_page_elements, category_name="Cell phones")

    def test11(self, product_page_elements):
        self.move_mouse_click_and_verify_transition(product_page_elements, category_name="Jewelry")

    def test13(self, product_page_elements):
        """ Negative test"""
        self.move_mouse_click_and_verify_transition(product_page_elements, category_name="Shoes")
