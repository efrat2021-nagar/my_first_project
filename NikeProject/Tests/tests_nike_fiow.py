
from datetime import date
from playwright.sync_api import expect
from PythonProject.NikeProject.pages.home_page import HomePage
from PythonProject.NikeProject.pages.search_results_page import SearchResultsPage
from PythonProject.NikeProject.pages.cart_page import CartPage

class testNikeHomePage(HomePage):
    def test_load(self):
        print("Opening Nike homepage")
        self.page.goto("https://www.nike.com/il/")


