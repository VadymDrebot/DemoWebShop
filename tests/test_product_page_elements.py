import logging
import time


from constants import product_page_constants as prod_page_const
from functions.common_functions import CommonFunctions
from functions.product_page_elements_functions import Product


class TestProductPageElements:
    """ verify correct displaying products on the page after choose and click on it in header menu"""
    logger = logging.getLogger(__name__)

    def test1(self, product_page_elements):
        product = Product(product_name="Books")
        product_page_elements.move_mouse_through_list_of_locators_and_click_last(movement_list_locator=product.mouse_movement_locators_list)
        product_page_elements.verify_correct_transition_to_page(product)
        product_page_elements.verify_ui_elements(product)

    def test2(self, product_page_elements):
        product = Product(product_name="Computers")
        product_page_elements.move_mouse_through_list_of_locators_and_click_last(movement_list_locator=product.mouse_movement_locators_list)
        product_page_elements.verify_correct_transition_to_page(product)
        product_page_elements.verify_ui_elements(product)

    def test3(self, product_page_elements):
        product = Product(product_name="Desktops")
        product_page_elements.move_mouse_through_list_of_locators_and_click_last(movement_list_locator=product.mouse_movement_locators_list)
        product_page_elements.verify_correct_transition_to_page(product)
        product_page_elements.verify_ui_elements(product)

    def test8(self, product_page_elements):
        product = Product(product_name="Cell phones")
        product_page_elements.move_mouse_through_list_of_locators_and_click_last(movement_list_locator=product.mouse_movement_locators_list)
        product_page_elements.verify_correct_transition_to_page(product)
        product_page_elements.verify_ui_elements(product)

    def test11(self, product_page_elements):
        product = Product(product_name="Jewelry")
        product_page_elements.move_mouse_through_list_of_locators_and_click_last(movement_list_locator=product.mouse_movement_locators_list)
        product_page_elements.verify_correct_transition_to_page(product)
        product_page_elements.verify_ui_elements(product)

    def test13(self, product_page_elements):
        """ Negative test"""
        product = Product(product_name := "Shoes")
        self.logger.info(f"There is no such element -{product.product_name}-")
        assert not product.mouse_movement_names_list


