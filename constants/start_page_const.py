class ProductCategoryPageConstants:
    # Product category page elements
    LIST_OF_SUBCATEGORY_ON_PAGE_xpath = "//div[@class='sub-category-checking_product_item']/h2/a"  # ["Desktops", " Notebooks", "Accessories"] on page

    LIST_OF_PRODUCT_BREADCRUMB_xpath = "//div[@class='breadcrumb']/ul/li"
    PAGE_TITLE_xpath = "//div[@class='page-title']"
    PAGE_TITLE_class = 'page-title'
    DROP_DOWN_SORT_BY_LIST_xpath = "//div[@class='product-sorting']"
    DROP_DOWN_DISPLAY_PER_PAGE_LIST_xpath = "//div[@class='product-page-size']"
    DROP_DOWN_VIEW_AS_LIST_xpath = "//div[@class='product-viewmode']"
    LIST_OF_PRODUCTS_ON_PAGE_xpath = "//div[@class='item-box']"  # list of products on the page
    LIST_OF_PRODUCTS_ON_PAGE_class = "checking_product_item-box"

    # as so not each product has 'price' or 'adding to cart' button -- lists mentioned below have DIFFERENT length
    ADDING_PART_OF_XPATH_FOR_TITLE = "//h2[@class='product-title']"
    ADDING_PART_OF_XPATH_FOR_ADD_TO_CART_BUTTON = "//input[@value='Add to cart']"
    ADDING_PART_OF_XPATH_FOR_PRICE_BUTTON = "//span[@class='price actual-price']"

    # consequently, to get a definite 'title' -- put [index] 'in the center'
    LIST_OF_PRODUCT_TITLES_ON_PAGE_xpath = f"{LIST_OF_PRODUCTS_ON_PAGE_xpath}" + "[{index}]" + f"{ADDING_PART_OF_XPATH_FOR_TITLE}"
    LIST_OF_ADD_TO_CART_BUTTONS_ON_PAGE_xpath = f"{LIST_OF_PRODUCTS_ON_PAGE_xpath}" + "[{index}]" + f"{ADDING_PART_OF_XPATH_FOR_ADD_TO_CART_BUTTON}"
    LIST_OF_PRODUCT_PRICES_ON_PAGE_xpath = f"{LIST_OF_PRODUCTS_ON_PAGE_xpath}" + "[{index}]" + f"{ADDING_PART_OF_XPATH_FOR_PRICE_BUTTON}"


class ProductPageConstants:
    #       PRODUCT ITEM PAGE
    ADD_TO_CART_BUTTON_ON_PRODUCT_PAGE_xpath = "//input[@class='button-1 add-to-cart-button']"


class GlobalConstants:
    PATH_TO_CHROME_WEBDRIVER = "P:/Pycharm/PycharmProjects/DemoWebShop/drivers/chromedriver.exe"
    PATH_TO_FIREFOX__WEBDRIVER = "P:/Pycharm/PycharmProjects/DemoWebShop/drivers/geckodriver.exe"
    START_PAGE_url = "http://demowebshop.tricentis.com/"
    REGISTER_PAGE_url = f"{START_PAGE_url}register"
    # PRODUCT_SUBCATEGORY_PAGE_url = "http://demowebshop.tricentis.com/{subcategory}"

    REGISTER_BUTTON_IN_HEADER_xpath = "//a[@class='ico-register']"
    REGISTER_BUTTON_IN_HEADER_class = "ico-register"
    LOGIN_BUTTON_IN_HEADER_xpath = "//a[@class='ico-login']"
    LOGOUT_BUTTON_IN_HEADER_xpath = "//a[@class='ico-logout']"
    SHOPPING_CART_BUTTON_IN_HEADER_xpath = "//li[@id='topcartlink']"
    SHOPPING_CART_BUTTON_IN_HEADER_id = 'topcartlink'
    QUANTITY_OF_PRODUCTS_IN_SHOPPING_CART_xpath = "//span[@class='cart-qty']"  # could be seen next to 'Shopping cart' in 'top menu'


