import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser_page():
    url = "https://winwin.travel/app/landings/en"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        context = browser.new_context()
        page = context.new_page()

        page.goto(url)

        yield page

        browser.close()