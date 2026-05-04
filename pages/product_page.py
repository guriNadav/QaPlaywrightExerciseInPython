import random
import re
from typing import Optional
from playwright.sync_api import Page
from pages.base_page import BasePage

class ProductPage(BasePage):
    """Page object for an eBay product detail page.
    Provides utilities for selecting random variant options, adding the product to the cart,
    and handling the lightbox confirmation dialog.
    """
    
    add_to_cart_btn = "//span[contains(@class, 'ux-call-to-action__text') and contains(., 'Add to cart')]"
    lightbox = ".lightbox-dialog__window.lightbox-dialog__window--animate.keyboard-trap--active"
    lightbox_confirm_btn = '[data-testid="ux-call-to-action"]'


    def select_random_variants(self):
        custom_selects = self.page.locator(
            '[data-testid="x-msku-evo"] .listbox-button', 
            has=self.page.locator(".btn__text", has_text=re.compile(r"^Select$", re.IGNORECASE))
        )

        custom_count = custom_selects.count()
        
        if custom_count > 0:
            for _ in range(custom_count):
                current_container = custom_selects.first
                current_container.click()
                valid_options = current_container.locator('.listbox__option[role="option"]:not([aria-disabled="true"])').filter(
                    has_not_text=re.compile(r"Select|Out of stock", re.IGNORECASE)
                )

                options_count = valid_options.count()
                if options_count > 0:
                    random_index = random.randint(0, options_count - 1)
                    valid_options.nth(random_index).click()
                    self.page.wait_for_timeout(500)
        else:
            native_selects = self.page.locator("select:visible")
            native_count = native_selects.count()
            
            for i in range(native_count):
                select = native_selects.nth(i)
                options = select.locator("option:not([disabled])")
                options_count = options.count()
                
                if options_count > 1:
                    random_index = random.randint(1, options_count - 1)
                    select.select_option(index=random_index)

    def add_to_cart(self) -> None:
        """Click the *Add to cart* button."""
        self.page.locator(self.add_to_cart_btn).click()

    def wait_for_lightbox(self) -> None:
        container = self.page.locator(self.lightbox)
        container.wait_for(state="visible")
        container.locator(self.lightbox_confirm_btn).first.wait_for(state="visible")

    def screenshot_lightbox(self, path: str) -> None:
        self.wait_for_lightbox()
        self.page.locator(self.lightbox).screenshot(path=path)