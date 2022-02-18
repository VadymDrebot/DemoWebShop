import logging
from selenium.webdriver.common.by import By

from constants import header_constants as header_const
from constants import shopping_cart_constants as cart_const
from constants.product_page_constants import PAGE_TITLE_class
# from constants.shopping_cart_constants import ShoppingCartObject
from functions.log_in_functions import LogInFunctions
from functions.shopping_cart_functions import ShoppingCartObject

class TestShoppingCartRegisteredUser:
    """  Tests for registered user:
    8. add random product and verify its existence in shopping cart after LogOut and LogIn again
    9. add 3 more random products  and verify its existence in shopping cart after LogOut and LogIn again
    10. removing random position from shopping cart by tick and verify its absence in shopping cart after LogOut and LogIn again
    """

    logger = logging.getLogger(__name__)

    def test8(self, shopping_cart_reg):
        """
        Summary: add random product from random 'Category page' and verify its existence in 'Shopping cart' after LogOut and LogIn again
        Steps:
             1. remember number of products in 'Shopping cart'
             2. click 'Add to Cart' on a random product
             3. verify the number next to 'Shopping cart' in the header increase by '1'
             5. verify presence of the added product in the 'Shopping cart'
             6. Log Out
             7. Log In with the same credentials
             8. verify the existence of the ADDED product (not all products) in the 'Shopping cart'
        """
        cart_object = ShoppingCartObject(start_count_in_cart=shopping_cart_reg.get_item_quantity_from_top_menu_shopping_cart(comment='before'))

        # 1. remember number of products in 'Shopping cart'

        # 2. click 'Add to Cart' on a random cart_object (verifying "The cart_object has been added to your shopping cart" message)
        shopping_cart_reg.add_random_products_to_shopping_cart(cart_object, adding_amount := 1)

        # 3. verify the number next to 'shopping cart' in the top menu increase by '1'
        assert shopping_cart_reg.get_item_quantity_from_top_menu_shopping_cart(comment='after') == cart_object.start_count_in_cart + adding_amount

        # 4. verify presence of the chosen cart_object in the 'shopping cart'
        shopping_cart_reg.verify_presence_of_products_inside_shopping_cart(cart_object, comment="before LogOut")

        # 6,7 Log Out and Log In with the same credentials
        LogInFunctions(shopping_cart_reg.driver).logout_and_login()

        # 8. verify the existence of the ADDED cart_object in the "shopping cart"
        shopping_cart_reg.verify_presence_of_products_inside_shopping_cart(cart_object, comment="after LogIn")

    def test9(self, shopping_cart_reg):
        """
             Summary: add 2 random product from random Category page and verify its existence in shopping cart after LogOut and LogIn again
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
        cart_object = ShoppingCartObject(start_count_in_cart=shopping_cart_reg.get_item_quantity_from_top_menu_shopping_cart())

        # 2,3. click 'Add to Cart' on a random product twice (verifying "The cart_object has been added to your shopping cart" message)
        shopping_cart_reg.add_random_products_to_shopping_cart(cart_object, adding_amount=2)

        # 4. verify the number next to 'shopping cart' in the top menu increase by '2'
        assert shopping_cart_reg.get_item_quantity_from_top_menu_shopping_cart(comment='after') == cart_object.start_count_in_cart + 2

        # 5. verify presence of the chosen cart_object in the 'shopping cart'
        shopping_cart_reg.verify_presence_of_products_inside_shopping_cart(cart_object, comment="before LogOut")

        # 6,7 Log Out and Log In with the same credentials
        LogInFunctions(shopping_cart_reg.driver).logout_and_login()

        # 8. verify the existence of the ADDED cart_object in the "shopping cart"
        shopping_cart_reg.verify_presence_of_products_inside_shopping_cart(cart_object, comment="after  LogIn")

    def test10(self, shopping_cart_reg):
        """
             Summary: removing two random positions from 'Shopping cart' by tick and verify its absence in Shopping cart after LogOut and LogIn again
             Preconditions: 'Shopping cart' should have at least 2 product
             Steps:
                   1. remember number of products in 'Shopping cart'
                   2. click 'Shopping cart'
                   3. in the shopping cart tick next to the random product in the 'Remove' column
                   4. click 'Update shopping cart' button
                   5. verify removed product not in the 'Shopping cart' any more
                   6. verify the number next to 'shopping cart' in the top menu decrease by '2'
                   7. Log Out
                   8. Log In with the same credentials
                   9. verify the absence of the removed product in the "shopping cart"
        """
        # 1. remember number of products in 'Shopping cart'
        cart_object = ShoppingCartObject(start_count_in_cart=shopping_cart_reg.get_item_quantity_from_top_menu_shopping_cart())
        assert cart_object.start_count_in_cart >= 2, "Quantity in the 'Shopping cart' too small for test"

        # 2,3,4 click 'Shopping cart'. Tick next to the random product in the 'Remove' column. Click 'Update shopping cart' button
        shopping_cart_reg.remove_random_products_from_shopping_cart(cart_object, removing_positions_amount=2)

        # 5. verify removed product not in the 'Shopping cart' any more
        shopping_cart_reg.verify_absence_of_products_inside_shopping_cart(cart_object, comment="before LogOut")

        # 6. verify the number next to 'shopping cart' in the top menu increase by '2'
        assert shopping_cart_reg.get_item_quantity_from_top_menu_shopping_cart() == \
               cart_object.start_count_in_cart - cart_object.removing_products_amount

        # 7,8 Log Out and Log In with the same credentials
        LogInFunctions(shopping_cart_reg.driver).logout_and_login()

        # 9. verify the absence of the REMOVED position in the "shopping cart"
        shopping_cart_reg.verify_absence_of_products_inside_shopping_cart(cart_object, comment="after LogIn")
