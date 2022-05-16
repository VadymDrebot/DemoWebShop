from selenium.webdriver.common.by import By

from constants import header_constants as header_const
from constants import shopping_cart_constants as cart_const

from functions.shopping_cart_functions import ShoppingCartObject


class TestShoppingCartUnregisteredUser:
    """  Tests for unregistered user:
    test1: verify empty 'Shopping cart'
    test2: add random product to the 'Shopping cart'
    test3: add 2 random products to the 'Shopping cart'
    test4: add 5 random products to the 'Shopping cart'
    test5: removing random product from the 'Shopping cart'
    test6: set quantity to 3 of a random product in the 'Shopping cart'.
    """
# alot of fail
    # FAIL
    # def test1_empty_shopping_cart(self, shopping_cart_unreg):
    #     """ Summary: verify empty shopping cart
    #         Steps:
    #              1. move mouse to 'shopping cart' in header
    #              2. verify prompt message: 'You have no items in your shopping cart.'
    #              3. click 'Shopping cart' in header
    #              4. verify page name: 'Shopping cart' and message: 'Your Shopping Cart is empty!'
    #     """
    #     # 1. move mouse to 'shopping cart' in header
    #     shopping_cart_unreg.move_mouse_to_locator(locator=header_const.SHOPPING_CART_BUTTON_IN_HEADER_id)
    #
    #     # 2. verify prompt message: 'You have no items in your shopping cart.'
    #     shopping_cart_unreg.verify_message(locator=header_const.USERPROMPT_SHOPPING_CART_IN_HEADER_xpath,
    #                                        expected_text=header_const.USERPROMPT_EMPTY_SHOPPING_CART_text)
    #
    #     # 3. click 'Shopping cart' in header and verify page name 'Shopping cart'
    #     shopping_cart_unreg.click_button_and_verify_new_url(button_locator=header_const.SHOPPING_CART_BUTTON_IN_HEADER_id,
    #                                                         button_locator_type=By.ID, url=cart_const.SHOPPING_CART_url)
    #
    #     # 4. verify page name: 'Shopping cart' and message: 'Your Shopping Cart is empty!'
    #     shopping_cart_unreg.verify_empty_shopping_cart()

    def test2_add_one_random_product(self, shopping_cart_unreg):
        """
        Summary: add one random product
        Steps:
              1. verify quantity in 'Shopping cart' in header is 0
              2. open random category page
              3. click 'Add to Cart' on a random product
              4. verify message at the top of the page: "The product has been added to your shopping cart"
              5. verify quantity in 'Shopping cart' in header is 1
              6. go to 'Shopping cart'
              7. verify presence of the added product in the 'Shopping cart'
        """
        cart_object = ShoppingCartObject()
        assert shopping_cart_unreg.get_item_quantity_from_top_menu(comment="before adding") == 0
        # steps 1,2,3 -- click 'Add to Cart' on a random product and verify message "The product has been added to your shopping cart"
        shopping_cart_unreg.add_random_products(cart_object, adding_amount := 1)

        # 3. verify the number next to 'Shopping cart' became '1'
        assert shopping_cart_unreg.get_item_quantity_from_top_menu(comment="after adding") == adding_amount

        # 4. verify presence of the added product in the 'Shopping cart'
        assert shopping_cart_unreg.check_presence_of_products_inside_shopping_cart(cart_object)

    # @FAIL

    # def test3_add_3_random_products(self, shopping_cart_unreg):
    #     """
    #     Summary: add 2 random products
    #     Steps:
    #         1. verify quantity in 'Shopping cart' in header is 0
    #         2. click 'Add to Cart' on a first random product
    #         3. verify message at the top of the page: "The product has been added to your shopping cart"
    #         4. click 'Add to Cart' on a second random product
    #         5. verify message at the top of the page: "The product has been added to your shopping cart"
    #         6. verify the number next to 'shopping cart' became '2'
    #         7. verify presence of the added products in the 'shopping cart'
    #     """
    #     cart_object = ShoppingCartObject()
    #     assert shopping_cart_unreg.get_item_quantity_from_top_menu(comment="before adding") == 0
    #
    #     # 1-4. click 'Add to Cart' on 2 random products (verifying "The cart_object has been added to your shopping cart" message)
    #     shopping_cart_unreg.add_random_products(cart_object, adding_amount := 2)
    #
    #     # 5. verify the number next to the 'Shopping cart' became '2'
    #     assert shopping_cart_unreg.get_item_quantity_from_top_menu(comment="after adding") == adding_amount
    #
    #     # 6. verify presence of the added products in the 'Shopping cart'
    #     assert shopping_cart_unreg.check_presence_of_products_inside_shopping_cart(cart_object)
    #
    # def test4_add_5_random_products(self, shopping_cart_unreg):
    #     """
    #     Summary: add 5 random products
    #     Steps:
    #         1. click 'Add to Cart' on 5 random products (verifying "The cart_object has been added to your shopping cart" message)
    #         2. verify the number next to the 'Shopping cart' became '5'
    #         3. verify presence of the added products in the 'Shopping cart'
    #     """
    #     cart_object = ShoppingCartObject()
    #     assert shopping_cart_unreg.get_item_quantity_from_top_menu(comment="before adding") == 0
    #     # 1. click 'Add to Cart' on 5 random products (verifying "The cart_object has been added to your shopping cart" message)
    #     shopping_cart_unreg.add_random_products(cart_object, adding_amount := 5)
    #
    #     # 2. verify the number next to 'shopping cart' became '5'
    #     assert shopping_cart_unreg.get_item_quantity_from_top_menu(comment="after adding") == adding_amount
    #
    #     # 3. verify presence of the chosen products in the 'shopping cart'
    #     assert shopping_cart_unreg.check_presence_of_products_inside_shopping_cart(cart_object)


    # FAIL FAIL
    # def test6_remove_random_product(self, shopping_cart_unreg):
    #     """
    #     Summary: 6. removing random product from shopping cart
    #     Steps:
    #         1. click 'Add to Cart' on a first random product
    #         2. verify message at the top of the page: "The product has been added to your shopping cart"
    #         3. click 'Add to Cart' on a second random product
    #         4. verify message at the top of the page: "The product has been added to your shopping cart"
    #         6. verify presence of the added products in the 'Shopping cart'
    #         7. in the 'Shopping cart' tick in the column 'Remove' next to the random product
    #         8. click 'Update shopping cart' button
    #         9. verify removed product is absent in the 'Shopping cart'
    #      """
    #     cart_object = ShoppingCartObject()
    #     # 1-4. click 'Add to Cart' on 2 random products (verifying "The product has been added to your shopping cart" messages)
    #     shopping_cart_unreg.add_random_products(cart_object, adding_amount := 2)
    #
    #     # 5. verify the number next to 'shopping cart' became '2'
    #     assert shopping_cart_unreg.get_item_quantity_from_top_menu() == adding_amount
    #
    #     # 6. verify presence of the 'cart_object.list_of_products_in_shopping_cart' in the 'shopping cart'
    #     assert shopping_cart_unreg.check_presence_of_products_inside_shopping_cart(cart_object, comment="Cart BEFORE removing ")
    #
    #     # 7-8. remove random product from the 'Shopping cart'
    #     shopping_cart_unreg.remove_random_products_with_update_button(cart_object)
    #
    #     # 9. verify removed cart_object not in the 'Shopping cart' any more
    #     assert not shopping_cart_unreg.check_presence_of_the_product_inside_shopping_cart(cart_object, checked_product=cart_object.removed_product)

    def test7_increase_product_quantity_with_quantity_input_field(self, shopping_cart_unreg):
        """
        Summary: increase quantity of a random product in the 'Shopping cart'
        Steps:
            1. click 'Add to Cart' on a random 2 product
            2. verify message at the top of the page: "The product has been added to your shopping cart"
            3. verify the number next to 'Shopping cart' became '2'
            4. verify presence of the added products in the 'Shopping cart'
            5. choose a random product for edit
            6. remember 'total' price and 'sub-total' price
            7. in the 'Shopping cart' increase the input field 'Qty.' by '1'
            8. click 'Update Shopping cart' button
            9. verify the number next to 'Shopping cart' became '3'
            10. verify the number in 'Qty.'  increased by  '1'
            11. verify 'total' and 'sub-total' increased by product's price
        """
        cart_object = ShoppingCartObject()
        # 1-2. click 'Add to Cart' on a random product,  verify message at the top of the page: "The product has been added to your shopping cart"
        shopping_cart_unreg.add_random_products(cart_object, adding_amount := 2)

        # 3. verify the number next to 'Shopping cart' became '2'
        assert shopping_cart_unreg.get_item_quantity_from_top_menu() == adding_amount

        # 4. verify presence of the added product in the 'Shopping cart'
        assert shopping_cart_unreg.check_presence_of_products_inside_shopping_cart(cart_object)

        # 5. remember random product to the 'cart.object.product_under_work
        shopping_cart_unreg.get_random_product(cart_object)

        # 6. remember 'total' price and 'sub-total' price
        shopping_cart_unreg.get_total_and_subtotal_data(cart_object, comment="before cart edit")

        # 6. in the shopping cart fill the input field 'Qty.' with number '2' and click 'Update'
        cart_object.product_under_work.quantity += 1
        shopping_cart_unreg.set_item_quantity_and_click_update(cart_object)

        # 7. verify 'total' and 'sub-total' increased by cart_object's price
        shopping_cart_unreg.get_total_and_subtotal_data(cart_object, comment="after cart edit")

        assert float(cart_object.total_price.after_cart_edit) == \
               float(cart_object.total_price.before_cart_edit) * cart_object.product_under_work.quantity

        assert float(cart_object.sub_total_price.after_cart_edit) == \
               float(cart_object.sub_total_price.before_cart_edit) + \
               float(cart_object.product_under_work.price) * (cart_object.product_under_work.quantity - 1)
