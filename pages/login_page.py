from typing import Optional
from pages.base_page import BasePage

class LoginPage(BasePage):
    path = "https://ebay.com"
    sign_in_bar = "//a[text()='Sign in']"
    email_input = "#userid"
    continue_button = "#signin-continue-btn"
    password_input = "#pass"
    login_in_button = "#sgnBt"
    error_message = "#errf"

    def sign_in(self):
        self.click(self.sign_in_bar)

    def enter_user_id(self, user_id: str):
        self.page.click(self.email_input)
        self.page.type(self.email_input, user_id, delay=50)
        self.click(self.continue_button)

    def enter_password(self, password: str):
        self.page.click(self.password_input)
        self.page.type(self.password_input, password, delay=50)
        self.click(self.login_in_button)

    def login(self, user_id: str, password: str):
        self.sign_in()
        self.page.wait_for_timeout(1500)
        self.enter_user_id(user_id)
        self.enter_password(password)

    def get_error_message(self) -> Optional[str]:
        try:
            return self.get_text(self.error_message)
        except Exception:
            return None