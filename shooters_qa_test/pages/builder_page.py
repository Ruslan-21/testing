from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BuilderPage(BasePage):
    BUILDER_CANVAS = (By.CSS_SELECTOR, "canvas")

    def wait_for_canvas(self, timeout=30):

        try:
            iframe = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "iframe"))
            )
            self.driver.switch_to.frame(iframe)
        except:
            pass


        self.wait_for_element(self.BUILDER_CANVAS, timeout=timeout)


        self.driver.switch_to.default_content()
