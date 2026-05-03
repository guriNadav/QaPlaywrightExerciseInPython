
from typing import Optional
from pages.base_page import BasePage

class LoginPage(BasePage):
    path = "https://ebay.com"
    sign_in_bar = "//a[text()='Sign in']"
    email_input = "#userid"
    continue_button = "#signin-continue-btn"
    password_input = "#pass"
    login_in_button = "#sgnBt"
    error_message = "#errf"

    def sign_in(self):
        self.click(self.sign_in_bar)

    def enter_user_id(self, user_id: str):
        self.type_text(self.email_input, user_id)
        self.click(self.continue_button)

    def enter_password(self, password: str):
        self.type_text(self.password_input, password)
        self.click(self.login_in_button)

    def login(self, user_id: str, password: str):
        # ניווט ראשוני לדף הלוגין
        self.page.goto(self.path)
        # במקרים מסוימים איביי מציג דף שונה, לכן נוסיף בדיקה קלה
        if self.page.locator(self.email_input).is_visible():
            self.enter_user_id(user_id)
            self.enter_password(password)

    def get_error_message(self) -> Optional[str]:
        try:
            return self.get_text(self.error_message)
        except Exception:
            return None
# from typing import Optional
# from pages.base_page import BasePage

# class LoginPage(BasePage):
#     """Page object representing the eBay login flow."""
    
#     # נתיב יחסי; משמש לניווט ראשוני אם נדרש
#     path = "https://ebay.com" 
#     sign_in_bar = "//a[text()='Sign in']"
#     email_input = "#userid"
#     continue_button = "#signin-continue-btn"
#     password_input = "#pass"
#     login_in_button = "#sgnBt"
#     error_message = "#errf"

#     async def sign_in(self) -> None:
#         """Click the sign‑in link/bar."""
#         self.click(self.sign_in_bar)

#     async def enter_user_id(self, user_id: str) -> None:
#         """Enter the e‑mail/username and click continue."""
#         self.type_text(self.email_input, user_id)
#         self.click(self.continue_button)

#     async def enter_password(self, password: str) -> None:
#         """Enter the password and submit the login form."""
#         self.type_text(self.password_input, password)
#         self.click(self.login_in_button)

#     async def login(self, user_id: str, password: str) -> None:
#         """Perform the full login sequence."""
#         self.sign_in()
#         self.enter_user_id(user_id)
#         self.enter_password(password)

#     async def get_error_message(self) -> Optional[str]:
#         """Return the error message text if present, otherwise None."""
#         try:
#             return self.get_text(self.error_message)
#         except Exception:
#             return None


# from typing import Optional

# from .base_page import BasePage


# class LoginPage(BasePage):
#     """Page object representing the eBay login flow."""

#     # Relative path used after navigation; adjust as needed for full URL construction
#     path = "/cart"

#     sign_in_bar = "//a[text()='Sign in']"
#     email_input = "#userid"
#     continue_button = "#signin-continue-btn"
#     password_input = "#pass"
#     login_in_button = "#sgnBt"
#     error_message = "#errf"

#     async def sign_in(self) -> None:
#         """Click the sign‑in link/bar."""
#         await self.click(self.sign_in_bar)

#     async def enter_user_id(self, user_id: str) -> None:
#         """Enter the e‑mail/username and click continue."""
#         await self.type_text(self.email_input, user_id)
#         await self.click(self.continue_button)

#     async def enter_password(self, password: str) -> None:
#         """Enter the password and submit the login form."""
#         await self.type_text(self.password_input, password)
#         await self.click(self.login_in_button)

#     async def login(self, user_id: str, password: str) -> None:
#         """Perform the full login sequence.

#         Raises any exception that occurs during the steps.
#         """
#         await self.sign_in()
#         await self.enter_user_id(user_id)
#         await self.enter_password(password)

#     async def get_error_message(self) -> Optional[str]:
#         """Return the error message text if present, otherwise ``None``."""
#         try:
#             return await self.get_text(self.error_message)
#         except Exception:
#             return None
