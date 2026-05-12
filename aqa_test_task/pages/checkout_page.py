class CheckoutPage:

    first_name_input = "#first-name"
    last_name_input = "#last-name"
    postal_code_input = "#postal-code"

    continue_btn = "#continue"
    finish_btn = "#finish"
    back_home_btn = "#back-to-products"

    product_name = ".inventory_item_name"
    total_label = ".summary_total_label"
    success_header = ".complete-header"

    cart_badge = ".shopping_cart_badge"

    def __init__(self, page):
        self.page = page

    # FORM STEP

    def enter_first_name(self, first_name):
        self.page.locator(self.first_name_input).fill(first_name)

    def enter_last_name(self, last_name):
        self.page.locator(self.last_name_input).fill(last_name)

    def enter_postal_code(self, postal_code):
        self.page.locator(self.postal_code_input).fill(postal_code)

    def click_continue(self):
        self.page.locator(self.continue_btn).click()

    # OVERVIEW STEP

    def overview_product_name(self):
        return self.page.locator(self.product_name).inner_text()

    def total_price_visible(self):
        return self.page.locator(self.total_label).is_visible()

    def click_finish(self):
        self.page.locator(self.finish_btn).click()

    # COMPLETE STEP

    def success_message(self):
        return self.page.locator(self.success_header).inner_text()

    def click_back_home(self):
        self.page.locator(self.back_home_btn).click()

    # CART STATE

    def cart_is_empty(self):
        return self.page.locator(self.cart_badge).count() == 0