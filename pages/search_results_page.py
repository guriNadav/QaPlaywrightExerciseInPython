from pages.base_page import BasePage
from playwright.sync_api import Page

class SearchResultsPage(BasePage):
    """Page object for eBay search results.
    Provides helpers to filter by maximum price, retrieve item locators, 
    and navigate through pagination.
    """
    
    items_selector = "//ul[contains(@class,'srp-results')]//li[contains(@class,'s-card')]"
    next_button = "a[aria-label='Go to next search page']"

    def apply_max_price(self, max_price: float) -> None:
        """Set the maximum price filter if the input is visible.
        Args:
            max_price: Desired maximum price.
        """
        max_input = self.page.locator("input[aria-label^='Maximum Value in']")
        if max_input.is_visible():
            max_input.fill(str(max_price))
            self.page.keyboard.press("Enter")
            self.page.wait_for_selector(self.items_selector, state="visible")

    def get_items(self):
        """Return a locator for all result items on the page."""
        return self.page.locator(self.items_selector)

    def go_to_next_page(self) -> bool:
        """Click the next-page link if it is visible.
        Returns True when navigation succeeds, otherwise False.
        """
        next_elem = self.page.locator(self.next_button)
        if next_elem.is_visible():
            next_elem.click()
            self.page.wait_for_load_state("networkidle")
            return True
        return False