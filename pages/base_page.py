from playwright.sync_api import Page, Locator

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def go_to(self, url: str):
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()

    def wait_for_element(self, locator: Locator, timeout: int = 5000) -> Locator:
        locator.wait_for(state="visible", timeout=timeout)
        return locator
