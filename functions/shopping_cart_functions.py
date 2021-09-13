import random

from selenium.webdriver.common.by import By

from constants.shopping_cart_constants import ShoppingCartConstants
from constants.start_page_const import ProductCategoryPageConstants
from functions.common_functions import CommonFunctions


class ShoppingCartFunctions(CommonFunctions, ProductCategoryPageConstants, ShoppingCartConstants):

    def make_list_of_dom_indexes(self, product, list_locator, locator_type=By.XPATH):
        """ 'list_locator' -- list of items on a page(shopping cart).
        Return: list of DOM indexes(from 1 to ...) into the 'product' object"""
        product_amount_on_page = len(self.driver.find_elements(by=locator_type, value=list_locator))  # f.e. len=5
        product.list_of_dom_indexes = [index for index in range(1, product_amount_on_page + 1)]  # lst= [1,2,3,4,5]
        return product

    def choose_random_product_in_shopping_cart(self, product):
        """ choose RANDOM product from SHOPPING CART
        Return: {"title": "", "price": "", "dom index": ""} inside the 'product' object """
        random_dom_index = random.choice(product.list_of_cart_dom_indexes)
        product.product_in_process["dom index"] = random_dom_index
        product.product_in_process["title"] = self.get_text_from_locator(
            locator=self.PRODUCT_TITLE_IN_SHOPPING_CART_xpath.format(index=random_dom_index))
        product.product_in_process["price"] = self.get_text_from_locator(
            locator=self.PRODUCT_PRICE_IN_SHOPPING_CART_xpath.format(index=random_dom_index))
        return product

    def add_some_products_to_shopping_cart(self, product, amount):
        """ 'amount'  -- quantity of products, wanted to add to 'Shopping cart'
        Make: add 'amount'(int) products to a shopping cart, and:
        Return: list - 'list_of_cart_dom_indexes' with the DOM indexes inside the 'product' object """
        for i in range(1, amount + 1):
            self.open_random_product_category_page()
            self.click_add_cart_of_random_product(product)
            product.list_of_cart_dom_indexes.append(i)

    def click_add_cart_of_random_product(self, product):
        """ on a product category page(with numerous amount of products) choose RANDOM product with a 'Add to cart' button
        Make: add {"title": "", "price":""} to the list 'list_of_products_in_shopping_cart' . Result: [{"title": "", "price":""}, ...]  """
        self.make_list_of_dom_indexes(product, list_locator=self.LIST_OF_PRODUCTS_ON_PAGE_xpath)

        while product.list_of_dom_indexes:
            random_dom_index = random.choice(product.list_of_dom_indexes)  # choose random DOM-index , f.e. '2'
            product.list_of_dom_indexes.remove(random_dom_index)  # lst= [1,3,4,5]

            # if 'add to cart' button exists -- remember 'name' and 'price' and click it
            if self.verify_presence_of_element(locator=self.LIST_OF_ADD_TO_CART_BUTTONS_ON_PAGE_xpath.format(index=random_dom_index)):
                title_from_dom = self.get_text_from_locator(locator=self.LIST_OF_PRODUCT_TITLES_ON_PAGE_xpath.format(index=random_dom_index))
                price_from_dom = self.get_text_from_locator(locator=self.LIST_OF_PRODUCT_PRICES_ON_PAGE_xpath.format(index=random_dom_index))

                self.driver.find_element(by=By.XPATH,
                                         value=self.LIST_OF_ADD_TO_CART_BUTTONS_ON_PAGE_xpath.format(index=random_dom_index)).click()

                try:
                    # after click 'Add to Cart' some products open 'Product page' to clarify details. If happens -- open new 'Product category page'
                    self.verify_message(locator=self.PRODUCT_HAS_BEEN_ADDED_MESSAGE_xpath,
                                        expected_text=self.PRODUCT_HAS_BEEN_ADDED_MESSAGE_text)
                    product.current_count_in_cart += 1
                    # write 'name' and 'price' into the list 'product.list_of_products_in_shopping_cart' as a dictionary
                    product.temporary_dic = {"title": title_from_dom, "price": price_from_dom}
                    self.logger.info(f"Product was added to Shopping cart with title: -{title_from_dom}- and price: -{price_from_dom}-")
                    return product
                except AssertionError:
                    self.open_random_product_category_page()
                    self.click_add_cart_of_random_product(product)

                    # if self.verify_message(locator=self.PRODUCT_HAS_BEEN_ADDED_MESSAGE_xpath,
                #                        expected_text=self.PRODUCT_HAS_BEEN_ADDED_MESSAGE_text):
                #     product.current_count_in_cart += 1
                #     # write 'name' and 'price' into the list 'product.list_of_products_in_shopping_cart' as a dictionary
                #     product.temporary_dic = {"title": title_from_dom, "price": price_from_dom}
                #     self.logger.info(f"Product was added to Shopping cart with title: -{title_from_dom}- and price: -{price_from_dom}-")
                # return product
        else:
            # if there is no item with 'add to cart' button -- open new page
            self.open_random_product_category_page()
            self.click_add_cart_of_random_product(product)

    def get_item_quantity_from_top_menu_shopping_cart(self):
        """ READ quantity of products in the 'shopping cart' in the 'top menu' .
         Return: string in format : '(int)'  . F.e.: (2)"""
        quantity = self.get_text_from_locator(locator=self.QUANTITY_OF_PRODUCTS_IN_SHOPPING_CART_xpath)
        int_quantity = int(quantity[1:-1])
        self.logger.info(f"Quantity of products in shopping cart from top menu : -{int_quantity}-")
        return int_quantity

    def set_item_quantity_in_shopping_cart(self, product, action, action_parameter):
        """
        Make: change product item quantity (Qty.) in the shopping cart
        Params: 'action' -- 'increase' or 'decrease' , 'action_parameter' -- amount(int) for 'action' """
        old_value = int(self.get_value_from_input_field(
            locator=self.PRODUCT_QUANTITY_INPUT_FIELD_xpath.format(index=product.product_in_process["dom index"])))
        if action == "increase":
            new_value = old_value + action_parameter
        elif action == "decrease":
            new_value = old_value - action_parameter
        else:
            raise ValueError("Wrong 'action' data")
        self.wait_send_keys(locator=self.PRODUCT_QUANTITY_INPUT_FIELD_xpath.format(index=product.product_in_process["dom index"]),
                            data=f"{new_value}")
        self.logger.info(f"New quantity of a chosen product: -{new_value}-")
        self.wait_click_ability_and_click(locator=self.UPDATE_SHOPPING_CART_BUTTON_name, locator_type=By.NAME)

    def check_presence_of_the_product_inside_shopping_cart(self, product):
        """ Check if ONE(product.product_in_process) product presents in 'shopping cart':
        Return: True if presents,  False -- if not presents"""
        for product_dom_index in product.list_of_cart_dom_indexes:
            title_from_dom = self.get_text_from_locator(locator=self.PRODUCT_TITLE_IN_SHOPPING_CART_xpath.format(index=product_dom_index))
            if title_from_dom == product.product_in_process["title"]:
                # verify 'price' only if name was found in shopping cart
                price_from_dom = self.get_text_from_locator(locator=self.PRODUCT_PRICE_IN_SHOPPING_CART_xpath.format(index=product_dom_index))
                if price_from_dom == product.product_in_process["price"]:
                    # self.logger.info(f"title: -{title_from_dom}- , price: -{price_from_dom}-")
                    return True
        else:
            return False

    def verify_presence_of_products_inside_shopping_cart(self, product):
        """ verify(assert) presence of all products from 'product.list_of_products_in_shopping_cart' in the shopping cart"""
        # go to the 'shopping cart' (click 'Shopping Cart' button in top menu
        self.wait_click_ability_and_click(locator=self.SHOPPING_CART_BUTTON_IN_HEADER_id, locator_type=By.ID)

        for product.product_in_process in product.list_of_products_in_shopping_cart:
            assert self.check_presence_of_the_product_inside_shopping_cart(product), f"-{product.product_in_process['title']}- not in the cart"
            self.logger.info(f"Product -{product.product_in_process['title']}- presents in Shopping cart")

    def remove_random_product_from_shopping_cart(self, product):
        """ Make: choose RANDOM product in the shopping cart, tick next to it, click 'Update shopping cart'
        Return: title of the removed item in 'product.product_in_process["title"]' for further actions"""
        # tick the removing item
        self.make_list_of_dom_indexes(product, list_locator=self.LIST_OF_PRODUCTS_IN_SHOPPING_CART_path)
        random_dom_index = random.choice(product.list_of_cart_dom_indexes)  # choose random DOM-index , f.e. '2'
        self.wait_click_ability_and_click(locator=self.PRODUCT_REMOVING_CHECK_BOX_IN_SHOPPING_CART_xpath.format(index=random_dom_index))

        # remember removing item
        product.product_in_process["title"] = self.get_text_from_locator(
            locator=self.PRODUCT_TITLE_IN_SHOPPING_CART_xpath.format(index=random_dom_index))
        self.logger.info(f"removing_product_title: -{product.product_in_process['title']}-")

        # click update
        self.wait_click_ability_and_click(locator_type=By.NAME, locator=self.UPDATE_SHOPPING_CART_BUTTON_name)

    def get_total_and_subtotal_data(self, product, time):
        """ Make: remember 'total' product price and 'sub-total' price of the Shopping cart
        Params: time -- 'before cart edit' or 'after cart edit'
        Return: filling the value in the total_editing_product_price = {"before cart edit": "", "after cart edit": ""} depends on given key(time)"""
        product.total_editing_product_price[time] = self.get_text_from_locator(
            locator=self.PRODCUT_TOTAL_PRICE_xpath.format(index=product.product_in_process["dom index"]))
        product.sub_total_price[time] = self.get_text_from_locator(locator=self.SUB_TOTAL_SUM_OF_SHOPPING_CART)
        self.logger.info(f"Total price for chosen product-{time}-: -{product.total_editing_product_price[time]}-")
        self.logger.info(f"Sub total price in the Shopping cart-{time}-: -{product.sub_total_price[time]}-")

    # def remember_all_products_in_shopping_cart(self,product):
