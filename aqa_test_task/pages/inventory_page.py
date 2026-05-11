
class InventoryPage:


    def __init__(self, page):
        self.page = page


    def open_burger_menu(self):
        self.page.click("#react-burger-menu-btn")


    def click_logout(self):
        self.page.click("#logout_sidebar_link")


    def is_login_page_opened(self):
        return "saucedemo.com" in self.page.url


    def username_field_empty(self):
        return self.page.input_value("#user-name") == ""


    def password_field_empty(self):
        return self.page.input_value("#password") == ""