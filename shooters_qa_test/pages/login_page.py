from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import time

class LoginPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='emailOrPhoneNumber']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    OK_BTN = (By.XPATH, "//button[text()='Ok']")
    AVATAR_IMG = (By.CSS_SELECTOR, "img[role='img'][alt='Avatar image']")
    LOGOUT_BTN = (By.XPATH, "//p[text()='Log Out']")

    def login(self, email, password):

        email_input = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        email_input.clear()
        email_input.send_keys(email)


        password_input = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        password_input.clear()
        password_input.send_keys(password)


        sign_in_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.SIGN_IN_BTN)
        )
        sign_in_btn.click()


        try:
            ok_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.OK_BTN)
            )
            ok_button.click()
        except:
            pass


        time.sleep(30)

    def logout(self):

        avatar = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.AVATAR_IMG)
        )
        avatar.click()


        logout_btn = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.LOGOUT_BTN)
        )
        logout_btn.click()
