from selenium.webdriver.common.by import By
from constants import global_constants as global_const

SHOPPING_CART_url = f"{global_const.START_PAGE_url}cart"

PAGE_TITLE_text = "Shopping cart"

EMPTY_CONTENT_class = (By.CLASS_NAME, "order-summary-content")
EMPTY_CONTENT_text = "Your Shopping Cart is empty!"

# notification in the top of the page
PRODUCT_HAS_BEEN_ADDED_MESSAGE_xpath = (By.XPATH, "//div/p[@class='content']")
PRODUCT_HAS_BEEN_ADDED_MESSAGE_text = "The product has been added to your shopping cart"

# inside the shopping cart
LIST_OF_PRODUCTS_xpath = (By.XPATH, "//tr[@class='cart-item-row']")
PRODUCT_TITLE_xpath = (By.XPATH, f"{LIST_OF_PRODUCTS_xpath}" + "[{index}]//a[@class='product-name']")
PRODUCT_PRICE_xpath = (By.XPATH, f"{LIST_OF_PRODUCTS_xpath}" + "[{index}]//span[@class='product-unit-price']")
PRODUCT_REMOVING_CHECK_BOX_xpath = (By.XPATH, f"{LIST_OF_PRODUCTS_xpath}" + "[{index}]//input[@name='removefromcart']")
PRODUCT_QUANTITY_INPUT_FIELD_xpath = (By.XPATH, f"{LIST_OF_PRODUCTS_xpath}" + "[{index}]//input[@class='qty-input']")
PRODCUT_TOTAL_PRICE_xpath = (By.XPATH, f"{LIST_OF_PRODUCTS_xpath}" + "[{index}]//span[@class='product-subtotal']")

LIST_OF_TITLES_xpath = (By.XPATH, "//tr[@class='cart-item-row']//a[@class='product-name']")
SUB_TOTAL_SUM_xpath = (By.XPATH, "//tbody/tr[1]//span[@class='product-price']")  # before 'shipping' and 'tax'
UPDATE_BUTTON_name = "updatecart"
