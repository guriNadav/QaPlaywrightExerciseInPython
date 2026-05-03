"""Python equivalent of the Playwright TypeScript configuration.

The original ``playwright.config.ts`` defined global test settings, reporter
configuration, and project‑specific device settings. In the Python ecosystem we
typically configure Playwright via ``pytest`` (using the ``pytest-playwright``
plugin) and a ``conftest.py`` or ``pytest.ini`` file. This module provides a
``CONFIG`` dictionary that mirrors the original TS options so it can be imported
by a ``conftest.py`` if desired.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load ``.env`` located at the repository root (same directory as this file)
load_dotenv(dotenv_path=Path(__file__).with_name(".env"))

# Base configuration mirroring ``playwright.config.ts``
CONFIG = {
    "test_dir": "./tests",
    "fully_parallel": True,
    "forbid_only": bool(os.getenv("CI")),  # equivalent to !!process.env.CI
    "retries": 2 if os.getenv("CI") else 1,
    "workers": 1 if os.getenv("CI") else None,
    "reporters": [
        ["html"],
        [
            "allure-playwright",
            {
                "outputFolder": "allure-results",
                "detail": True,
            },
        ],
    ],
    "use": {
        "base_url": "https://www.ebay.com",
        "screenshot": "only-on-failure",
        "video": "retain-on-failure",
        "trace": "retain-on-failure",
        "action_timeout": 20000,
        "navigation_timeout": 40000,
    },
    "projects": [
        {
            "name": "chromium",
            # Playwright's built‑in device descriptor for Desktop Chrome
            "use": {
                "browser_name": "chromium",
                "viewport": {"width": 1280, "height": 720},
                "user_agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
                ),
                "device_scale_factor": 1,
                "is_mobile": False,
                "has_touch": False,
                "default_browser_type": "chromium",
            },
        }
    ],
}
