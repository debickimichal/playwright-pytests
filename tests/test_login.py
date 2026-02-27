from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    expect(login_page.flash_message).to_contain_text(
        "You logged into a secure area"
    )
