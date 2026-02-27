import pytest
import time
from Pages.home_page import HomePage
from Pages.search_results_page import SearchResultsPage
from Pages.product_page import ProductPage

def test_nike_purchase_flow(driver):
    # 1. Initialize the Pages (using the driver from conftest)
    home = HomePage(driver)
    results = SearchResultsPage(driver)
    product = ProductPage(driver)

    # 2. Open Nike website and dismiss cookies
    print("Opening Nike home page...")
    home.load()

    # 3. Search for a specific product
    search_item = "Air Force 1"
    print(f"Searching for {search_item}...")
    home.search_for(search_item)

    # 4. Wait a few seconds to see the results before closing
    # This is just for you to see it working - in real tests we use assertions
    print("Search completed. Waiting to show results...")
    time.sleep(10)

    # 5. Validation (Optional - check if the title updated)
    assert search_item in driver.title
    print("Test passed successfully!")