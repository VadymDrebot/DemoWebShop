import logging
from selenium.webdriver.common.by import By
# from constants.shopping_cart_constants import NewShoppingCart
from functions.log_in_functions import LogInFunctions
from functions.shopping_cart_functions import NewShoppingCart


# class TestShoppingCartUnregisteredUser:
#     """  Tests for unregistered user:
#     1. verify empty shopping cart
#     2. add random product from 'product list' and verify its existence in shopping cart
#     3. add random product from 'product page' and verify its existence in shopping cart
#     4. add 2 random products from 'product list' and verify its existence in shopping cart
#     5. add 5 random products from 'product list' and verify its existence in shopping cart
#     6. removing random product from shopping cart
#     7. increase quantity of a random product in the shopping cart. Verify 'total' and 'sub-total' sums and quantity in top menu
#     """
#     logger = logging.getLogger(__name__)
#
#     def test1(self, shopping_cart):
#         """ Summary: verify empty shopping cart
#             Steps:
#                  1. move mouse to 'shopping cart' in header and verify 'You have no items in your shopping cart.' prompt message
#                  2. click 'Shopping cart' in header and verify page name and 'Your Shopping Cart is empty!' message
#         """
#         # 1. move mouse to 'shopping cart' in header and verify 'You have no items in your shopping cart.' prompt message
#         shopping_cart.move_mouse_to_locator(locator=shopping_cart.SHOPPING_CART_BUTTON_IN_HEADER_id, locator_type=By.ID)
#         shopping_cart.verify_message(locator=shopping_cart.USERPROMPT_SHOPPING_CART_IN_HEADER_xpath,
#                                      expected_text=shopping_cart.USERPROMPT_EMPTY_SHOPPING_CART_text)
#
#         # 2. click 'Shopping cart' in top menu and verify page name 'Shopping cart' and 'Your Shopping Cart is empty!' message
#         shopping_cart.click_button_and_verify_new_url(button_locator=shopping_cart.SHOPPING_CART_BUTTON_IN_HEADER_id,
#                                                       button_locator_type=By.ID, url=shopping_cart.SHOPPING_CART_url)
#         shopping_cart.verify_message(locator=shopping_cart.PAGE_TITLE_class, locator_type=By.CLASS_NAME,
#                                      expected_text=shopping_cart.PAGE_TITLE_SHOPPING_CART_text)
#         shopping_cart.verify_message(locator=shopping_cart.SHOPPING_CART_CONTENT_class, locator_type=By.CLASS_NAME,
#                                      expected_text=shopping_cart.SHOPPING_CART_EMPTY_CCONTENT_text)
#
#     def test2(self, shopping_cart):
#         """
#         Summary: add one random product from 'product list' and verify its existence in shopping cart
#         Steps:
#               1. click 'Add to Cart' on a random product (verifying "The product has been added to your shopping cart" message)
#               2. verify the number next to 'shopping cart' became '1'
#               3. verify presence of the chosen product in the 'shopping cart'
#         """
#         product = NewShoppingCart()
#         # 1. click 'Add to Cart' on a random product (verifying "The product has been added to your shopping cart" message)
#         shopping_cart.add_some_products_to_shopping_cart(product, amount=1)
#
#         # 2. verify the number next to 'shopping cart' became ''
#         assert shopping_cart.get_item_quantity_from_top_menu_shopping_cart() == "(1)"
#
#         # 3. verify presence of the chosen products in the 'shopping cart'
#         shopping_cart.verify_presence_of_products_inside_shopping_cart(product)
#
#     def test4(self, shopping_cart):
#         """
#         Summary: add 2 random products from 'product list' and verify its existence in shopping cart
#         Steps:
#             1. click 'Add to Cart' on 2 random products (verifying "The product has been added to your shopping cart" message)
#             2. verify the number next to 'shopping cart' became '2'
#             3. verify presence of the chosen products in the 'shopping cart'
#         """
#         product = NewShoppingCart()
#         # 1. click 'Add to Cart' on 2 random products (verifying "The product has been added to your shopping cart" message)
#         shopping_cart.add_some_products_to_shopping_cart(product, amount=2)
#
#         # 2. verify the number next to 'shopping cart' became '2'
#         assert shopping_cart.get_item_quantity_from_top_menu_shopping_cart() == "(2)"
#
#         # 3. verify presence of the chosen products in the 'shopping cart'
#         shopping_cart.verify_presence_of_products_inside_shopping_cart(product)
#
#     def test5(self, shopping_cart):
#         """
#         Summary: add 5 random products from 'product list' and verify its existence in shopping cart
#         Steps:
#             1. click 'Add to Cart' on 5 random products (verifying "The product has been added to your shopping cart" message)
#             2. verify the number next to 'shopping cart' became '5'
#             3. verify presence of the chosen products in the 'shopping cart'
#         """
#         product = NewShoppingCart()
#         # 1. click 'Add to Cart' on 2 random products (verifying "The product has been added to your shopping cart" message)
#         shopping_cart.add_some_products_to_shopping_cart(product, amount=5)
#
#         # 2. verify the number next to 'shopping cart' became '5'
#         assert shopping_cart.get_item_quantity_from_top_menu_shopping_cart() == "(5)"
#
#         # 3. verify presence of the chosen products in the 'shopping cart'
#         shopping_cart.verify_presence_of_products_inside_shopping_cart(product)
#
#     def test6(self, shopping_cart):
#         """
#         Summary: 6. removing random product from shopping cart
#         Steps:
#             1. click 'Add to Cart' on 2 random products (verifying "The product has been added to your shopping cart" message)
#             2. verify the number next to 'shopping cart' became '2'
#             3. verify presence of the chosen products in the 'shopping cart'
#             4. in the shopping cart tick next to product for removing,remember it and click 'Update shopping cart' button
#             5. verify removed product not in the 'Shopping cart' any more
#         """
#         product = NewShoppingCart()
#         # 1. click 'Add to Cart' on 2 random products (verifying "The product has been added to your shopping cart" message)
#         shopping_cart.add_some_products_to_shopping_cart(product, amount=2)
#
#         # 2. verify the number next to 'shopping cart' became '2'
#         assert shopping_cart.get_item_quantity_from_top_menu_shopping_cart() == "(2)"
#
#         # 3. verify presence of the chosen products in the 'shopping cart'
#         shopping_cart.verify_presence_of_products_inside_shopping_cart(product)
#
#         # 4. remove random product from the 'shopping cart'
#         shopping_cart.remove_random_product_from_shopping_cart(product)
#
#         # 5. verify removed product not in the 'Shopping cart' any more
#         assert not shopping_cart.check_presence_of_the_product_inside_shopping_cart(product)
#         assert shopping_cart.get_item_quantity_from_top_menu_shopping_cart() == "(1)"
#         self.logger.info(f"Cart AFTER removing: -{shopping_cart.get_list_of_texts(list_locator=shopping_cart.LIST_OF_TITLES_IN_SHOPPING_CART_xpath)}")
#
#     def test7(self, shopping_cart):
#         """
#         Summary: increase quantity of a random product in the shopping cart. Verify 'total' and 'sub-total' sums and quantity in top menu
#         Steps:
#             1. click 'Add to Cart' on a random product (verifying "The product has been added to your shopping cart" message)
#             2. verify the number next to 'shopping cart' became '1'
#             3. verify presence of the chosen product in the 'shopping cart'
#             4. choose a product for edit
#             5. remember 'total' and 'sub-total'
#             6. in the shopping cart fill the input field 'Qty.' with number '2'
#             7. click 'Update Shopping cart' button
#             8. verify 'total' and 'sub-total' increased by product's price
#         """
#         product = NewShoppingCart()
#         # 1. click 'Add to Cart' on a random product (verifying "The product has been added to your shopping cart" message)
#         shopping_cart.add_some_products_to_sopping_cart(product, amount=2)
#
#         # 2. verify the number next to 'shopping cart' became '1'
#         assert shopping_cart.get_item_quantity_from_top_menu_shopping_cart() == "(2)"
#
#         # 3. verify presence of the chosen product in the 'shopping cart'
#         shopping_cart.verify_presence_of_products_inside_shopping_cart(product)
#
#         # 4. choose a product for edit
#         shopping_cart.choose_random_product_in_shopping_cart(product)
#
#         # 5. remember 'total' and 'sub-total'
#         shopping_cart.get_total_and_subtotal_data(product, time='before cart edit')
#
#         # 6. in the shopping cart fill the input field 'Qty.' with number '2' and click 'Update'
#         shopping_cart.set_item_quantity_in_shopping_cart(product, action="increase", action_parameter=1)
#
#         # 7. verify 'total' and 'sub-total' increased by product's price
#         shopping_cart.get_total_and_subtotal_data(product, time='after cart edit')
#
#         assert float(product.total_editing_product_price["after cart edit"]) == \
#                float(product.total_editing_product_price["before cart edit"]) + float(product.product_in_process["price"])
#         assert float(product.sub_total_price["after cart edit"]) == \
#                float(product.sub_total_price["before cart edit"]) + float(product.product_in_process["price"])


