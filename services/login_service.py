from playwright.sync_api import Page
from pages.login_page import LoginPage

class LoginService:
    def __init__(self, page: Page):
        self.page = page
        self.login_page = LoginPage(page)

    def login(self, user_id: str, password: str): # הורדנו async
        self.page.goto(self.login_page.path)
        self.login_page.login(user_id, password)
        self.page.wait_for_load_state("domcontentloaded")

    def is_logged_in(self) -> bool:
        try:
            return self.page.locator("#gh-uo").is_visible()
        except Exception:
            return False


# from typing import Optional

# from playwright.async_api import Page

# # from ..pages.login_page import LoginPage
# from pages.login_page import LoginPage



# class LoginService:
#     """Service that handles user login and checks login status.

#     Mirrors the original TypeScript implementation, preserving the navigation
#     flow, credential submission, and error handling.
#     """

#     def __init__(self, page: Page):
#         self.page = page
#         self.login_page = LoginPage(page)

#     async def login(self, user_id: str, password: str) -> None:
#         """Navigate to the login page and perform the login sequence."""
#         # Navigate to the login page URL defined in the page object
#         await self.page.goto(self.login_page.path)
#         await self.login_page.login(user_id, password)
#         # Ensure the page has finished loading after login
#         await self.page.wait_for_load_state("domcontentloaded")

#     async def is_logged_in(self) -> bool:
#         """Return ``True`` if the user menu indicating a logged‑in state is visible.

#         Errors while locating the element are caught and result in ``False``.
#         """
#         try:
#             return await self.page.locator("#gh-uo").is_visible()
#         except Exception:
#             return False





# # from typing import Optional

# # from playwright.async_api import Page

# # from ..pages.login_page import LoginPage


# # class LoginService:
# #     """Service that handles user login and checks login status.

# #     Mirrors the original TypeScript implementation, preserving the navigation
# #     flow, credential submission, and error handling.
# #     """

# #     def __init__(self, page: Page):
# #         self.page = page
# #         self.login_page = LoginPage(page)

# #     async def login(self, user_id: str, password: str) -> None:
# #         """Navigate to the login page and perform the login sequence."""
# #         # Navigate to the login page URL defined in the page object
# #         await self.page.goto(self.login_page.path)
# #         await self.login_page.login(user_id, password)
# #         # Ensure the page has finished loading after login
# #         await self.page.wait_for_load_state("domcontentloaded")

# #     async def is_logged_in(self) -> bool:
# #         """Return ``True`` if the user menu indicating a logged‑in state is visible.

# #         Errors while locating the element are caught and result in ``False``.
# #         """
# #         try:
# #             return await self.page.locator("#gh-uo").is_visible()
# #         except Exception:
# #             return False
