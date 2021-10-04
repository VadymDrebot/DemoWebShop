import random
import time

from selenium.webdriver.common.by import By

from constants import header_constants as header_const
from constants import product_page_constants as prod_page_const
from constants import shopping_cart_constants as cart_const
from constants.product_page_constants import PAGE_TITLE_class
from functions.project_functions import ProjectFunction


class ShoppingCartObject():
    def __init__(self, start_count_in_cart=0, removing_positions_amount=0, removing_products_amount=0):
        self.list_of_products_under_work = []  # each element will be : [ {"title": "", "price": "", "dom index": ""}, ...]
        self.product_under_work = {"title": "", "price": "", "dom index": "", "quantity": 0}  # the product 'under work'
        self.start_count_in_cart = start_count_in_cart
        self.current_count_in_cart = self.start_count_in_cart

        self.total_price = {"before cart edit": "", "after cart edit": ""}
        self.sub_total_price = {"before cart edit": "", "after cart edit": ""}


class ShoppingCartFunctions(ProjectFunction):

    def choose_random_product_in_shopping_cart(self, cart_object):
        """
        choose RANDOM product from SHOPPING CART
        fill: cart_object.product_under_work : {"title": "", "price": "", "dom index": ""}
        """
        cart_object.list_of_cart_dom_indexes = self.get_list_of_dom_indexes(products_list_locator=cart_const.LIST_OF_PRODUCTS_IN_SHOPPING_CART_xpath)
        random_dom_index = random.choice(cart_object.list_of_cart_dom_indexes)

        cart_object.product_under_work["dom index"] = random_dom_index
        cart_object.product_under_work["title"] = self.get_text_from_locator(
            locator=cart_const.PRODUCT_TITLE_IN_SHOPPING_CART_xpath.format(index=random_dom_index))
        cart_object.product_under_work["price"] = self.get_text_from_locator(
            locator=cart_const.PRODUCT_PRICE_IN_SHOPPING_CART_xpath.format(index=random_dom_index))
        return cart_object

    def add_products_to_shopping_cart(self, cart_object, adding_amount):
        """
        'adding_amount' (type: <int>) -- quantity of products, wanted to add to 'Shopping cart'
        make: add 'adding_amount' products to a shopping cart
        fill: list_of_cart_dom_indexes with (type: <list>)  with  {"title": "", "price":""} , ...
        """
        self.logger.info(f"Cart before adding: {self.get_list_of_shopping_cart_products(cart_object)}")
        while cart_object.current_count_in_cart != cart_object.start_count_in_cart + adding_amount:
            current_url = self.open_random_product_category_page_and_get_url()
            self.click_add_cart_of_random_product(cart_object, current_url)

    def click_add_cart_of_random_product(self, cart_object, current_url=""):
        """
        make: on a cart_object category page(with numerous adding_amount of products) choose RANDOM cart_object with a 'Add to cart' button
        fill: cart_object.list_of_products_under_work = [ {"title": "", "price":""} ]
        """
        cart_object.list_of_add_cart_dom_indexes = self.get_list_of_dom_indexes(
            products_list_locator=prod_page_const.LIST_OF_PRODUCTS_ON_PAGE_xpath,
            condition_list_locator=prod_page_const.LIST_OF_ADD_TO_CART_BUTTONS_ON_PAGE_xpath)

        while cart_object.list_of_add_cart_dom_indexes:
            random_dom_index = random.choice(cart_object.list_of_add_cart_dom_indexes)
            cart_object.list_of_add_cart_dom_indexes.remove(random_dom_index)

            # if 'add to cart' button exists -- remember 'name' and 'price' and click it
            cart_object.product_under_work["title"] = self.get_text_from_locator(
                locator=prod_page_const.LIST_OF_PRODUCT_TITLES_ON_PAGE_xpath.format(index=random_dom_index))
            cart_object.product_under_work["price"] = self.get_text_from_locator(
                locator=prod_page_const.LIST_OF_PRODUCT_PRICES_ON_PAGE_xpath.format(index=random_dom_index))

            self.driver.find_element(by=By.XPATH,
                                     value=prod_page_const.LIST_OF_ADD_TO_CART_BUTTONS_ON_PAGE_xpath.format(index=random_dom_index)).click()

            # after click 'Add to Cart' some products open 'Product page' to clarify details. If happens -- open new 'Product category page'
            time.sleep(1)
            if self.driver.current_url == current_url:
                self.verify_message(locator=cart_const.PRODUCT_HAS_BEEN_ADDED_MESSAGE_xpath,
                                    expected_text=cart_const.PRODUCT_HAS_BEEN_ADDED_MESSAGE_text, comments="above the header")
                # write 'name' and 'price' into the list 'cart_object.list_of_products_under_work' as a dictionary
                self.logger.info(f"Product was added to Shopping cart: -{cart_object.product_under_work['title']}-")
                copy_for_list = cart_object.product_under_work.copy()
                cart_object.list_of_products_under_work.append(copy_for_list)
                cart_object.current_count_in_cart += 1
                return
            else:
                break

    def get_item_quantity_from_top_menu_shopping_cart(self, comment=""):
        """
        make: READ quantity of products in the 'Shopping cart' in the header .
        return: <int>
        """
        quantity = self.get_text_from_locator(locator=header_const.QUANTITY_OF_PRODUCTS_IN_SHOPPING_CART_xpath)
        int_quantity = int(quantity[1:-1])
        self.logger.info(f"Quantity of products in shopping cart from the header -{comment}- : -{int_quantity}-")
        return int_quantity

    def set_item_quantity_in_shopping_cart(self, cart_object, value):
        """
        make: change cart_object item quantity (Qty.) in the shopping cart
        Params: 'action' -- 'increase' or 'decrease' , 'value' -- adding_amount(int) for 'action' """
        self.wait_send_keys(locator=cart_const.PRODUCT_QUANTITY_INPUT_FIELD_xpath.format(index=cart_object.product_under_work["dom index"]),
                            data=f"{value}")
        self.wait_click_ability_and_click(locator=cart_const.UPDATE_SHOPPING_CART_BUTTON_name, locator_type=By.NAME)

        new_value = self.get_value_from_input_field(
            locator=cart_const.PRODUCT_QUANTITY_INPUT_FIELD_xpath.format(index=cart_object.product_under_work['dom index']))
        self.logger.info(f"New quantity of -{cart_object.product_under_work['title']}- : -{new_value}-")

    def verify_presence_of_products_inside_shopping_cart(self, cart_object, comment="Expected product in the Shopping cart"):
        """
        make: verify presence of all products from the list: 'cart_object.list_of_products_under_work' in the shopping cart
        input params:  cart_object.list_of_products_under_work
        """
        # go to the 'Shopping cart' by click 'Shopping Cart' button in the header
        self.wait_click_ability_and_click(locator=header_const.SHOPPING_CART_BUTTON_IN_HEADER_id, locator_type=By.ID)

        for cart_object.product_under_work in cart_object.list_of_products_under_work:
            assert self.check_presence_of_the_product_inside_shopping_cart(cart_object), \
                f"-{cart_object.product_under_work['title']}- not in the cart"
            # self.logger.info(f"-{comment}-  : -{cart_object.product_under_work['title']}-")
        self.logger.info(f"Shopping cart -{comment}-  : -{self.get_list_of_texts(list_locator=cart_const.LIST_OF_TITLES_IN_SHOPPING_CART_xpath)}-")

    def check_presence_of_the_product_inside_shopping_cart(self, cart_object):
        """
        make: check if ONE (cart_object.product_under_work) product presents in the 'Shopping cart':
        input params: cart_object.product_under_work
        return: True / False
        """
        cart_object.list_of_cart_dom_indexes = self.get_list_of_dom_indexes(products_list_locator=cart_const.LIST_OF_PRODUCTS_IN_SHOPPING_CART_xpath)
        for product_dom_index in cart_object.list_of_cart_dom_indexes:
            if cart_object.product_under_work["title"] == \
                    self.get_text_from_locator(locator=cart_const.PRODUCT_TITLE_IN_SHOPPING_CART_xpath.format(index=product_dom_index)):

                # verify 'price' only if name was found in the Shopping cart
                if cart_object.product_under_work["price"] == \
                        self.get_text_from_locator(locator=cart_const.PRODUCT_PRICE_IN_SHOPPING_CART_xpath.format(index=product_dom_index)):
                    # self.logger.info(f"title: -{title_from_dom}- , price: -{price_from_dom}-")
                    return True
        else:
            return False

    def verify_absence_of_products_inside_shopping_cart(self, cart_object, comment="Absent product"):
        """
        make: verify(assert) absence of ALL products from 'cart_object.list_of_products_under_work' in the 'Shopping cart'
        input param: cart_object.list_of_products_under_work  (type <list>)
        """
        # go to the 'Shopping cart' (by click 'Shopping Cart' button in the header)
        self.wait_click_ability_and_click(locator=header_const.SHOPPING_CART_BUTTON_IN_HEADER_id, locator_type=By.ID)

        if cart_object.current_count_in_cart == 0:
            self.verify_empty_shopping_cart()
            self.logger.info(f"Shopping cart is empty -{comment}-")

        else:
            for cart_object.product_under_work in cart_object.list_of_products_under_work:
                # assert not self.check_presence_of_the_product_inside_shopping_cart(cart_object), \
                assert not self.check_presence_of_the_product_inside_shopping_cart(cart_object), \
                    f"-{cart_object.product_under_work['title']}- presents in the cart"
                # self.logger.info(f" -{comment}-  : -{cart_object.product_under_work['title']}-")

            self.logger.info(
                f"Shopping cart -{comment}-  : -{self.get_list_of_texts(list_locator=cart_const.LIST_OF_TITLES_IN_SHOPPING_CART_xpath)}-")

    def remove_random_products_from_shopping_cart(self, cart_object, removing_positions_amount=0, removing_products_amount=0):
        """
        removing_positions_amount -- number of ticks in the 'Remove' column next to removing product
        removing_products_amount -- number from the column 'Qty.' column next to removing product
        make: choose RANDOM positions (amount==removing_positions_amount) in the shopping cart,tick next to it, click 'Update shopping cart'
        fill: cart_object.list_of_products_under_work -- list of the removed positions for further actions
        """
        cart_object.list_of_products_under_work.clear()
        setattr(cart_object, "removing_positions_amount", removing_positions_amount)
        setattr(cart_object, "removing_products_amount", removing_products_amount)

        # make list of 'Shopping cart' dom indexes
        self.wait_click_ability_and_click(locator=header_const.SHOPPING_CART_BUTTON_IN_HEADER_id, locator_type=By.ID)
        self.logger.info(f"Shopping cart before removing : -{self.get_list_of_texts(list_locator=cart_const.LIST_OF_TITLES_IN_SHOPPING_CART_xpath)}-")

        cart_object.list_of_cart_dom_indexes = self.get_list_of_dom_indexes(products_list_locator=cart_const.LIST_OF_PRODUCTS_IN_SHOPPING_CART_xpath)

        for _ in range(cart_object.removing_positions_amount):
            random_dom_index = random.choice(cart_object.list_of_cart_dom_indexes)  # choose random DOM-index , f.e. '2'
            self.wait_click_ability_and_click(locator=cart_const.PRODUCT_REMOVING_CHECK_BOX_IN_SHOPPING_CART_xpath.format(index=random_dom_index))

            # remember 'title' and 'quantity' of the removing position
            cart_object.product_under_work["title"] = self.get_text_from_locator(
                locator=cart_const.PRODUCT_TITLE_IN_SHOPPING_CART_xpath.format(index=random_dom_index))

            # count quantity of removing items for further actions (in case if there were >1 items in 'Qty' column)
            cart_object.removing_products_amount += int(self.get_value_from_input_field(
                locator=cart_const.PRODUCT_QUANTITY_INPUT_FIELD_xpath.format(index=random_dom_index)))

            copy_for_list = cart_object.product_under_work.copy()
            cart_object.list_of_products_under_work.append(copy_for_list)
            cart_object.list_of_cart_dom_indexes.remove(random_dom_index)

            self.logger.info(f"Removing product: -{cart_object.product_under_work['title']}-")

            # click 'Update shopping cart' button
        self.wait_click_ability_and_click(locator_type=By.NAME, locator=cart_const.UPDATE_SHOPPING_CART_BUTTON_name)
        cart_object.current_count_in_cart -= cart_object.removing_products_amount
        return cart_object

    def get_total_and_subtotal_data(self, cart_object, comment):
        """
        make: remember 'total' product price and 'sub-total' price of the 'Shopping cart'
        comment: <str> -- 'before cart edit' OR 'after cart edit'
        fill: cart_object.total_price = {"before cart edit": "", "after cart edit": ""} and
              cart_object.sub_total_price = {"before cart edit": "", "after cart edit": ""} depends on given key(comment)
        """
        cart_object.total_price[comment] = self.get_text_from_locator(
            locator=cart_const.PRODCUT_TOTAL_PRICE_xpath.format(index=cart_object.product_under_work["dom index"]))
        cart_object.sub_total_price[comment] = self.get_text_from_locator(locator=cart_const.SUB_TOTAL_SUM_OF_SHOPPING_CART)
        self.logger.info(f"Total price  -{comment}-: -{cart_object.total_price[comment]}-")
        self.logger.info(f"Sub total price  -{comment}-: -{cart_object.sub_total_price[comment]}-")

    def get_list_of_shopping_cart_products(self, cart_object):
        """ return: list of product items , taken from the 'Shopping cart' page """
        self.wait_click_ability_and_click(locator=header_const.SHOPPING_CART_BUTTON_IN_HEADER_id, locator_type=By.ID)
        if cart_object.current_count_in_cart == 0:
            self.verify_message(locator=cart_const.SHOPPING_CART_EMPTY_CONTENT_class, locator_type=By.CLASS_NAME,
                                expected_text=cart_const.SHOPPING_CART_EMPTY_CONTENT_text)
            return []
        else:
            return self.get_list_of_texts(list_locator=cart_const.LIST_OF_TITLES_IN_SHOPPING_CART_xpath)
