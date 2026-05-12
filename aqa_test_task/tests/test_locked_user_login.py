from aqa_test_task.pages.login_page import LoginPage

def test_login_with_locked_out_user(page):
    login = LoginPage(page)

    login.open()

    login.enter_login("locked_out_user")

    login.enter_password("secret_sauce")

    login.click_login()

    error_text = login.get_error()
    assert "Sorry, this user has been locked out" in error_text

    assert login.login_field_has_error()
    assert login.password_field_has_error()

    assert login.is_error_icon_visible()