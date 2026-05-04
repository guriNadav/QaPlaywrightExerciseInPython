# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Development Commands

- **Install dependencies**: `pip install -r requirements.txt`
- **Run the full test suite**: `pytest`
- **Run a single test file**: `pytest tests/e2e_test.py`
- **Run a specific test function**: `pytest -k test_complete_flow`
- **Load environment variables**: ensure a `.env` file with `EBAY_USER` and `EBAY_PASS` exists; `load_dotenv()` is called automatically in tests.
- **Execute Playwright browsers**: the code uses the **sync** Playwright API. Ensure the browsers are installed with `playwright install`.
- **Generate test data**: `data/testData.json` contains the search query, price ceiling and limit used by the e2e test.

## High‑Level Architecture

- **Page Objects (`pages/` folder)**
  - `BasePage` wraps common Playwright actions (click, fill, get text, wait).
  - `HomePage`, `ProductPage`, `CartPage` extend `BasePage` and expose page‑specific selectors and behaviours (search, add to cart, retrieve total, etc.).
- **Services (`services/` folder)**
  - `LoginService`, `SearchService`, `CartService` orchestrate interactions between page objects and implement business‑level flows such as logging in, searching items under a price, adding items to the cart, asserting budget constraints, and cleaning up.
- **Utilities (`utils/` folder)**
  - `price_utils.extract_price` parses price strings into floats, handling commas and multiple numbers.
- **Tests (`tests/` folder)**
  - `e2e_test.py` is an end‑to‑end pytest test that drives the full user journey using the sync Playwright `Page` fixture.
- **Configuration**
  - `.env` for credentials, loaded by `dotenv.load_dotenv()`.
  - `playwright_config.py` (if present) may contain test fixtures; Playwright’s default pytest plugin supplies the `page` fixture.

## Project Structure Overview

```
python_project/
│   CLAUDE.md            # ← this file
│   requirements.txt
│   .env                 # (not version‑controlled)
│   data/
│       testData.json   # test input data
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── product_page.py
│   └── cart_page.py
│
├── services/
│   ├── login_service.py
│   ├── search_service.py
│   └── cart_service.py
│
├── utils/
│   └── price_utils.py
│
└── tests/
    └── e2e_test.py
```

## Notes for Claude Code
- Prefer the **sync** Playwright API (`playwright.sync_api`) when writing new interactions.
- When adding new page objects, follow the existing pattern: inherit from `BasePage` and expose selectors as class attributes.
- Keep service methods straightforward; they should compose page‑object calls without adding extra layers.
- Use the `tests/e2e_test.py` pattern for new end‑to‑end tests: load environment, instantiate services, perform actions, and clean up.
- Screenshots are stored in a top‑level `screenshots/` directory; ensure it exists before writing.
