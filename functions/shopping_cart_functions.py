import random, time

from selenium.webdriver.common.by import By

from constants import header_constants as header_const
from constants import product_page_constants as prod_page_const
from constants import shopping_cart_constants as cart_const

from functions.project_functions import ProjectFunction


class ProductDescription:
    def __init__(self):
        self.title = ""
        self.price = ""
        self.dom_index = ""
        self.quantity = 0


class PriceObject:
    def __init__(self):
        self.before_cart_edit = ""
        self.after_cart_edit = ""


class ShoppingCartObject:
    def __init__(self, start_count_in_cart=0):
        self.list_of_products_in_shopping_cart = []
        self.start_count_in_cart = start_count_in_cart
        self.current_count_in_cart = self.start_count_in_cart

        self.removed_product = ProductDescription()
        self.product_under_work = ProductDescription()

        self.total_price = PriceObject()
        self.sub_total_price = PriceObject()


class ShoppingCartFunctions(ProjectFunction):

    def get_random_product(self, cart_object):
        """
        choose RANDOM product from SHOPPING CART
        fill: cart_object.product_under_work : {"title": "", "price": "", "quantity": ""}
        """
        cart_object.list_of_cart_dom_indexes = self.get_list_of_dom_indexes(products_list_locator=cart_const.LIST_OF_PRODUCTS_xpath)
        random_dom_index = random.choice(cart_object.list_of_cart_dom_indexes)

        cart_object.product_under_work.dom_index = random_dom_index

        cart_object.product_under_work.title = self.get_text_from_locator(
            locator=self.formated_locator(cart_const.PRODUCT_TITLE_xpath, index=random_dom_index))
        cart_object.product_under_work.price = self.get_text_from_locator(
            locator=self.formated_locator(cart_const.PRODUCT_PRICE_xpath, index=random_dom_index))
        cart_object.product_under_work.quantity = int(self.get_value_from_input_field(
            locator=self.formated_locator(cart_const.PRODUCT_QUANTITY_INPUT_FIELD_xpath, index=random_dom_index)))
        self.logger.info(f"Chosen product :  --{cart_object.product_under_work.title}-- with price: --{cart_object.product_under_work.price}--")

    def add_random_products(self, cart_object, adding_amount: int):
        """
        'adding_amount'  -- quantity of products, wanted to add to 'Shopping cart'
        make: add 'adding_amount' products to a shopping cart
        fill: cart_object.list_of_products_in_shopping_cart => [ {"title": "", "price":""}  , ... ]
        """
        while cart_object.current_count_in_cart != cart_object.start_count_in_cart + adding_amount:
            self.open_random_product_category_page()
            current_url = self.driver.current_url
            self.click_add_cart_button_of_random_product(cart_object, current_url)

    def click_add_cart_button_of_random_product(self, cart_object, current_url=""):
        """
        make: on a cart_object category page(with numerous adding_amount of products) choose RANDOM cart_object with a 'Add to cart' button
        fill: cart_object.list_of_products_under_work = [ {"title": "", "price":""} ]
        """
        # create list of dom indexes of "Add to cart' buttons
        cart_object.list_of_add_cart_dom_indexes = self.get_list_of_dom_indexes(
            products_list_locator=prod_page_const.LIST_OF_PRODUCTS_ON_PAGE_xpath,
            condition_list_locator=prod_page_const.LIST_OF_ADD_TO_CART_BUTTONS_ON_PAGE_xpath)
        # remove products dom index from "list_of_add_cart_dom_indexes" and try to add the product to the cart(not allways it's possible)
        while cart_object.list_of_add_cart_dom_indexes:
            random_dom_index = random.choice(cart_object.list_of_add_cart_dom_indexes)
            cart_object.list_of_add_cart_dom_indexes.remove(random_dom_index)

            # if 'add to cart' button exists -- remember 'name' and 'price' and click it
            temp_product = ProductDescription()
            temp_product.title = self.get_text_from_locator(
                locator=self.formated_locator(prod_page_const.LIST_OF_PRODUCT_TITLES_ON_PAGE_xpath, random_dom_index))
            temp_product.price = self.get_text_from_locator(
                locator=self.formated_locator(prod_page_const.LIST_OF_PRODUCT_PRICES_ON_PAGE_xpath, random_dom_index))

            self.driver.find_element(*self.formated_locator(prod_page_const.LIST_OF_ADD_TO_CART_BUTTONS_ON_PAGE_xpath, random_dom_index)).click()

            # after click 'Add to Cart' some products open 'Product page' to clarify details. If happens -- open new 'Category  page'
            time.sleep(1)
            if self.driver.current_url == current_url:
                self.verify_message(locator=cart_const.PRODUCT_HAS_BEEN_ADDED_MESSAGE_xpath,
                                    expected_text=cart_const.PRODUCT_HAS_BEEN_ADDED_MESSAGE_text, comments="above the header")
                self.logger.info(f"Product was added to Shopping cart: --{temp_product.title}--")
                cart_object.list_of_products_in_shopping_cart.append(temp_product)
                cart_object.current_count_in_cart += 1
                return
            else:
                return

    def get_item_quantity_from_top_menu(self, comment="") -> int:
        """ make: READ quantity of products in the 'Shopping cart' in the header . """
        quantity = self.get_text_from_locator(header_const.QUANTITY_OF_PRODUCTS_IN_SHOPPING_CART_xpath)
        int_quantity = int(quantity[1:-1])
        self.logger.info(f"Quantity of products in shopping cart from the header -{comment}- : --{int_quantity}--")
        return int_quantity

    def set_item_quantity_and_click_update(self, cart_object):
        """ make: change cart_object item quantity (Qty.) in the shopping cart and click 'Update...'   """
        quantity_input_field_locator = self.formated_locator(cart_const.PRODUCT_QUANTITY_INPUT_FIELD_xpath,
                                                             index=cart_object.product_under_work.dom_index)

        self.wait_send_keys(locator=quantity_input_field_locator, data=str(cart_object.product_under_work.quantity))
        self.wait_click_ability_and_click(locator=cart_const.UPDATE_BUTTON_xpath)

        self.logger.info(f"EXPECTED new quantity : --{cart_object.product_under_work.quantity}-- ")
        self.logger.info(f"  ACTUAL new quantity : --{self.get_value_from_input_field(locator=quantity_input_field_locator)}-- ")

    def check_presence_of_given_products_inside_shopping_cart(self, cart_object, given_products_list, comment=""):
        self.wait_click_ability_and_click(header_const.SHOPPING_CART_BUTTON_IN_HEADER_id)

        for checking_product in given_products_list:
            if not self.check_presence_of_the_product_inside_shopping_cart(cart_object, checking_product, comment):
                self.logger.info(f"Shopping cart -{comment}- : -{self.get_list_of_texts(list_locator=cart_const.LIST_OF_TITLES_xpath)}-")
                return False
        return True

    def check_presence_of_products_inside_shopping_cart(self, cart_object, comment="") -> bool:
        """make: verify presence of all products from the list: 'cart_object.list_of_products_in_shopping_cart' in the shopping cart"""
        # go to the 'Shopping cart' by click 'Shopping Cart' button in the header
        self.wait_click_ability_and_click(header_const.SHOPPING_CART_BUTTON_IN_HEADER_id)

        for checked_product in cart_object.list_of_products_in_shopping_cart:
            if not self.check_presence_of_the_product_inside_shopping_cart(cart_object=cart_object, checked_product=checked_product, comment=comment):
                return False
        return True

    def check_presence_of_the_product_inside_shopping_cart(self, cart_object, checked_product, comment="") -> bool:
        """ make: check if ONE (checked_product) product presents in the 'Shopping cart'  """
        cart_object.list_of_cart_dom_indexes = self.get_list_of_dom_indexes(products_list_locator=cart_const.LIST_OF_PRODUCTS_xpath)
        for product_dom_index in cart_object.list_of_cart_dom_indexes:
            if checked_product.title == \
                    self.get_text_from_locator(locator=self.formated_locator(cart_const.PRODUCT_TITLE_xpath, product_dom_index)) \
                    and checked_product.price == \
                    self.get_text_from_locator(locator=self.formated_locator(cart_const.PRODUCT_PRICE_xpath, product_dom_index)):
                # self.logger.info(f"EXPECTED product in the 'Shopping cart -{comment}-: --{checked_product.title}--")
                # self.logger.info(
                #     f"  ACTUAL product in the 'Shopping cart -{comment}-: --{self.get_text_from_locator(locator=self.formated_locator(cart_const.PRODUCT_TITLE_xpath, product_dom_index))}--")
                return True
        return False

    def remove_random_products_with_update_button(self, cart_object, removed_amount=1):
        """ choose random product(s), tick it(them), click 'Update...' button"""
        # make list of 'Shopping cart' dom indexes
        self.wait_click_ability_and_click(locator=header_const.SHOPPING_CART_BUTTON_IN_HEADER_id, locator_type=By.ID)
        self.logger.info(f"Shopping cart before removing : -{self.get_list_of_texts(list_locator=cart_const.LIST_OF_TITLES_xpath)}-")
        cart_object.list_of_cart_dom_indexes = self.get_list_of_dom_indexes(products_list_locator=cart_const.LIST_OF_PRODUCTS_xpath)

        for _ in range(removed_amount):
            # get random item and tick next to it
            random_dom_index = random.choice(cart_object.list_of_cart_dom_indexes)
            self.wait_click_ability_and_click(self.formated_locator(cart_const.PRODUCT_REMOVING_CHECK_BOX_xpath, index=random_dom_index))

            removed_item = ProductDescription()
            removed_item.title = cart_object.product_under_work.title = self.get_text_from_locator(
                locator=self.formated_locator(cart_const.PRODUCT_TITLE_xpath, index=random_dom_index))
            removed_item.price = cart_object.product_under_work.price = self.get_text_from_locator(
                locator=self.formated_locator(cart_const.PRODUCT_PRICE_xpath, index=random_dom_index))

            cart_object.removed_products.append(removed_item)

            cart_object.list_of_cart_dom_indexes.remove(random_dom_index)
            self.logger.info(f"Removing product: --{removed_item.title}--")

        # click 'Update...' button
        self.wait_click_ability_and_click(cart_const.UPDATE_BUTTON_xpath)
        self.logger.info(f"Shopping cart after removing : -{self.get_list_of_texts(list_locator=cart_const.LIST_OF_TITLES_xpath)}-")

    def get_total_and_subtotal_data(self, cart_object, comment=""):
        """
        make: remember 'total' product price and 'sub-total' price of the 'Shopping cart'
        fill: cart_object.total_price and cart_object.sub_total_price depends on given key(comment)
        """
        total_price = self.get_text_from_locator(
            locator=self.formated_locator(cart_const.PRODCUT_TOTAL_PRICE_xpath, index=cart_object.product_under_work.dom_index))
        sub_total_price = self.get_text_from_locator(locator=cart_const.SUB_TOTAL_SUM_xpath)

        if comment == "before cart edit":
            cart_object.total_price.before_cart_edit = total_price
            cart_object.sub_total_price.before_cart_edit = sub_total_price
        elif comment == "after cart edit":
            cart_object.total_price.after_cart_edit = total_price
            cart_object.sub_total_price.after_cart_edit = sub_total_price
        else:
            raise AssertionError(f"Wrong key/comment")
        self.logger.info(f"    Total price  -{comment}-: --{total_price}--")
        self.logger.info(f"Sub total price  -{comment}-: --{sub_total_price}--")

    def get_list_of_shopping_cart_products(self, cart_object):
        """ return: list of product items , taken from the 'Shopping cart' page """
        self.wait_click_ability_and_click(button=header_const.SHOPPING_CART_BUTTON_IN_HEADER_id)
        if cart_object.current_count_in_cart == 0:
            self.verify_message(locator=cart_const.EMPTY_CONTENT_class,
                                expected_text=cart_const.EMPTY_CONTENT_text)
            return []
        return self.get_list_of_texts(list_locator=cart_const.LIST_OF_TITLES_xpath)
