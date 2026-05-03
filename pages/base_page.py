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


# from playwright.async_api import Page


# class BasePage:
#     """Base page object providing common actions using Playwright async API."""

#     def __init__(self, page: Page):
#         self.page = page

#     async def click(self, selector: str) -> None:
#         """Click an element identified by the selector."""
#         await self.page.click(selector)

#     async def type_text(self, selector: str, text: str) -> None:
#         """Fill an input element with the provided text."""
#         await self.page.fill(selector, text)

#     async def get_text(self, selector: str) -> str:
#         """Retrieve inner text of the element identified by the selector."""
#         return await self.page.inner_text(selector)

#     async def wait_for(self, selector: str) -> None:
#         """Wait for the element matching selector to be visible/attached."""
#         await self.page.wait_for_selector(selector)
