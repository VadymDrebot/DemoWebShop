# Category category page elements
from selenium.webdriver.common.by import By

LIST_OF_SUBCATEGORY_ON_PAGE_xpath = (By.XPATH, "//div[@class='sub-category-grid']//h2/a")  # ["Desktops"," Notebooks","Accessories"]

LIST_OF_PRODUCT_BREADCRUMB_xpath = (By.XPATH, "//div[@class='breadcrumb']/ul/li")
PAGE_TITLE_xpath = (By.XPATH, "//div[@class='page-title']/h1")
PAGE_TITLE_class = (By.CLASS_NAME, 'page-title')

DROP_DOWN_SORT_BY_LIST_BLOCK_xpath = (By.XPATH, "//div[@class='product-sorting']")  # name of the drop down list
DROP_DOWN_SORT_BY_LIST_xpath = (By.XPATH, "//div[@class='product-sorting']//option")  # all values from drop down list
DROP_DOWN_SORT_BY_SELECT_BLOCK_xpath = (By.XPATH, "//div[@class='product-sorting']/select")  # SELECT block of values (OPTION tags)

DROP_DOWN_DISPLAY_PER_PAGE_BLOCK_xpath = (By.XPATH, "//div[@class='product-page-size']")
DROP_DOWN_DISPLAY_PER_PAGE_SELECT_BLOCK_xpath = (By.XPATH, "//div[@class='product-page-size']/select")
# DROP_DOWN_DISPLAY_PER_PAGE_LIST_xpath = (By.XPATH, "//div[@class='product-page-size']//option")

DROP_DOWN_VIEW_AS_BLOCK_xpath = (By.XPATH, "//div[@class='product-viewmode']")
DROP_DOWN_VIEW_AS_SELECT_BLOCK_xpath = (By.XPATH, "//div[@class='product-viewmode']/select")
# DROP_DOWN_VIEW_AS_LIST_xpath = (By.XPATH, "//div[@class='product-viewmode']//option")

FILTER_BY_PRICE_BLOCK_xpath = (By.XPATH, "//div[@class='product-filters price-range-filter']")
FILTER_BY_PRICE_LIST_OF_VALUES_xpath = (By.XPATH, "//ul[@class='price-range-selector']/li/a")
REMOVE_FILTER_BUTTON = (By.XPATH, "//a[@class='remove-price-range-filter']")

LIST_OF_PRODUCTS_ON_PAGE_GRID_VIEW_xpath_as_string = "//div[@class='product-grid']"
LIST_OF_PRODUCTS_ON_PAGE_GRID_VIEW_xpath = (By.XPATH, LIST_OF_PRODUCTS_ON_PAGE_GRID_VIEW_xpath_as_string)
# LIST_OF_PRODUCTS_ON_PAGE_class = "checking_product_item-box"
LIST_OF_PRODUCTS_ON_PAGE_LIST_VIEW_xpath = (By.XPATH, "//div[@class='product-list']")

# could be as several or no one as well on the page
PRODUCT_TITLE = "//h2[@class='product-title']"
ADD_TO_CART_BUTTON = "//input[@value='Add to cart']"
PRICE_BUTTON = "//span[@class='price actual-price']"

# consequently, to get a definite 'title' -- put [index] 'in the center'
LIST_OF_PRODUCT_TITLES_ON_PAGE_xpath = (By.XPATH, f"{LIST_OF_PRODUCTS_ON_PAGE_GRID_VIEW_xpath_as_string}" + "[{index}]" + f"{PRODUCT_TITLE}")
LIST_OF_ADD_TO_CART_BUTTONS_ON_PAGE_xpath = (
    By.XPATH, (f"{LIST_OF_PRODUCTS_ON_PAGE_GRID_VIEW_xpath_as_string}" + "[{index}]" + f"{ADD_TO_CART_BUTTON}"))
LIST_OF_PRODUCT_PRICES_ON_PAGE_xpath = (By.XPATH, f"{LIST_OF_PRODUCTS_ON_PAGE_GRID_VIEW_xpath_as_string}" + "[{index}]" + f"{PRICE_BUTTON}")

LIST_OF_TITLES = (By.XPATH, "//div[@class='item-box']//h2[@class='product-title']")
LIST_OF_PRICES = (By.XPATH, "//div[@class='item-box']//span[@class='price actual-price']")
# class ProductPageConstants:
#       PRODUCT ITEM PAGE
ADD_TO_CART_BUTTON_ON_PRODUCT_PAGE_xpath = (By.XPATH, "//input[@class='button-1 add-to-cart-button']")
