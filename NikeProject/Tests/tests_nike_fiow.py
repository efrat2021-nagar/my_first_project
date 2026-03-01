import pytest
from selenium import webdriver
from Pages.home_page import HomePage
from Pages.search_results_page import SearchResultsPage
from Pages.product_page import ProductPage


# --- Setup Fixture ---
@pytest.fixture
def driver():
    """Sets up the Chrome driver before each test and closes it after."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# --- Page 1: Home Page Tests ---

def test_home_page_title(driver):
    home = HomePage(driver)
    home.load()
    # Verify the page loaded with the correct title
    assert "Nike" in driver.title


def test_search_execution(driver):
    home = HomePage(driver)
    home.load()
    home.search_for("Air Force 1")
    # Verify the search directed to a results page
    assert "Air Force 1" in driver.title


# --- Page 2: Search Results Page Tests ---

def test_results_list_not_empty(driver):
    home = HomePage(driver)
    results = SearchResultsPage(driver)

    home.load()
    home.search_for("Jordan")
    # Check that the product list contains items
    products = results.get_product_list()
    assert len(products) > 0


def test_apply_gender_filter(driver):
    home = HomePage(driver)
    results = SearchResultsPage(driver)

    home.load()
    home.search_for("Running")
    results.apply_filter("Men")
    # Check if the URL updated to reflect the filter
    assert "men" in driver.current_url.lower()


# --- Page 3: Product Page Tests ---

def test_product_price_visibility(driver):
    home = HomePage(driver)
    results = SearchResultsPage(driver)
    product = ProductPage(driver)

    home.load()
    home.search_for("Dunk")
    results.click_first_product()
    # Verify the price element is not empty
    price = product.get_price()
    assert price is not None
    assert len(price) > 0


def test_error_when_no_size_selected(driver):
    home = HomePage(driver)
    results = SearchResultsPage(driver)
    product = ProductPage(driver)

    home.load()
    home.search_for("Pegasus")
    results.click_first_product()
    product.click_add_to_cart()
    # Verify an error message appears because no size was picked
    assert product.is_error_message_displayed()