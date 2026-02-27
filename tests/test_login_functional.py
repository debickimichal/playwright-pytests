import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from playwright.sync_api import expect

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!") #comment
    dashboard = DashboardPage(page)
    expect(dashboard.welcome_message).to_contain_text("You logged into a secure area")
    dashboard.logout()

def test_links_after_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")
    dashboard = DashboardPage(page)
    expect(dashboard.logout_button).to_be_visible()

