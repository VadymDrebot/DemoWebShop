import pytest

from Pages.Header import header_constants as header_const
from Pages.Shopping_cart_Page import shopping_cart_constants as cart_const


class TestShoppingCartUnregisteredUser:
    """  Tests for unregistered user:
    test1: verify empty 'Shopping cart'
    test2: adding one/several random products to the 'Shopping cart'
    test3: removing random product from the 'Shopping cart'
    test4: set quantity to 3 of a random product in the 'Shopping cart'.
    """

    def test1_empty_shopping_cart(self, product_page_elements):
        """
        Summary: verify empty shopping cart
            Steps:
                 1. move mouse to 'shopping cart' in header
                 2. verify prompt message: 'You have no items in your shopping cart.'
                 3. click 'Shopping cart' in header
                 4. verify page name: 'Shopping cart' and message: 'Your Shopping Cart is empty!'
        """
        # 1. move mouse to 'shopping cart' in header
        product_page_elements.move_mouse_to_locator(locator=header_const.SHOPPING_CART_BUTTON_IN_HEADER_id)

        # 2. verify PROMPT message: 'You have no items in your shopping cart.'
        # DO NOT WORKS IN 'HEADLESS' MODE
        # product_page_elements.verify_message(locator=header_const.USERPROMPT_SHOPPING_CART_IN_HEADER_xpath,
        #                                      expected_text=header_const.USERPROMPT_EMPTY_SHOPPING_CART_text)

        # 3. click 'Shopping cart' in header and verify page name 'Shopping cart'
        product_page_elements.click_button_and_verify_new_url(button=header_const.SHOPPING_CART_BUTTON_IN_HEADER_id,
                                                              url=cart_const.SHOPPING_CART_url)

        # 4. verify page name: 'Shopping cart' and message: 'Your Shopping Cart is empty!'
        product_page_elements.verify_empty_shopping_cart()

    @pytest.mark.parametrize("adding_amount", [2, 4])
    def test2_add_several_random_products(self, cart_object, adding_amount):
        """
        Summary: add random products to the 'Shopping cart' and verify its presence
        Steps:
            1. verify quantity in 'Shopping cart' in header is 0
            2. click 'Add to Cart' on a random products
            3. verify message at the top of the page: "The product has been added to your shopping cart"
            4. verify the number next to 'Shopping cart' == 'adding_amount'
            5. verify presence of the added products in the 'shopping cart'
        """
        cart_object.add_products_and_verify_its_presence_in_shopping_cart(adding_amount=adding_amount)

    @pytest.mark.parametrize("adding_amount,removed_amount", [(2, 2), (2, 1)])
    def test3_remove_random_products(self, cart_object, adding_amount, removed_amount):
        """
        Summary: 6. removing random products from the 'Shopping cart'
        Steps:
            1. add one/several products to the 'Shopping crt'
            2. verify message at the top of the page after each adding: "The product has been added to your shopping cart"
            3. verify presence of the added products in the 'Shopping cart'
            4. in the 'Shopping cart' tick in the column 'Remove' next to the random product
            5. click 'Update shopping cart' button
            6. verify removed product is absent in the 'Shopping cart'
         """
        # 1-3. add one/several products to the 'Shopping crt' and verify its presence
        cart_object.add_products_and_verify_its_presence_in_shopping_cart(adding_amount=adding_amount)

        # 4-5. remove random product from the 'Shopping cart'
        cart_object.remove_random_products_with_update_button(removed_amount=removed_amount)

        # 6. verify removed cart_object not in the 'Shopping cart' any more
        assert not cart_object.check_presence_of_products_inside_shopping_cart(checked_products=cart_object.list_of_removed_products)

    @pytest.mark.parametrize("adding_product_amount,increasing_amount", [(2, 2), (3, 10)])
    def test4_increase_product_quantity_with_quantity_input_field(self, cart_object, adding_product_amount, increasing_amount):
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
        # 1-4. add one/several products to the 'Shopping crt' and verify its presence

        cart_object.add_products_and_verify_its_presence_in_shopping_cart(adding_amount=adding_product_amount)

        # 5. remember random product to the 'cart.object.product_under_work
        cart_object.get_random_product()

        # 6. remember 'total' price and 'sub-total' price
        cart_object.get_total_and_subtotal_data(comment="before cart edit")

        # 7-9. in the shopping cart fill the input field 'Qty.' with number '2' and click 'Update'
        cart_object.product_under_work.quantity += increasing_amount
        cart_object.set_item_quantity_and_click_update()

        # 11. verify 'total' and 'sub-total' increased by cart_object's price
        cart_object.get_total_and_subtotal_data(comment="after cart edit")

        assert float(cart_object.total_price.after_cart_edit) == \
               float(cart_object.total_price.before_cart_edit) * cart_object.product_under_work.quantity

        assert float(cart_object.sub_total_price.after_cart_edit) == \
               float(cart_object.sub_total_price.before_cart_edit) + \
               float(cart_object.product_under_work.price) * increasing_amount
