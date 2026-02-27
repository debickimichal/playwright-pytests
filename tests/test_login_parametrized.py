import pytest
from pages.login_page import LoginPage
from playwright.sync_api import expect


@pytest.mark.parametrize("username,password,expected_message", [
    ("wrong", "wrong", "Your username is invalid!"),
    ("tomsmith", "wrong", "Your password is invalid!"),
    ("", "", "Your username is invalid!")
])
def test_invalid_login(page, username, password, expected_message):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)
    expect(login_page.flash_message).to_contain_text(expected_message)
