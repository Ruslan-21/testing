from aqa_test_task.pages.login_page import LoginPage


def test_invalid_password(page):
    login = LoginPage(page)

    login.open()
    login.enter_login("standard_user")
    login.enter_password("wrong_password")
    login.click_login()

    assert "Username and password do not match" in login.get_error()