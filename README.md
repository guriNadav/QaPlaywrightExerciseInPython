# 📘 eBay End‑to‑End Automation Suite

[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![Playwright](https://img.shields.io/badge/playwright-1.40%2B-green.svg)](https://playwright.dev/python)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📚 Table of Contents
- [Project Overview](#project-overview)
- [Project Architecture](#project-architecture)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Reporting](#reporting)
- [CI/CD](#cicd)
- [Anti‑Bot Handling](#anti-bot-handling)
- [Contributing](#contributing)
- [License](#license)

---

## 🚀 Project Overview
This repository contains an **end‑to‑end (E2E) automation suite** for the eBay marketplace, built with **Python 3.11+** and **Playwright (synchronous API)**.  The test flow covers:
1. Login with credentials from a `.env` file.
2. Searching for products under a configurable price ceiling.
3. Adding the first matching items to the cart.
4. Verifying the cart total and performing a full cleanup.

The suite follows the **Page Object Model (POM)**, separating concerns into **Pages**, **Services**, **Utils**, and **Tests** for maintainability and readability.

---

## 🏗️ Project Architecture
```
python_project/
│   CLAUDE.md                # Project‑specific instructions for Claude Code
│   requirements.txt         # Python dependencies
│   .env (ignored)           # eBay credentials (EBAY_USER, EBAY_PASS)
│   README.md                # 📄 This file
│
├── data/
│   └── testData.json        # Test input – query, price ceiling, limit
│
├── pages/                   # Page‑Object layer – UI wrappers
│   ├── base_page.py
│   ├── home_page.py
│   ├── product_page.py
│   └── cart_page.py
│
├── services/                # Business‑logic layer – orchestrates pages
│   ├── login_service.py
│   ├── search_service.py
│   └── cart_service.py
│
├── utils/                   # Helper functions
│   └── price_utils.py
│
└── tests/                   # Pytest suite
    └── e2e_test.py
```
* **Pages** – Low‑level interactions with Playwright (click, fill, wait, get text).
* **Services** – High‑level flows that combine page actions (e.g., `LoginService.login()`).
* **Utils** – Re‑usable helpers such as price parsing.
* **Tests** – Pytest entry points that wire everything together.

---

## 🛠️ Prerequisites
| Requirement | Version |
|-------------|---------|
| Python      | ≥ 3.11 |
| Playwright  | ≥ 1.40 (sync API) |
| pytest      | ≥ 7.0 |
| Allure‑pytest | ≥ 2.13 |
| dotenv      | ≥ 1.0 |

*Node.js* is **not** required because the suite uses Playwright’s **synchronous** Python API.

---

## 📦 Installation & Setup
```bash
# 1️⃣ Clone the repository (if you haven't already)
git clone <repo‑url>
cd python_project

# 2️⃣ Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .\.venv\Scripts\activate  # Windows PowerShell

# 3️⃣ Install Python dependencies
pip install -r requirements.txt

# 4️⃣ Install Playwright browsers (required for any test run)
playwright install
```
> **Tip**: The `playwright install` step downloads Chromium, Firefox, and WebKit binaries.

---

## ⚙️ Configuration
1. **Environment variables** – Create a `.env` file at the repository root:
   ```dotenv
   EBAY_USER=your_ebay_username
   EBAY_PASS=your_ebay_password
   ```
   The test harness loads this automatically via `dotenv.load_dotenv()`.
2. **pytest.ini** – The repository ships a default `pytest.ini`.  Adjust `addopts` if you need custom markers.
3. **playwright_config.py** (optional) – You can override Playwright launch options (e.g., headless, slow‑mo) by editing this file.  It is imported automatically by the Playwright pytest plugin.

---

## ▶️ Running Tests
| Mode | Command |
|------|---------|
| **Headless (default)** | `pytest` |
| **Run a single test file** | `pytest tests/e2e_test.py` |
| **Run a single test function** | `pytest -k test_complete_flow` |
| **Headed (visible browser)** | `PWDEBUG=1 pytest` |
| **Step‑by‑step debugging** | `PWDEBUG=1 pytest -k test_complete_flow` |

The `PWDEBUG=1` environment variable launches Playwright in headed mode with the inspector open, letting you pause and examine the DOM.

---

## 📊 Reporting
The suite integrates **Allure Report** for rich HTML artifacts.
```bash
# Generate the report after a test run
pytest --alluredir=allure-results
# Serve it locally
allure serve allure-results
```
The generated report includes:
- Test case hierarchy
- Screenshots (saved under `screenshots/`)
- Console logs and Playwright traces

---

## 🚧 CI/CD
A **GitHub Actions** workflow (`.github/workflows/ci.yml`) runs on every push:
1. Sets up Python, installs dependencies, and installs Playwright browsers.
2. Executes `pytest --alluredir=allure-results`.
3. Publishes the Allure results as a static site to **GitHub Pages** under the `gh‑pages` branch, retaining a **30‑day history** of reports.

The workflow ensures that every commit provides an up‑to‑date test report accessible via:
```
https://<your‑org>.github.io/<repo>/
```

---

## 🛡️ Anti‑Bot Handling
Automating eBay is challenging because the platform employs aggressive bot detection.  The following mitigations are baked into the suite:
- **Custom User‑Agent strings** masquerade as a real browser.
- **Explicit wait strategies** (`await page.wait_for_load_state('networkidle')`, `time.sleep` for throttling) avoid rapid, detectable request bursts.
- **Synchronous Playwright API** reduces the number of concurrent connections, mimicking human interaction patterns.
- **Randomized delays** between actions (configurable in `services/*_service.py`).

These measures keep the automation under the radar while preserving test reliability.

---

## 🤝 Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feat/your‑feature`).
3. Write tests alongside any new code.
4. Run the full suite and ensure the Allure report passes.
5. Submit a pull request – CI will automatically generate a report for review.

---

## 📄 License
This project is licensed under the **MIT License** – see the `LICENSE` file for details.

---

*Generated with Claude Code* 🎉
