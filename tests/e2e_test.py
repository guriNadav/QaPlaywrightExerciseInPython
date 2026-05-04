import json
import os
import pytest
from pathlib import Path
from dotenv import load_dotenv
from playwright.sync_api import Page

# טעינת משתני סביבה
load_dotenv()

from services.login_service import LoginService
from services.search_service import SearchService
from services.cart_service import CartService

# נתיב לקובץ הנתונים
TEST_DATA_PATH = Path(__file__).parent.parent / "data" / "testData.json"

with TEST_DATA_PATH.open(encoding='utf-8') as f:
    TEST_DATA = json.load(f)

def test_complete_flow(page: Page):
    # אתחול הסרביסים (סינכרוני)
    login_service = LoginService(page)
    search_service = SearchService(page)
    cart_service = CartService(page)

    print("--- Starting Login ---")
    # ביצוע הלוגין
    login_service.login(
        os.getenv("EBAY_USER", ""),
        os.getenv("EBAY_PASS", ""),
    )
    print("--- Login Finished! ---")

    # חיפוש מוצרים
    urls = search_service.search_items_by_name_under_price(
        TEST_DATA["search"]["query"],
        TEST_DATA["search"]["maxPrice"],
        TEST_DATA["search"]["limit"],
    )

    if not urls:
        pytest.skip("No items found")

    # הוספה לסל ואימות
    cart_service.add_items_to_cart(urls)
    cart_service.assert_cart_total_not_exceeds(
        TEST_DATA["search"]["maxPrice"],
        len(urls),
    )
    cart_service.clear_cart()


# import json
# import os
# import pytest
# from pathlib import Path
# from dotenv import load_dotenv
# from playwright.async_api import Page

# # טעינת משתני סביבה
# load_dotenv()

# # ייבוא סרביסים - וודא שהנתיבים תואמים למבנה הפרויקט
# from services.login_service import LoginService
# from services.search_service import SearchService
# from services.cart_service import CartService

# # טעינת נתוני בדיקה (testData.json)
# # הערה: הנתיב מכוון לתיקיית data שנמצאת רמה אחת מעל תיקיית tests
# TEST_DATA_PATH = Path(__file__).parent.parent / "data" / "testData.json"

# try:
#     with TEST_DATA_PATH.open(encoding='utf-8') as f:
#         TEST_DATA = json.load(f)
# except FileNotFoundError:
#     # הגנה למקרה שהקובץ לא נמצא בנתיב המצופה
#     print(f"Warning: Test data not found at {TEST_DATA_PATH}")
#     TEST_DATA = {}

# # @pytest.mark.asyncio
# async def test_complete_flow(page: Page):
#     """
#     E2E test that logs in, searches for items, adds them to the cart, 
#     verifies the total, and clears the cart.
#     """
    
#     # אתחול הסרביסים
#     login_service = LoginService(page)
#     search_service = SearchService(page)
#     cart_service = CartService(page)

#     # 1. התחברות (משיכת פרטים מ-env)
#     await login_service.login(
#         os.getenv("EBAY_USER", ""),
#         os.getenv("EBAY_PASS", ""),
#     )

#     # 2. חיפוש פריטים וקבלת רשימת כתובות (URLs)
#     urls = await search_service.search_items_by_name_under_price(
#         TEST_DATA.get("search", {}).get("query", "laptop"),
#         TEST_DATA.get("search", {}).get("maxPrice", 500.0),
#         TEST_DATA.get("search", {}).get("limit", 3),
#     )

#     if not urls:
#         pytest.skip("No items found matching the criteria")

#     # 3. הוספת הפריטים לסל הקניות
#     await cart_service.add_items_to_cart(urls)

#     # 4. אימות שהסכום הכולל לא חורג מהתקציב
#     await cart_service.assert_cart_total_not_exceeds(
#         TEST_DATA.get("search", {}).get("maxPrice", 500.0),
#         len(urls),
#     )

#     # 5. ניקוי סל הקניות (Clean up)
#     await cart_service.clear_cart()


# import json
# import os
# from pathlib import Path
# from dotenv import load_dotenv


# import pytest
# from playwright.async_api import Page

# # Load environment variables from a .env file if it exists
# load_dotenv()

# # Service imports – adjust PYTHONPATH as needed when running tests
# from services.login_service import LoginService
# from services.search_service import SearchService
# from services.cart_service import CartService

# # Load test data (located at project_root/data/testData.json)
# TEST_DATA_PATH = Path(__file__).parent.parent / "data" / "testData.json"
# with TEST_DATA_PATH.open() as f:
#     TEST_DATA = json.load(f)


# @pytest.mark.asyncio
# async def test_complete_flow(page: Page):
#     """E2E test that logs in, searches for items, adds them to the cart, verifies the total, and clears the cart."""
#     login_service = LoginService(page)
#     search_service = SearchService(page)
#     cart_service = CartService(page)

#     # Login using credentials from environment variables (or .env file)
#     await login_service.login(
#         os.getenv("EBAY_USER", ""),
#         os.getenv("EBAY_PASS", ""),
#     )

#     # Perform search and retrieve product URLs
#     urls = await search_service.search_items_by_name_under_price(
#         TEST_DATA["search"]["query"],
#         TEST_DATA["search"]["maxPrice"],
#         TEST_DATA["search"]["limit"],
#     )

#     if not urls:
#         pytest.skip("No items found")

#     # Add items to the cart
#     await cart_service.add_items_to_cart(urls)

#     # Verify total does not exceed budget per item
#     await cart_service.assert_cart_total_not_exceeds(
#         TEST_DATA["search"]["maxPrice"],
#         len(urls),
#     )

#     # Clean up cart
#     await cart_service.clear_cart()
