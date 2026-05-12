

class InventoryPage:

    burger_menu_btn = "#react-burger-menu-btn"
    logout_btn = "#logout_sidebar_link"

    add_to_cart_btn = '[data-test="add-to-cart-sauce-labs-backpack"]'
    cart_badge = ".shopping_cart_badge"
    cart_btn = ".shopping_cart_link"

    sort_dropdown = '[data-test="product-sort-container"]'
    product_names = ".inventory_item_name"
    product_prices = ".inventory_item_price"

    twitter_link = ".social_twitter a"
    facebook_link = ".social_facebook a"
    linkedin_link = ".social_linkedin a"

    def __init__(self, page):
        self.page = page

    # BURGER MENU

    def open_burger_menu(self):
        self.page.locator(self.burger_menu_btn).wait_for(state="attached")
        self.page.locator(self.burger_menu_btn).click()

    def click_logout(self):
        self.page.locator(self.logout_btn).wait_for(state="visible")
        self.page.locator(self.logout_btn).click()

    # LOGIN CHECKS

    def is_login_page_opened(self):
        return "saucedemo.com" in self.page.url

    def username_field_empty(self):
        return self.page.input_value("#user-name") == ""

    def password_field_empty(self):
        return self.page.input_value("#password") == ""

    # CART

    def add_product_to_cart(self):
        self.page.locator(self.add_to_cart_btn).click()

    def cart_counter(self):
        return self.page.locator(self.cart_badge).inner_text()

    def open_cart(self):
        self.page.locator(self.cart_btn).click()

    def cart_product_name(self):
        return self.page.locator(self.product_names).inner_text()

    # SORTING

    def choose_sorting(self, value):
        self.page.locator(self.sort_dropdown).select_option(value)

    def get_product_names(self):
        return self.page.locator(self.product_names).all_inner_texts()

    def get_product_prices(self):
        prices = self.page.locator(self.product_prices).all_inner_texts()

        return [
            float(price.replace("$", ""))
            for price in prices
        ]

    # FOOTER

    def open_twitter(self):
        with self.page.context.expect_page() as new_page:
            self.page.locator(self.twitter_link).click()
        return new_page.value

    def open_facebook(self):
        with self.page.context.expect_page() as new_page:
            self.page.locator(self.facebook_link).click()
        return new_page.value

    def open_linkedin(self):
        with self.page.context.expect_page() as new_page:
            self.page.locator(self.linkedin_link).click()
        return new_page.value