from pages.base_page import BasePage
from utils.price_utils import extract_price

class CartPage(BasePage):
    path = "https://ebay.com"
    total_selector = '[data-test-id="ITEM_TOTAL"]'
    remove_button_selector = '[data-test-id="cart-remove-item"]'

    def get_total_price(self) -> float:
        locator = self.page.locator(self.total_selector)
        try:
            locator.wait_for(state="visible")
            text = locator.inner_text()
            return extract_price(text)
        except Exception as e:
            print(f"Failed to retrieve cart total price: {e}")
            return 0.0

    def remove_all_items(self):
        remove_buttons = self.page.locator(self.remove_button_selector)
        count = remove_buttons.count()
        for _ in range(count):
            # תמיד לוחצים על הכפתור הראשון שנשאר
            remove_buttons.first.click()
            self.page.wait_for_timeout(1000)

    def navigate(self):
        self.page.goto(self.path, wait_until="domcontentloaded")

    def take_screenshot(self, file_name: str):
        self.page.screenshot(path=f"screenshots/{file_name}.png")
# from playwright.async_api import Page
# # תיקון נתיבים: שימוש בנתיב אבסולוטי ללא נקודות
# from pages.base_page import BasePage
# from utils.price_utils import extract_price

# class CartPage(BasePage):
#     """Page object representing the eBay cart page."""
    
#     path = "https://cart.ebay.com"
#     total_selector = '[data-test-id="ITEM_TOTAL"]'
#     remove_button_selector = '[data-test-id="cart-remove-item"]'

#     async def get_total_price(self) -> float:
#         """Return the total price displayed in the cart, or None on failure."""
#         locator = self.page.locator(self.total_selector)
#         try:
#             locator.wait_for(state="visible")
#             text = locator.inner_text()
#             return extract_price(text)
#         except Exception as e:
#             # בייצור כדאי להשתמש ב-logger מסודר
#             print(f"Failed to retrieve cart total price: {e}")
#             return None

#     async def remove_all_items(self) -> None:
#         """Click all remove‑item buttons to empty the cart."""
#         remove_buttons = self.page.locator(self.remove_button_selector)
#         count = remove_buttons.count()
#         for _ in range(count):
#             # תמיד לוחצים על הכפתור הראשון שנמצא (כי הרשימה מתעדכנת אחרי כל מחיקה)
#             remove_buttons.first.click()
#             self.page.wait_for_timeout(500)

#     async def navigate(self) -> None:
#         """Navigate to the cart page, waiting for DOM content to load."""
#         self.page.goto(self.path, wait_until="domcontentloaded")

#     async def take_screenshot(self, file_name: str) -> None:
#         """Capture a screenshot of the current page. 
#         The screenshot is saved under a 'screenshots' directory.
#         """
#         self.page.screenshot(path=f"screenshots/{file_name}.png")


# from playwright.async_api import Page
# from .base_page import BasePage
# from ..utils.price_utils import extract_price


# class CartPage(BasePage):
#     """Page object representing the eBay cart page."""

#     path = "https://cart.ebay.com"
#     total_selector = '[data-test-id="ITEM_TOTAL"]'
#     remove_button_selector = '[data-test-id="cart-remove-item"]'

#     async def get_total_price(self) -> float | None:
#         """Return the total price displayed in the cart, or ``None`` on failure."""
#         locator = self.page.locator(self.total_selector)
#         try:
#             await locator.wait_for(state="visible")
#             text = await locator.inner_text()
#             return extract_price(text)
#         except Exception as e:
#             # Log the error; in production you might use a logger
#             print(f"Failed to retrieve cart total price: {e}")
#             return None

#     async def remove_all_items(self) -> None:
#         """Click all remove‑item buttons to empty the cart."""
#         remove_buttons = self.page.locator(self.remove_button_selector)
#         count = await remove_buttons.count()
#         for _ in range(count):
#             # Always operate on the first matching button after each removal
#             await remove_buttons.first.click()
#             await self.page.wait_for_timeout(500)

#     async def navigate(self) -> None:
#         """Navigate to the cart page, waiting for DOM content to load."""
#         await self.page.goto(self.path, wait_until="domcontentloaded")

#     async def take_screenshot(self, file_name: str) -> None:
#         """Capture a screenshot of the current page.

#         The screenshot is saved under a ``screenshots`` directory relative to the
#         current working directory.
#         """
#         await self.page.screenshot(path=f"screenshots/{file_name}.png")
