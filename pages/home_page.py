from pages.base_page import BasePage

class HomePage(BasePage):
    search_input = "#gh-ac"
    search_button = "#gh-search-btn"

    def search(self, query: str):
        self.type_text(self.search_input, query)
        self.click(self.search_button)
# from pages.base_page import BasePage

# class HomePage(BasePage):
#     """Page object for the eBay home page with a simple search feature."""
    
#     search_input = "#gh-ac"
#     search_button = "#gh-search-btn"

#     async def search(self, query: str) -> None:
#         """Enter a query into the search box and click the search button."""
#         self.type_text(self.search_input, query)
#         self.click(self.search_button)


# from .base_page import BasePage


# class HomePage(BasePage):
#     """Page object for the eBay home page with a simple search feature."""

#     search_input = "#gh-ac"
#     search_button = "#gh-search-btn"

#     async def search(self, query: str) -> None:
#         """Enter a query into the search box and click the search button."""
#         await self.type_text(self.search_input, query)
#         await self.click(self.search_button)
