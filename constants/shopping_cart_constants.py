from constants import global_constants as global_const

SHOPPING_CART_url = f"{global_const.START_PAGE_url}cart"



PAGE_TITLE_SHOPPING_CART_text = "Shopping cart"


SHOPPING_CART_EMPTY_CONTENT_class="order-summary-content"
SHOPPING_CART_EMPTY_CONTENT_text = "Your Shopping Cart is empty!"

# notification in the top of the page
PRODUCT_HAS_BEEN_ADDED_MESSAGE_xpath = "//div/p[@class='content']"
PRODUCT_HAS_BEEN_ADDED_MESSAGE_text = "The product has been added to your shopping cart"

# inside the shopping cart
LIST_OF_PRODUCTS_IN_SHOPPING_CART_xpath = "//tr[@class='cart-item-row']"
PRODUCT_TITLE_IN_SHOPPING_CART_xpath = f"{LIST_OF_PRODUCTS_IN_SHOPPING_CART_xpath}" + "[{index}]//a[@class='product-name']"
PRODUCT_PRICE_IN_SHOPPING_CART_xpath = f"{LIST_OF_PRODUCTS_IN_SHOPPING_CART_xpath}" + "[{index}]//span[@class='product-unit-price']"
PRODUCT_REMOVING_CHECK_BOX_IN_SHOPPING_CART_xpath = f"{LIST_OF_PRODUCTS_IN_SHOPPING_CART_xpath}" + "[{index}]//input[@name='removefromcart']"
PRODUCT_QUANTITY_INPUT_FIELD_xpath = f"{LIST_OF_PRODUCTS_IN_SHOPPING_CART_xpath}" + "[{index}]//input[@class='qty-input']"
PRODCUT_TOTAL_PRICE_xpath = f"{LIST_OF_PRODUCTS_IN_SHOPPING_CART_xpath}" + "[{index}]//span[@class='product-subtotal']"

LIST_OF_TITLES_IN_SHOPPING_CART_xpath = "//tr[@class='cart-item-row']//a[@class='product-name']"
SUB_TOTAL_SUM_OF_SHOPPING_CART = "//tbody/tr[1]//span[@class='product-price']" # before 'shipping' and 'tax'
UPDATE_SHOPPING_CART_BUTTON_name = "updatecart"
