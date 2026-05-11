from aqa_test_task.pages.login_page import LoginPage

def test_login_with_locked_out_user(page):
    login = LoginPage(page)

    # Precondition
    login.open()

    # Step 1: enter login
    login.enter_login("locked_out_user")

    # Step 2: enter password
    login.enter_password("secret_sauce")

    # Step 3: click login
    login.click_login()

    # Expected result

    # error message
    error_text = login.get_error()
    assert "Sorry, this user has been locked out" in error_text

    # red fields (UI check)
    assert login.login_field_has_error()
    assert login.password_field_has_error()

    # X icon check
    assert login.is_error_icon_visible()