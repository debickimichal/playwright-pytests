import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function") #function->czysty browser na każdy test
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # headless = True (CI-ready)
        context = browser.new_context(              # izolowana sesja ktora ma wlasne cookies, historie itd.
            record_video_dir="videos/"
        )   
        
        page = context.new_page()

        yield page

        context.close()
        browser.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True) #jesli test failed to zrobi screnshota
def pytest_runtest_makereport(item, call):
    # uruchamiamy test
    outcome = yield
    rep = outcome.get_result()

    if rep.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")
