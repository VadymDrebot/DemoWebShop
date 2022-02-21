from functions.log_in_functions import LogInFunctions
from functions.shopping_cart_functions import ShoppingCartObject


class TestShoppingCartRegisteredUser:
    """  Tests for registered user:
    1. add random product and verify its existence in shopping cart after LogOut and LogIn again
    2. add 3 more random products  and verify its existence in shopping cart after LogOut and LogIn again
    3. removing random position from shopping cart by tick and verify its absence in shopping cart after LogOut and LogIn again
    """

    def test8_product_existence_after_logout_login(self, shopping_cart_reg):
        """
        Summary: add random product and verify its existence in 'Shopping cart' after LogOut and LogIn again
        Precondition: Log In with Valid login|password
        Steps:
             1. remember number of products in 'Shopping cart'
             2. click 'Add to Cart' on a random product
             3. verify the number next to 'Shopping cart' in the header increase by '1'
             4. verify presence of the added product in the 'Shopping cart'
             5. Log Out
             6. Log In with the same credentials
             7. verify the existence of the ADDED product (not all products) in the 'Shopping cart'
        """
        # 1. remember number of products in 'Shopping cart'
        cart_object = ShoppingCartObject(start_count_in_cart=shopping_cart_reg.get_item_quantity_from_top_menu(comment='before'))

        # 2. click 'Add to Cart' on a random cart_object (verifying "The cart_object has been added to your shopping cart" message)
        shopping_cart_reg.add_random_products(cart_object, adding_amount := 1)

        # 3. verify the number next to 'shopping cart' in the top menu increase by '1'
        assert shopping_cart_reg.get_item_quantity_from_top_menu(comment='after') == cart_object.start_count_in_cart + adding_amount

        # 4. verify presence of the chosen cart_object in the 'shopping cart'
        shopping_cart_reg.check_presence_of_products_inside_shopping_cart(cart_object, comment="before LogOut")

        # 6,7 Log Out and Log In with the same credentials
        LogInFunctions(shopping_cart_reg.driver).logout_and_login()

        # 8. verify the existence of the ADDED cart_object in the "shopping cart"
        shopping_cart_reg.check_presence_of_products_inside_shopping_cart(cart_object, comment="after LogIn")

    def test9_two_products_existence_after_logout_login(self, shopping_cart_reg):
        """
       Summary: add 2 random product from random Category page and verify its existence in shopping cart after LogOut and LogIn again
       Precondition: Log In with Valid login|password
       Steps:
           1. remember number of products in 'Shopping cart'
           2. click 'Add to Cart' on a random product (first product)
           3. click 'Add to Cart' on a random product (second product)
           4. verify the number next to 'shopping cart' in the top menu increase by '2'
           5. verify presence of the added products in the "Shopping cart"
           6. Log Out
           7. Log In with the same credentials
           8. verify the existence of the ADDED products (not all products) in the "shopping cart"
        """
        # 1. remember number of products in 'Shopping cart'
        cart_object = ShoppingCartObject(start_count_in_cart=shopping_cart_reg.get_item_quantity_from_top_menu(comment='before'))

        # 2,3. click 'Add to Cart' on a random product twice (verifying "The cart_object has been added to your shopping cart" message)
        shopping_cart_reg.add_random_products(cart_object, adding_amount := 2)

        # 4. verify the number next to 'shopping cart' in the top menu increase by '2'
        assert shopping_cart_reg.get_item_quantity_from_top_menu(comment='after') == cart_object.start_count_in_cart + adding_amount

        # 5. verify presence of the chosen cart_object in the 'shopping cart'
        shopping_cart_reg.check_presence_of_products_inside_shopping_cart(cart_object, comment="before LogOut")

        # 6,7 Log Out and Log In with the same credentials
        LogInFunctions(shopping_cart_reg.driver).logout_and_login()

        # 8. verify the existence of the ADDED cart_object in the "shopping cart"
        shopping_cart_reg.check_presence_of_products_inside_shopping_cart(cart_object, comment="after  LogIn")

    def test10_remove_two_random_products(self, shopping_cart_reg):
        """
             Summary: removing two random positions from 'Shopping cart' by tick and verify its absence in Shopping cart after LogOut and LogIn again
             Preconditions: Log In with Valid login|password
             Steps:
                   1. click 'Add to Cart' on a random product (first product)
                   2. click 'Add to Cart' on a random product (second product)
                   3. click 'Add to Cart' on a random product (third product)
                   4. verify presence of the added products in the "Shopping cart"
                   5. in the shopping cart tick next to the two random products in the 'Remove' column
                   6. click 'Update shopping cart' button
                   7. verify removed product not in the 'Shopping cart' any more
                   8. Log Out
                   9. Log In with the same credentials
                   10. verify the absence of the removed product in the "Shopping cart"
        """
        cart_object = ShoppingCartObject()
        cart_object.removed_products = []

        # 1,2,3 click 'Add to Cart' on a random products
        shopping_cart_reg.add_random_products(cart_object, adding_amount=3)

        # 4. verify presence of the added products in the "Shopping cart"
        assert shopping_cart_reg.check_presence_of_products_inside_shopping_cart(cart_object, comment="before removing")

        # 5,5 Tick next to the random product in the 'Remove' column. Click 'Update shopping cart' button
        shopping_cart_reg.remove_random_products_with_update_button(cart_object, removed_amount=2)

        # 7. verify removed product not in the 'Shopping cart' any more
        assert not shopping_cart_reg.check_presence_of_given_products_inside_shopping_cart(cart_object,
                                                                                           given_products_list=cart_object.removed_products,
                                                                                           comment="before LogOut")
        # 8,9 Log Out and Log In with the same credentials
        LogInFunctions(shopping_cart_reg.driver).logout_and_login()

        # 10. verify the absence of the REMOVED position in the "shopping cart"
        assert not shopping_cart_reg.check_presence_of_given_products_inside_shopping_cart(cart_object,
                                                                                           given_products_list=cart_object.removed_products,
                                                                                           comment="after LogIn")
