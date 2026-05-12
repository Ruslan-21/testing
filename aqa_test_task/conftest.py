import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def login():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,   # 👈 ОБЯЗАТЕЛЬНО: показывает окно
            slow_mo=200       # 👈 замедляет действия (чтобы видеть)
        )

        context = browser.new_context()
        page = context.new_page()

        # open site
        page.goto("https://www.saucedemo.com/")

        # login
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        yield page

        context.close()
        browser.close()