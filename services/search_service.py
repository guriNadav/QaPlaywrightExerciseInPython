from typing import List, Optional
from playwright.sync_api import Page

# תיקון נתיבים: שימוש בנתיבים אבסולוטיים ללא נקודות
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from utils.price_utils import extract_price

class SearchService:
    """Service that searches for items by name and filters them by maximum price.
    It uses the HomePage and SearchResultsPage page objects to perform the search,
    apply a price filter, iterate over result items, and paginate through result pages
    until the desired number of unique links is collected.
    """
    
    def __init__(self, page: Page):
        self.page = page
        self.home_page = HomePage(page)
        self.results_page = SearchResultsPage(page)

    def search_items_by_name_under_price(
        self, query: str, max_price: float, limit: int = 5,
    ) -> List[str]:
        """Search for items matching *query* and return up to *limit* links 
        whose price is less than or equal to *max_price*.
        """
        results: List[str] = []
        self.home_page.search(query)
        self.results_page.apply_max_price(max_price)

        while len(results) < limit:
            items = self.results_page.get_items()
            
            # וידוא לפחות פריט אחד נראה לפני המשך
            try:
                items.first.wait_for(state="visible")
            except Exception:
                # אם ההמתנה נכשלת, ממשיכים לאיטרציה הבאה (אין פריטים)
                pass

            count = items.count()
            if count == 0:
                break

            for i in range(count):
                item = items.nth(i)
                
                # חילוץ טקסט המחיר בצורה בטוחה
                try:
                    price_text = item.locator(".s-card__attribute-row").first.inner_text()
                except Exception:
                    price_text = None
                
                # חילוץ הלינק (href) בצורה בטוחה
                try:
                    link: Optional[str] = item.locator("a.s-card__link").first.get_attribute("href")
                except Exception:
                    link = None

                # עיבוד המחיר ובדיקת עמידה בתנאים
                price: Optional[float] = extract_price(price_text) if price_text else None
                
                if price is not None and price <= max_price and link:
                    if link not in results:
                        results.append(link)
                    if len(results) >= limit:
                        return results

            # ניסיון לעבור לעמוד הבא
            has_next = self.results_page.go_to_next_page()
            if not has_next:
                break
                
            self.page.wait_for_load_state("domcontentloaded")

        return results


# from typing import List, Optional

# from playwright.async_api import Page

# # from ..pages.home_page import HomePage
# # from ..pages.search_results_page import SearchResultsPage
# # from ..utils.price_utils import extract_price

# from pages.home_page import HomePage
# from pages.search_results_page import SearchResultsPage
# from utils.price_utils import extract_price


# class SearchService:
#     """Service that searches for items by name and filters them by maximum price.

#     It uses the HomePage and SearchResultsPage page objects to perform the
#     search, apply a price filter, iterate over result items, and paginate
#     through result pages until the desired number of unique links is collected.
#     """

#     def __init__(self, page: Page):
#         self.page = page
#         self.home_page = HomePage(page)
#         self.results_page = SearchResultsPage(page)

#     async def search_items_by_name_under_price(
#         self,
#         query: str,
#         max_price: float,
#         limit: int = 5,
#     ) -> List[str]:
#         """Search for items matching *query* and return up to *limit* links whose
#         price is less than or equal to *max_price*.

#         The method mirrors the original TypeScript implementation, preserving
#         error handling, deduplication, and pagination behavior.
#         """
#         results: List[str] = []

#         await self.home_page.search(query)
#         await self.results_page.apply_max_price(max_price)

#         while len(results) < limit:
#             items = await self.results_page.get_items()

#             # Ensure at least one item is visible before proceeding
#             try:
#                 await items.first.wait_for(state="visible")
#             except Exception:
#                 # If waiting fails, continue to the next iteration (no items)
#                 pass

#             count = await items.count()
#             if count == 0:
#                 break

#             for i in range(count):
#                 item = items.nth(i)

#                 # Extract price text safely
#                 try:
#                     price_text = await item.locator(".s-card__attribute-row").first.inner_text()
#                 except Exception:
#                     price_text = None

#                 # Extract href safely
#                 try:
#                     link: Optional[str] = await item.locator("a.s-card__link").first.get_attribute("href")
#                 except Exception:
#                     link = None

#                 price: Optional[float] = extract_price(price_text) if price_text else None

#                 if price is not None and price <= max_price and link:
#                     if link not in results:
#                         results.append(link)
#                     if len(results) >= limit:
#                         return results

#             has_next = await self.results_page.go_to_next_page()
#             if not has_next:
#                 break

#             await self.page.wait_for_load_state("domcontentloaded")

#         return results
