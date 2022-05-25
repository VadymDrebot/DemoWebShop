from selenium.webdriver.common.by import By

REGISTER_BUTTON_IN_HEADER_xpath = (By.XPATH, "//a[@class='ico-register']")
REGISTER_BUTTON_IN_HEADER_class = (By.CLASS_NAME, "ico-register")

LOGIN_BUTTON_IN_HEADER_xpath = (By.XPATH, "//a[@class='ico-login']")
# LOGIN_BUTTON_IN_HEADER_xpath = "//a[@class='ico-login']"
LOGOUT_BUTTON_IN_HEADER_xpath = (By.XPATH, "//a[@class='ico-logout']")

SHOPPING_CART_BUTTON_IN_HEADER_xpath = (By.XPATH, "//li[@id='topcartlink']")
SHOPPING_CART_BUTTON_IN_HEADER_id = (By.ID, 'topcartlink')
USERPROMPT_SHOPPING_CART_IN_HEADER_xpath = (By.XPATH, "//div[@class='count']")
USERPROMPT_EMPTY_SHOPPING_CART_text = "You have no items in your shopping cart."
QUANTITY_OF_PRODUCTS_IN_SHOPPING_CART_xpath = (By.XPATH, "//span[@class='cart-qty']")  # could be seen next to 'Shopping cart' in 'top menu'

# Products and cart_object categories in header
BOOKS_BUTTON_xpath = (By.XPATH, "//ul[@class='top-menu']//a[@href='/books']")
COMPUTERS_BUTTON_IN_HEADER_xpath = (By.XPATH, "//ul[@class='top-menu']//a[@href='/computers']")
DESKTOPS_BUTTON_IN_HEADER_xpath = (By.XPATH, "//ul[@class='top-menu']//a[@href='/desktops']")
NOTEBOOKS_BUTTON_IN_HEADER_xpath = (By.XPATH, "//ul[@class='top-menu']//a[@href='/notebooks']")
ACCESSORIES_BUTTON_IN_HEADER_xpath = (By.XPATH, "//ul[@class='top-menu']//a[@href='/accessories']")

ELECTRONICS_BUTTON_IN_HEADER_xpath = (By.XPATH, "//ul[@class='top-menu']//a[@href='/electronics']")
CAMERA_FOTO_BUTTON_IN_HEADER_xpath = (By.XPATH, "//ul[@class='top-menu']//a[@href='/camera-photo']")
CELL_PHONES_BUTTON_IN_HEADER_xpath = (By.XPATH, "//ul[@class='top-menu']//a[@href='/cell-phones']")

APPAREL_AND_SHOES_BUTTON_IN_HEADER_xpath = (By.XPATH, "//ul[@class='top-menu']//a[@href='/apparel-shoes']")
DIGITAL_DOWNLOADS_BUTTON_IN_HEADER_xpath = (By.XPATH, "//ul[@class='top-menu']//a[@href='/digital-downloads']")
JEWELRY_BUTTON_IN_HEADER_xpath = (By.XPATH, "//ul[@class='top-menu']//a[@href='/jewelry']")
GIFT_CARDS_BUTTON_IN_HEADER_xpath = (By.XPATH, "//ul[@class='top-menu']//a[@href='/gift-cards']")

BOOKS = {"mouse_movement": ["Books"], "xpath_for_click": BOOKS_BUTTON_xpath}

categories = {"Books": {"mouse_movement": ["Books"], "xpath_for_click": BOOKS_BUTTON_xpath},

              "Computers": {"mouse_movement": ["Computers"], "xpath_for_click": COMPUTERS_BUTTON_IN_HEADER_xpath,
                            "sub_menu": ["Desktops", "Notebooks", "Accessories"]},
              "Desktops": {"mouse_movement": ["Computers", "Desktops"], "xpath_for_click": DESKTOPS_BUTTON_IN_HEADER_xpath},
              "Notebooks": {"mouse_movement": ["Computers", "Notebooks"], "xpath_for_click": NOTEBOOKS_BUTTON_IN_HEADER_xpath},
              "Accessories": {"mouse_movement": ["Computers", "Accessories"], "xpath_for_click": ACCESSORIES_BUTTON_IN_HEADER_xpath},

              "Electronics": {"mouse_movement": ["Electronics"], "xpath_for_click": ELECTRONICS_BUTTON_IN_HEADER_xpath,
                              "sub_menu": ["Camera, photo", "Cell phones"]},
              "Camera, photo": {"mouse_movement": ["Electronics", "Camera, photo"], "xpath_for_click": CAMERA_FOTO_BUTTON_IN_HEADER_xpath},
              "Cell phones": {"mouse_movement": ["Electronics", "Cell phones"], "xpath_for_click": CELL_PHONES_BUTTON_IN_HEADER_xpath},

              "Apparel & Shoes": {"mouse_movement": ["Apparel & Shoes"], "xpath_for_click": APPAREL_AND_SHOES_BUTTON_IN_HEADER_xpath},
              "Digital downloads": {"mouse_movement": ["Digital downloads"], "xpath_for_click": DIGITAL_DOWNLOADS_BUTTON_IN_HEADER_xpath},
              "Jewelry": {"mouse_movement": ["Jewelry"], "xpath_for_click": JEWELRY_BUTTON_IN_HEADER_xpath},
              "Gift Cards": {"mouse_movement": ["Gift Cards"], "xpath_for_click": GIFT_CARDS_BUTTON_IN_HEADER_xpath}}
