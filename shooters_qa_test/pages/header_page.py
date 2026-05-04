from playwright.sync_api import Page

class HeaderPage:

    email_input = "#«r16»-form-item"
    password_input = "#«r17»"
    confirm_password_input = "#«r19»"
    register_btn = "[data-wwt-id='header__register--button']"
    sign_in_btn = "[data-wwt-id='header__sign-in--button']"
    get_disc = "[data-wwt-id='header__share--button']"
    logo_link = "[data-wwt-id='promo-button__get-discount--link']"
    modal_register = "#radix-«r2o»"


    def __init__(self, page: Page):
        self.page = page


    def check_register(self):
        self.page.locator(self.register_btn).click()
        self.page.wait_for_timeout(3000)

    def check_sing_in(self):
        self.page.locator(self.sign_in_btn).click()
        self.page.wait_for_timeout(3000)


    def check_logo(self):
        self.page.locator(self.get_disc).click()
        self.page.locator(self.logo_link).click()
