from pages.base_page import BasePage

class HomePage(BasePage):
    search_input = "#gh-ac"
    search_button = "#gh-search-btn"

    def search(self, query: str):
        self.type_text(self.search_input, query)
        self.click(self.search_button)