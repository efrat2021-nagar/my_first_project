
from datetime import date
from playwright.sync_api import expect
from PythonProject.NikeProject.pages.home_page import HomePage
from PythonProject.NikeProject.pages.search_results_page import SearchResultsPage
from PythonProject.NikeProject.pages.cart_page import CartPage


class TestNikeProject:

    def test_open_nike_homepage(self, page):
        home = HomePage(page)
        home.load()
        assert "nike" in page.url.lower()


    def test_search_item(self, page):
        home = HomePage(page)
        home.load()
        home.search_for_item("football")
        assert "search" in page.url.lower()


    def test_football_category_exists(self, page):
        home = HomePage(page)
        search = SearchResultsPage(page)
        home.load()
        home.search_for_item("football")
        assert search.check_football_category()


    def test_products_have_information(self, page):
        home = HomePage(page)
        search = SearchResultsPage(page)
        home.load()
        home.search_for_item("football")
        search.check_products_have_info()


    def test_open_cart_and_check_products(self, page):
        home = HomePage(page)
        cart = CartPage(page)
        home.load()
        cart.open_cart()
        cart.check_product_in_cart()
        cart.check_product_info()

        print("test end")