import time

from constants.start_page_const import Product
from functions.common_functions import CommonFunctions


class TestForUnregistered():
    def test1(self, shopping_cart_page):
        product = Product(product_subcategory="Desktops")
        shopping_cart_page.choose_product_from_header_and_click(product)
        # time.sleep(5)

        shopping_cart_page.verify_correct_transition_to_page(product)
