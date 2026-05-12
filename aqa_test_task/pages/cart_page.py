class CartPage:

    checkout_btn = "#checkout"

    product_name_locator = ".inventory_item_name"
    cart_item = ".cart_item"
    error_message = ".error-message-container"

    def __init__(self, page):
        self.page = page

    # ACTIONS

    def click_checkout(self):
        self.page.locator(self.checkout_btn).click()

    # DATA / CHECKS

    def product_name(self):
        return self.page.locator(self.product_name_locator).inner_text()

    def cart_is_empty(self):
        return self.page.locator(self.cart_item).count() == 0

    def get_error_message(self):
        return self.page.locator(self.error_message).inner_text()