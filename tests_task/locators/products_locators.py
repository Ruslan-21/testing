from selenium.webdriver.common.by import By

class ProductsLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input.search-keyword")
    PRODUCTS = (By.CSS_SELECTOR, "div.products div.product")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h4.product-name")
    QUANTITY_INPUT = (By.CSS_SELECTOR, "input.quantity")
    INCREMENT_BUTTON = (By.CSS_SELECTOR, "a.increment")
    ADD_BUTTON = (By.CSS_SELECTOR, "button[type='button']")
    CART_ICON = (By.CSS_SELECTOR, "img[alt='Cart']")
