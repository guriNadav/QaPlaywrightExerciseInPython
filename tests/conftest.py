import pytest
import allure
import pathlib
from playwright_config import CONFIG

# ---------------------------------------------------------------------------
# Setup & Configuration
# ---------------------------------------------------------------------------

# Ensure the screenshots directory exists for local debugging
_SCREENSHOTS_DIR = pathlib.Path("screenshots")
_SCREENSHOTS_DIR.mkdir(exist_ok=True)

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Inject project settings (User Agent, Viewport, etc.) from the Playwright config
    into each test's browser context.
    """
    project_use = CONFIG["projects"][0]["use"]
    return {
        **browser_context_args,
        "viewport": project_use["viewport"],
        "user_agent": project_use["user_agent"],
        "device_scale_factor": project_use["device_scale_factor"],
        "is_mobile": project_use["is_mobile"],
        "has_touch": project_use["has_touch"],
        "extra_http_headers": {
            "Accept-Language": "en-US,en;q=0.9"  # mimic a real user
        },
    }

@pytest.fixture(scope="function")
def context(context):
    """Set default timeouts for each test function."""
    context.set_default_timeout(CONFIG["use"]["action_timeout"])
    context.set_default_navigation_timeout(CONFIG["use"]["navigation_timeout"])
    return context

# ---------------------------------------------------------------------------
# Screenshot & Allure Reporting on Failure
# ---------------------------------------------------------------------------

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Capture a screenshot and attach it to the Allure report when a test fails.
    Also saves a local copy in the screenshots/ directory.
    """
    outcome = yield
    result = outcome.get_result()
    
    # We only care about failures that happen during the actual test call
    if result.when == "call" and result.failed:
        page = item.funcargs.get("page")
        if page:
            # 1. Save local copy (for your 'screenshots' folder)
            screenshot_path = _SCREENSHOTS_DIR / f"{item.name}.png"
            screenshot_bytes = page.screenshot(path=str(screenshot_path), full_page=True)
            
            # 2. Attach to Allure Report (for CI/GitHub Pages)
            allure.attach(
                screenshot_bytes,
                name=f"failure_screenshot_{item.name}",
                attachment_type=allure.attachment_type.PNG
            )