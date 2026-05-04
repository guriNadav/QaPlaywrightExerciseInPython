import random
import re
from typing import Optional
from playwright.sync_api import Page
# תיקון נתיב: שימוש בנתיב אבסולוטי
from pages.base_page import BasePage

class ProductPage(BasePage):
    """Page object for an eBay product detail page.
    Provides utilities for selecting random variant options, adding the product to the cart,
    and handling the lightbox confirmation dialog.
    """
    
    add_to_cart_btn = "//span[contains(@class, 'ux-call-to-action__text') and contains(., 'Add to cart')]"
    lightbox = ".lightbox-dialog__window.lightbox-dialog__window--animate.keyboard-trap--active"


    def select_random_variants(self):
        # המרה מדויקת של הסלקטור מה-TS לפייתון
        custom_selects = self.page.locator(
            '[data-testid="x-msku-evo"] .listbox-button', 
            has=self.page.locator(".btn__text", has_text=re.compile(r"^Select$", re.IGNORECASE))
        )

        custom_count = custom_selects.count()
        
        if custom_count > 0:
            # ב-TS השתמשת ב-first() בתוך הלולאה כי איביי מרענן את האלמנטים
            for _ in range(custom_count):
                current_container = custom_selects.first
                current_container.click()

                # סינון האופציות (המרה של .filter({ hasNotText: ... }))
                valid_options = current_container.locator('.listbox__option[role="option"]:not([aria-disabled="true"])').filter(
                    has_not_text=re.compile(r"Select|Out of stock", re.IGNORECASE)
                )

                options_count = valid_options.count()
                if options_count > 0:
                    random_index = random.randint(0, options_count - 1)
                    valid_options.nth(random_index).click()
                    self.page.wait_for_timeout(500)
        else:
            # לוגיקת ה-Native Select
            native_selects = self.page.locator("select:visible")
            native_count = native_selects.count()
            
            for i in range(native_count):
                select = native_selects.nth(i)
                options = select.locator("option:not([disabled])")
                options_count = options.count()
                
                if options_count > 1:
                    # ב-TS עשית Math.random() * (count - 1) + 1 כדי לדלג על ה-placeholder
                    random_index = random.randint(1, options_count - 1)
                    select.select_option(index=random_index)

    # def select_random_variants(self) -> None:
    #     """Select random options for custom and native variant selectors."""
        
    #     # בחירת ווריאציות מבוססות Listbox (Custom)
    #     custom_selects = self.page.locator(
    #         '[data-testid="x-msku-evo"] .listbox-button',
    #         has=self.page.locator('.btn__text', has_text=re.compile(r"^Select$", re.IGNORECASE)),
    #     )
        
    #     custom_count = custom_selects.count()
        
    #     if custom_count > 0:
    #         for i in range(custom_count):
    #             current_container = custom_selects.nth(i)
    #             current_container.click()
                
    #             # סינון אפשרויות לא זמינות או טקסטים של "בחר"
    #             valid_options = current_container.locator('.listbox__option[role="option"]:not([aria-disabled="true"])').filter(
    #                 has_not_text=re.compile(r"Select|Out of stock", re.IGNORECASE)
    #             )
                
    #             options_count = valid_options.count()
    #             if options_count > 0:
    #                 random_index = random.randint(0, options_count - 1)
    #                 valid_options.nth(random_index).click()
    #                 self.page.wait_for_timeout(500)
    #     else:
    #         # מעבר לחיפוש אלמנטים של <select> רגילים (Native)
    #         native_selects = self.page.locator('select:visible')
    #         native_count = native_selects.count()
            
    #         for i in range(native_count):
    #             select = native_selects.nth(i)
    #             options = select.locator('option:not([disabled])')
    #             options_count = options.count()
                
    #             if options_count > 1:
    #                 # דילוג על האופציה הראשונה (בדרך כלל placeholder)
    #                 random_index = random.randint(1, options_count - 1)
    #                 select.select_option(index=random_index)

    def add_to_cart(self) -> None:
        """Click the *Add to cart* button."""
        self.page.locator(self.add_to_cart_btn).click()

    def wait_for_lightbox(self) -> None:
        """Wait for the lightbox dialog to become visible."""
        self.page.locator(self.lightbox).wait_for(state="visible")

    def screenshot_lightbox(self, path: str) -> None:
        """Take a screenshot of the lightbox dialog."""
        self.page.locator(self.lightbox).screenshot(path=path)


# import random
# import re
# from typing import Optional

# from playwright.async_api import Page

# from .base_page import BasePage


# class ProductPage(BasePage):
#     """Page object for an eBay product detail page.

#     Provides utilities for selecting random variant options, adding the product
#     to the cart, and handling the lightbox confirmation dialog.
#     """

#     add_to_cart_btn = "//span[contains(@class, 'ux-call-to-action__text') and contains(., 'Add to cart')]"
#     lightbox = ".lightbox-dialog__window.lightbox-dialog__window--animate.keyboard-trap--active"

#     async def select_random_variants(self) -> None:
#         """Select random options for custom and native variant selectors.

#         The method mirrors the logic in the original TypeScript implementation:
#         * If custom list‑box selectors are present, click each and pick a random
#           viable option (excluding *Select* or *Out of stock* text).
#         * Otherwise, fall back to native `<select>` elements and choose a random
#           option (skipping the first placeholder option).
#         """
#         # Custom listbox based selectors
#         custom_selects = self.page.locator(
#             '[data-testid="x-msku-evo"] .listbox-button',
#             has=self.page.locator('.btn__text', has_text=re.compile(r"^Select$", re.IGNORECASE)),
#         )
#         custom_count = await custom_selects.count()
#         if custom_count > 0:
#             for i in range(custom_count):
#                 current_container = custom_selects.nth(i)
#                 await current_container.click()
#                 # Filter out options that are disabled or contain "Select" / "Out of stock"
#                 valid_options = current_container.locator('.listbox__option[role="option"]:not([aria-disabled="true"])').filter(
#                     has_not_text=re.compile(r"Select|Out of stock", re.IGNORECASE)
#                 )
#                 options_count = await valid_options.count()
#                 if options_count > 0:
#                     random_index = random.randint(0, options_count - 1)
#                     await valid_options.nth(random_index).click()
#                     await self.page.wait_for_timeout(500)
#         else:
#             # Fallback to native <select> elements that are visible
#             native_selects = self.page.locator('select:visible')
#             native_count = await native_selects.count()
#             for i in range(native_count):
#                 select = native_selects.nth(i)
#                 options = select.locator('option:not([disabled])')
#                 options_count = await options.count()
#                 if options_count > 1:
#                     # Skip the first option (often a placeholder) and pick a random one
#                     random_index = random.randint(1, options_count - 1)
#                     await select.select_option(index=random_index)

#     async def add_to_cart(self) -> None:
#         """Click the *Add to cart* button."""
#         await self.page.locator(self.add_to_cart_btn).click()

#     async def wait_for_lightbox(self) -> None:
#         """Wait for the lightbox dialog to become visible."""
#         await self.page.locator(self.lightbox).wait_for(state="visible")

#     async def screenshot_lightbox(self, path: str) -> None:
#         """Take a screenshot of the lightbox dialog.

#         Args:
#             path: Destination file path for the PNG screenshot.
#         """
#         await self.page.locator(self.lightbox).screenshot(path=path)
