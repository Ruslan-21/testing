from aqa_test_task.pages.login_page import LoginPage

def test_valid_login(page):
    login = LoginPage(page)

    login.open()
    login.enter_login("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    assert "inventory" in page.url