class TestShoppingCartRegisteredUser:
    """  Tests for registered user:
    1. add random product from 'product page' and verify its existence in shopping cart after LogOut and LogIn again
    2. add 2 more random products from 'product list' and verify its existence in shopping cart after LogOut and LogIn again
    3. removing random product from shopping cart and verify its absence in shopping cart after LogOut and LogIn again
    """

    logger = logging.getLogger(__name__)

    def test8(self, shopping_cart_reg):
        """
             Summary: add random product from 'product page' and verify its existence in shopping cart after LogOut and LogIn again
             Steps:
                   1. remember number of products in 'Shopping cart'
                   2. click 'Add to Cart' on a random product (verifying "The product has been added to your shopping cart" message)
                   3. verify the number next to 'shopping cart' in the top menu increase by '1'
                   4. verify presence of the chosen product in the 'shopping cart'
                   5. remember all products in the "Shopping cart"
                   6. Log Out
                   7. Log In with the same credentials
                   8. verify the existence of the ADDED product (not all products) in the "shopping cart"
        """
        # 1. remember number of products in 'Shopping cart'
        product = NewShoppingCart()
        shopping_cart_reg.refill_the_product(product)

        # 2. click 'Add to Cart' on a random product (verifying "The product has been added to your shopping cart" message)
        shopping_cart_reg.add_some_products_to_shopping_cart(product, amount=1)

        # 3. verify the number next to 'shopping cart' in the top menu increase by '1'
        assert shopping_cart_reg.get_item_quantity_from_top_menu_shopping_cart() == product.start_count_in_cart + 1

        # 4. verify presence of the chosen product in the 'shopping cart'
        shopping_cart_reg.verify_presence_of_products_inside_shopping_cart(product)

        # 6,7 Log Out and Log In with the same credentials
        shopping_cart_reg.logout_and_login()

        # 8. verify the existence of the ADDED product in the "shopping cart"
        shopping_cart_reg.verify_presence_of_products_inside_shopping_cart(product)