# Products and product categories in header
BOOKS_BUTTON_xpath = "//ul[@class='top-menu']//a[@href='/books']"
COMPUTERS_BUTTON_IN_HEADER_xpath = "//ul[@class='top-menu']//a[@href='/computers']"
DESKTOPS_BUTTON_IN_HEADER_xpath = "//ul[@class='top-menu']//a[@href='/desktops']"
NOTEBOOKS_BUTTON_IN_HEADER_xpath = "//ul[@class='top-menu']//a[@href='/notebooks']"
ACCESSORIES_BUTTON_IN_HEADER_xpath = "//ul[@class='top-menu']//a[@href='/accessories']"

ELECTRONICS_BUTTON_IN_HEADER_xpath = "//ul[@class='top-menu']//a[@href='/electronics']"
CAMERA_FOTO_BUTTON_IN_HEADER_xpath = "//ul[@class='top-menu']//a[@href='/camera-photo']"
CELL_PHONES_BUTTON_IN_HEADER_xpath = "//ul[@class='top-menu']//a[@href='/cell-phones']"

APPAREL_AND_SHOES_BUTTON_IN_HEADER_xpath = "//ul[@class='top-menu']//a[@href='/apparel-shoes']"
DIGITAL_DOWNLOADS_BUTTON_IN_HEADER_xpath = "//ul[@class='top-menu']//a[@href='/digital-downloads']"
JEWELRY_BUTTON_IN_HEADER_xpath = "//ul[@class='top-menu']//a[@href='/jewelry']"
GIFT_CARDS_BUTTON_IN_HEADER_xpath = "//ul[@class='top-menu']//a[@href='/gift-cards']"

product_dict = {"Books": {"mouse_movement": ["Books"], "xpath": BOOKS_BUTTON_xpath},

                "Computers": {"mouse_movement": ["Computers"], "xpath": COMPUTERS_BUTTON_IN_HEADER_xpath,
                              "sub_menu": ["Desktops", "Notebooks", "Accessories"]},
                # "Desktops": {"mouse_movement": ["Computers", "Desktops"], "xpath": DESKTOPS_BUTTON_IN_HEADER_xpath}, # here is a bug
                "Notebooks": {"mouse_movement": ["Computers", "Notebooks"], "xpath": NOTEBOOKS_BUTTON_IN_HEADER_xpath},
                "Accessories": {"mouse_movement": ["Computers", "Accessories"], "xpath": ACCESSORIES_BUTTON_IN_HEADER_xpath},

                "Electronics": {"mouse_movement": ["Electronics"], "xpath": ELECTRONICS_BUTTON_IN_HEADER_xpath,
                                "sub_menu": ["Camera,photo", "Cell phones"]},
                # "Camera,photo": {"mouse_movement": ["Electronics", "Camera,photo"], "xpath": CAMERA_FOTO_BUTTON_IN_HEADER_xpath},
                "Cell phones": {"mouse_movement": ["Electronics", "Cell phones"], "xpath": CELL_PHONES_BUTTON_IN_HEADER_xpath},

                "Apparel & Shoes": {"mouse_movement": ["Apparel & Shoes"], "xpath": APPAREL_AND_SHOES_BUTTON_IN_HEADER_xpath},
                "Digital downloads": {"mouse_movement": ["Digital downloads"], "xpath": DIGITAL_DOWNLOADS_BUTTON_IN_HEADER_xpath}}


# "Jewelry": {"mouse_movement": ["Jewelry"], "xpath": JEWELRY_BUTTON_IN_HEADER_xpath},
# "Gift Cards": {"mouse_movement": ["Gift Cards"], "xpath": GIFT_CARDS_BUTTON_IN_HEADER_xpath}}


class Product:
    def __init__(self, product_name):
        self.__product_name = ""
        self.product_name = product_name

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, product_name):  # product_name == "Desktops"
        self.__product_name = product_name
        for item in product_dict.keys():
            if item == product_name:  # checking_product_item = "Desktops"
                self.mouse_movement_names_list = product_dict[item]["mouse_movement"]  # ["Computers", "Desktops"],
                self.product_sub_menu_list = product_dict[item].get("sub_menu")  # ["Desktops", "Notebooks", "Accessories"]
                self.mouse_movement_locators_list = [product_dict[name]["xpath"] for name in product_dict[product_name]["mouse_movement"]]
                break
        else:
            # self.logger.info( "There is no such element -{product_name}-")
            self.mouse_movement_names_list = False
