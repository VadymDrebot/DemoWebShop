class ShoppingCartConstants:
    # SHOPPING_CART_url = f"{START_PAGE_url}cart"

    DROPDOWN_MINI_SHOPPING_CART_IN_TOP_MENU_xpath = "//div[@class='count']"
    DROPDOWN_EMPTY_MINI_SHOPPING_CART_text = "You have no items in your shopping cart."

    PAGE_TITLE_SHOPPING_CART_text = "Shopping cart"

    SHOPPING_CART_EMPTY_CONTENT_text = "Your Shopping Cart is empty!"

    # notification in the top of the page
    PRODUCT_HAS_BEEN_ADDED_MESSAGE_xpath = "//div/p[@class='content']"
    PRODUCT_HAS_BEEN_ADDED_MESSAGE_text = "The product has been added to your shopping cart"

    # inside the shopping cart
    LIST_OF_PRODUCTS_IN_SHOPPING_CART_path = "//tr[@class='cart-item-row']"
    PRODUCT_TITLE_IN_SHOPPING_CART_xpath = f"{LIST_OF_PRODUCTS_IN_SHOPPING_CART_path}" + "[{index}]//a[@class='product-name']"
    PRODUCT_PRICE_IN_SHOPPING_CART_xpath = f"{LIST_OF_PRODUCTS_IN_SHOPPING_CART_path}" + "[{index}]//span[@class='product-unit-price']"
    PRODUCT_REMOVING_CHECK_BOX_IN_SHOPPING_CART_xpath = f"{LIST_OF_PRODUCTS_IN_SHOPPING_CART_path}" + "[{index}]//input[@name='removefromcart']"
    PRODUCT_QUANTITY_INPUT_FIELD_xpath = f"{LIST_OF_PRODUCTS_IN_SHOPPING_CART_path}" + "[{index}]//input[@class='qty-input']"
    PRODCUT_TOTAL_PRICE_xpath = f"{LIST_OF_PRODUCTS_IN_SHOPPING_CART_path}" + "[{index}]//span[@class='product-subtotal']"

    LIST_OF_TITLES_IN_SHOPPING_CART_xpath = "//tr[@class='cart-item-row']//a[@class='product-name']"
    SUB_TOTAL_SUM_OF_SHOPPING_CART = "//tbody/tr[1]//span[@class='product-price']"
    UPDATE_SHOPPING_CART_BUTTON_name = "updatecart"


class NewShoppingCart:
    def __init__(self, start_product_count=0, current_product_count=0):
        self.__temporary_dic = {}
        self.list_of_products_in_shopping_cart = []  # each element will be : {"title": "", "price": "", "dom index": ""}
        self.start_count_in_cart = start_product_count
        self.current_count_in_cart = current_product_count

        self.total_editing_product_price = {"before cart edit": "", "after cart edit": ""}
        self.sub_total_price = {"before cart edit": "", "after cart edit": ""}

        self.product_in_process = {"title": "", "price": "", "dom index": ""}

        self.list_of_cart_dom_indexes = []

    @property
    def temporary_dic(self):
        return self.__temporary_dic

    @temporary_dic.setter
    def temporary_dic(self, temporary_dic):
        """ 'temporary_dic' """
        self.list_of_products_in_shopping_cart.append(temporary_dic)


class ExistingShoppingCart:
    def __init__(self, start_product_count=0, current_product_count=0):
        self.__temporary_dic = {}
        self.list_of_products_in_shopping_cart = []  # each element will be : {"title": "", "price": "", "dom index": ""}
        self.start_count_in_cart = start_product_count
        self.current_count_in_cart = current_product_count

        self.total_editing_product_price = {"before cart edit": "", "after cart edit": ""}
        self.sub_total_price = {"before cart edit": "", "after cart edit": ""}

        self.product_in_process = {"title": "", "price": "", "dom index": ""}

        self.list_of_cart_dom_indexes = []

    @property
    def temporary_dic(self):
        return self.__temporary_dic

    @temporary_dic.setter
    def temporary_dic(self, temporary_dic):
        """ 'temporary_dic' """
        self.list_of_products_in_shopping_cart.append(temporary_dic)
