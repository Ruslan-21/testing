from playwright.sync_api import Page

class LoginPage:

    username = "#user-name"
    password = "#password"
    login_btn = "#login-button"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    def enter_login(self, username):
        self.page.locator(self.username).fill(username)

    def enter_password(self, password):
        self.page.locator(self.password).fill(password)

    def click_login(self):
        self.page.locator(self.login_btn).click()

    def get_error(self):
        return self.page.locator("h3[data-test='error']").inner_text()

    def login_field_has_error(self):
        return "error" in self.page.locator(self.username).get_attribute("class")

    def password_field_has_error(self):
        return "error" in self.page.locator(self.password).get_attribute("class")

    def is_error_icon_visible(self):
        return self.page.locator(".error_icon, .error-icon").first.is_visible()