import json
import os
import pytest
from pathlib import Path
from dotenv import load_dotenv
from playwright.sync_api import Page

load_dotenv()

from services.login_service import LoginService
from services.search_service import SearchService
from services.cart_service import CartService

TEST_DATA_PATH = Path(__file__).parent.parent / "data" / "testData.json"

with TEST_DATA_PATH.open(encoding='utf-8') as f:
    TEST_DATA = json.load(f)

def test_complete_flow(page: Page):
    login_service = LoginService(page)
    search_service = SearchService(page)
    cart_service = CartService(page)

    login_service.login(
        os.getenv("EBAY_USER", ""),
        os.getenv("EBAY_PASS", ""),
    )

    cart_service.clear_cart()

    urls = search_service.search_items_by_name_under_price(
        TEST_DATA["search"]["query"],
        TEST_DATA["search"]["maxPrice"],
        TEST_DATA["search"]["limit"],
    )

    if not urls:
        pytest.skip("No items found")

    cart_service.add_items_to_cart(urls)
    cart_service.assert_cart_total_not_exceeds(
        TEST_DATA["search"]["maxPrice"],
        len(urls),
    )