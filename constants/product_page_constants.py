# Category category page elements
from selenium.webdriver.common.by import By

LIST_OF_SUBCATEGORY_ON_PAGE_xpath = (By.XPATH, "//div[@class='sub-category-grid']//h2/a")  # ["Desktops"," Notebooks","Accessories"]

LIST_OF_PRODUCT_BREADCRUMB_xpath = (By.XPATH, "//div[@class='breadcrumb']/ul/li")
PAGE_TITLE_xpath = (By.XPATH, "//div[@class='page-title']/h1")
PAGE_TITLE_class = 'page-title'
DROP_DOWN_SORT_BY_LIST_xpath = (By.XPATH, "//div[@class='product-sorting']/span")
DROP_DOWN_DISPLAY_PER_PAGE_LIST_xpath = (By.XPATH, "//div[@class='product-page-size']/span")
DROP_DOWN_VIEW_AS_LIST_xpath = (By.XPATH, "//div[@class='product-viewmode']/span")
LIST_OF_PRODUCTS_ON_PAGE_xpath = (By.XPATH, "//div[@class='product-grid']/div[@class='item-box']")  # list of products on the page(need so long)
# LIST_OF_PRODUCTS_ON_PAGE_class = "checking_product_item-box"

# as so not each cart_object has 'price' or 'adding to cart' button -- lists mentioned below have DIFFERENT length
ADDING_PART_OF_XPATH_FOR_TITLE = "//h2[@class='product-title']"
ADDING_PART_OF_XPATH_FOR_ADD_TO_CART_BUTTON = "//input[@value='Add to cart']"
ADDING_PART_OF_XPATH_FOR_PRICE_BUTTON = "//span[@class='price actual-price']"

# consequently, to get a definite 'title' -- put [index] 'in the center'
LIST_OF_PRODUCT_TITLES_ON_PAGE_xpath = (By.XPATH, f"{LIST_OF_PRODUCTS_ON_PAGE_xpath}" + "[{index}]" + f"{ADDING_PART_OF_XPATH_FOR_TITLE}")
LIST_OF_ADD_TO_CART_BUTTONS_ON_PAGE_xpath = f"{LIST_OF_PRODUCTS_ON_PAGE_xpath}" + "[{index}]" + f"{ADDING_PART_OF_XPATH_FOR_ADD_TO_CART_BUTTON}"
LIST_OF_PRODUCT_PRICES_ON_PAGE_xpath = f"{LIST_OF_PRODUCTS_ON_PAGE_xpath}" + "[{index}]" + f"{ADDING_PART_OF_XPATH_FOR_PRICE_BUTTON}"

# class ProductPageConstants:
#       PRODUCT ITEM PAGE
ADD_TO_CART_BUTTON_ON_PRODUCT_PAGE_xpath = "//input[@class='button-1 add-to-cart-button']"
