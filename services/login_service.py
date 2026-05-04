from playwright.sync_api import Page
from pages.login_page import LoginPage

class LoginService:
    def __init__(self, page: Page):
        self.page = page
        self.login_page = LoginPage(page)

    def login(self, user_id: str, password: str): 
        self.page.wait_for_load_state("networkidle")
        self.page.goto(self.login_page.path)
        self.login_page.login(user_id, password)

    def is_logged_in(self) -> bool:
        try:
            return self.page.locator("#gh-uo").is_visible()
        except Exception:
            return False