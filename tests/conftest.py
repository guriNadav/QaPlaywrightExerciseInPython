import pytest
from playwright_config import CONFIG

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    מזריק את הגדרות ה-Project (כמו ה-User Agent וה-Viewport) 
    מתוך קובץ הקונפיג לכל טסט שנפתח.
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
            "Accept-Language": "en-US,en;q=0.9" # עוזר להיראות כמו משתמש אמיתי
        }
    }

@pytest.fixture(scope="function")
def context(context):
    """מגדיר את זמני ההמתנה (Timeouts) לכל טסט."""
    context.set_default_timeout(CONFIG["use"]["action_timeout"])
    context.set_default_navigation_timeout(CONFIG["use"]["navigation_timeout"])
    return context
