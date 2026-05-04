from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, selector: str):
        self.page.click(selector)

    def type_text(self, selector: str, text: str):
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        return self.page.inner_text(selector)

    def wait_for(self, selector: str):
        self.page.wait_for_selector(selector)