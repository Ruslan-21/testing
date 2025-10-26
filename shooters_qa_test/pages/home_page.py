from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    BUILD_FOR_FREE_BTN = (
        By.XPATH,
        "//button[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'build for free')]"
    )

    def go_to_build(self):

        return self.click(self.BUILD_FOR_FREE_BTN)
