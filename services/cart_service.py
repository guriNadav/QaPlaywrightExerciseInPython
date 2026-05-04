from typing import List
from playwright.sync_api import Page
from pages.product_page import ProductPage
from pages.cart_page import CartPage

class CartService:
    """Service for interacting with product and cart pages.
    Provides methods to add items to the cart, verify the cart total against a budget,
    clear the cart, and navigate to the cart page.
    """
    
    def __init__(self, page: Page):
        self.page = page
        self.product_page = ProductPage(page)
        self.cart_page = CartPage(page)

    def add_items_to_cart(self, urls: List[str]) -> None:
        """Visit each product URL, select random variants, add to cart, and capture a lightbox screenshot.
        Args:
            urls: List of product page URLs to process.
        """
        index = 1
        for url in urls:
            self.page.goto(url)
            self.product_page.select_random_variants()
            self.product_page.add_to_cart()
            self.product_page.wait_for_lightbox()
            self.product_page.screenshot_lightbox(f"screenshots/item-{index}.png")
            index += 1

    def assert_cart_total_not_exceeds(self, budget_per_item: float, items_count: int) -> None:
        """Assert that the cart total does not exceed the calculated budget.
        Raises an AssertionError if the total is missing or exceeds the expected maximum.
        """
        self.cart_page.navigate()
        total = self.cart_page.get_total_price()
        expected_max = budget_per_item * items_count
        
        assert total is not None, "Cart total price not found or invalid"
        assert total <= expected_max, f"Cart total {total} exceeds expected max {expected_max}"
        
        self.cart_page.take_screenshot("cart-summary")

    def clear_cart(self) -> None:
        self.cart_page.navigate()
        self.page.wait_for_timeout(2000)
        try:
            self.cart_page.remove_all_items() 
        except Exception:
            pass 
    def link_to_cart(self) -> None:
        """Navigate to the cart page without performing any additional actions."""
        self.cart_page.navigate()