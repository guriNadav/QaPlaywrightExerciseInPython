from pages.base_page import BasePage
from utils.price_utils import extract_price

class CartPage(BasePage):
    path = "https://cart.ebay.com"
    total_selector = '[data-test-id="ITEM_TOTAL"]'
    remove_button_selector = "button:has-text('Remove'), [data-test-id='cart-remove-item']"

    def get_total_price(self) -> float:
        locator = self.page.locator(self.total_selector)
        try:
            locator.wait_for(state="visible")
            text = locator.inner_text()
            return extract_price(text)
        except Exception as e:
            print(f"Failed to retrieve cart total price: {e}")
            return 0.0
   
    def remove_all_items(self):
            remove_buttons = self.page.locator(self.remove_button_selector)
            
            try:
                remove_buttons.first.wait_for(state="visible", timeout=2000)
            except Exception:
                print("No remove buttons found. Cart might be empty.")
                return

            while remove_buttons.count() > 0:
                btn = remove_buttons.first
                if btn.is_visible():
                    btn.click()
                    self.page.wait_for_timeout(2000)
                else:
                    break

    def navigate(self):
        self.page.goto(self.path, wait_until="domcontentloaded")

    def take_screenshot(self, file_name: str):
        self.page.screenshot(path=f"screenshots/{file_name}.png")
