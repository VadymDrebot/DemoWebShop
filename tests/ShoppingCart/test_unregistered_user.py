import logging
from selenium.webdriver.common.by import By

from constants import header_constants as header_const
from constants import shopping_cart_constants as cart_const
from constants.product_page_constants import PAGE_TITLE_class
# from constants.shopping_cart_constants import ShoppingCartObject
from functions.log_in_functions import LogInFunctions
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
    logger = logging.getLogger(__name__)

    def test1(self, shopping_cart):
        """ Summary: verify empty shopping cart
            Steps:
                 1. move mouse to 'shopping cart' in header
                 2. verify prompt message: 'You have no items in your shopping cart.'
                 3. click 'Shopping cart' in header
                 4. verify page name: 'Shopping cart' and message: 'Your Shopping Cart is empty!'
        """
        # 1. move mouse to 'shopping cart' in header
        shopping_cart.move_mouse_to_locator(locator=header_const.SHOPPING_CART_BUTTON_IN_HEADER_id, locator_type=By.ID)

        # 2. verify prompt message: 'You have no items in your shopping cart.'
        shopping_cart.verify_message(locator=header_const.USERPROMPT_SHOPPING_CART_IN_HEADER_xpath,
                                     expected_text=header_const.USERPROMPT_EMPTY_SHOPPING_CART_text)

        # 3. click 'Shopping cart' in header and verify page name 'Shopping cart'
        shopping_cart.click_button_and_verify_new_url(button_locator=header_const.SHOPPING_CART_BUTTON_IN_HEADER_id,
                                                      button_locator_type=By.ID, url=cart_const.SHOPPING_CART_url)

        # 4. verify page name: 'Shopping cart' and message: 'Your Shopping Cart is empty!'
        shopping_cart.verify_empty_shopping_cart()

    def test2(self, shopping_cart):
        """
        Summary: add one random product
        Steps:
              1. open random category page
              2. click 'Add to Cart' on a random product
              3. verify message at the top of the page: "The product has been added to your shopping cart"
              4. verify the number next to 'Shopping cart' became '1'
              5. go to 'Shopping cart'
              6. verify presence of the added product in the 'Shopping cart'
        """
        cart_object = ShoppingCartObject()
        # steps 1,2,3 -- click 'Add to Cart' on a random product and verify message "The product has been added to your shopping cart"
        shopping_cart.add_random_products_to_shopping_cart(cart_object, adding_amount := 1)

        # 3. verify the number next to 'Shopping cart' became '1'
        assert shopping_cart.get_item_quantity_from_top_menu_shopping_cart() == adding_amount

        # 4. verify presence of the added product in the 'Shopping cart'
        shopping_cart.verify_presence_of_products_inside_shopping_cart(cart_object)

    def test3(self, shopping_cart):
        """
        Summary: add 2 random products
        Steps:
            1. click 'Add to Cart' on a first random product
            2. verify message at the top of the page: "The product has been added to your shopping cart"
            3. click 'Add to Cart' on a second random product
            4. verify message at the top of the page: "The product has been added to your shopping cart"
            5. verify the number next to 'shopping cart' became '2'
            6. verify presence of the chosen products in the 'shopping cart'
        """
        cart_object = ShoppingCartObject()
        # 1-4. click 'Add to Cart' on 2 random products (verifying "The cart_object has been added to your shopping cart" message)
        shopping_cart.add_random_products_to_shopping_cart(cart_object, adding_amount := 2)

        # 5. verify the number next to the 'Shopping cart' became '2'
        assert shopping_cart.get_item_quantity_from_top_menu_shopping_cart() == adding_amount

        # 6. verify presence of the added products in the 'Shopping cart'
        shopping_cart.verify_presence_of_products_inside_shopping_cart(cart_object)

    def test4(self, shopping_cart):
        """
        Summary: add 5 random products
        Steps:
            1. click 'Add to Cart' on 5 random products (verifying "The cart_object has been added to your shopping cart" message)
            2. verify the number next to the 'Shopping cart' became '5'
            3. verify presence of the added products in the 'Shopping cart'
        """
        cart_object = ShoppingCartObject()
        # 1. click 'Add to Cart' on 5 random products (verifying "The cart_object has been added to your shopping cart" message)
        shopping_cart.add_random_products_to_shopping_cart(cart_object, adding_amount := 5)

        # 2. verify the number next to 'shopping cart' became '5'
        assert shopping_cart.get_item_quantity_from_top_menu_shopping_cart() == adding_amount

        # 3. verify presence of the chosen products in the 'shopping cart'
        shopping_cart.verify_presence_of_products_inside_shopping_cart(cart_object)

    def test6(self, shopping_cart):
        """
        Summary: 6. removing random product from shopping cart
        Steps:
            1. click 'Add to Cart' on a first random product
            2. verify message at the top of the page: "The product has been added to your shopping cart"
            3. click 'Add to Cart' on a second random product
            4. verify message at the top of the page: "The product has been added to your shopping cart"
            5. verify the number next to 'shopping cart' became '2'
            6. verify presence of the added products in the 'Shopping cart'
            7. in the 'Shopping cart' tick in the column 'Remove' next to the random product
            8. click 'Update shopping cart' button
            9. verify removed product is absent in the 'Shopping cart'
            10.verify the number next to the 'Shopping cart' became '1'
        """
        cart_object = ShoppingCartObject()
        # 1-4. click 'Add to Cart' on 2 random products (verifying "The product has been added to your shopping cart" messages)
        shopping_cart.add_random_products_to_shopping_cart(cart_object, adding_amount := 2)

        # 5. verify the number next to 'shopping cart' became '2'
        assert shopping_cart.get_item_quantity_from_top_menu_shopping_cart() == adding_amount

        # 6. verify presence of the chosen products in the 'shopping cart'
        shopping_cart.verify_presence_of_products_inside_shopping_cart(cart_object, comment="Cart BEFORE removing ")

        # 7-8. remove random product from the 'Shopping cart'
        shopping_cart.remove_random_products_from_shopping_cart(cart_object, removing_positions_amount=1)

        # 9. verify removed cart_object not in the 'Shopping cart' any more
        shopping_cart.verify_absence_of_products_inside_shopping_cart(cart_object, comment="Cart AFTER removing  ")

        # 10.verify the number next to the 'Shopping cart'
        assert shopping_cart.get_item_quantity_from_top_menu_shopping_cart() == adding_amount - cart_object.removing_products_amount

    def test7(self, shopping_cart):
        """
        Summary: increase quantity of a random product in the 'Shopping cart'
        Steps:
            1. click 'Add to Cart' on a random product
            2. verify message at the top of the page: "The product has been added to your shopping cart"
            3. verify the number next to 'Shopping cart' became '1'
            4. verify presence of the added product in the 'Shopping cart'
            5. choose a random product for edit
            6. remember 'total' price and 'sub-total' price
            7. in the 'Shopping cart' fill the input field 'Qty.' with number '2'
            8. click 'Update Shopping cart' button
            9. verify the number next to 'Shopping cart' became '1'
            10. verify the number in 'Qty.'  became  '2'
            11. verify 'total' and 'sub-total' increased by product's price
        """
        cart_object = ShoppingCartObject()
        # 1-2. click 'Add to Cart' on a random product,  verify message at the top of the page: "The product has been added to your shopping cart"
        shopping_cart.add_random_products_to_shopping_cart(cart_object, adding_amount := 2)

        # 3. verify the number next to 'Shopping cart' became '1'
        assert shopping_cart.get_item_quantity_from_top_menu_shopping_cart() == adding_amount

        # 4. verify presence of the added product in the 'Shopping cart'
        shopping_cart.verify_presence_of_products_inside_shopping_cart(cart_object)

        # 5. choose a cart_object for edit
        shopping_cart.choose_random_product_in_shopping_cart(cart_object)

        # 6. remember 'total' price and 'sub-total' price
        shopping_cart.get_total_and_subtotal_data(cart_object, comment='before cart edit')

        # 6. in the shopping cart fill the input field 'Qty.' with number '2' and click 'Update'
        shopping_cart.set_item_quantity_in_shopping_cart(cart_object, value := 4)

        # 7. verify 'total' and 'sub-total' increased by cart_object's price
        shopping_cart.get_total_and_subtotal_data(cart_object, comment='after cart edit')

        assert float(cart_object.total_price["after cart edit"]) == \
               float(cart_object.total_price["before cart edit"]) * value

        assert float(cart_object.sub_total_price["after cart edit"]) == \
               float(cart_object.sub_total_price["before cart edit"]) + float(cart_object.product_under_work["price"]) * (value - 1)
