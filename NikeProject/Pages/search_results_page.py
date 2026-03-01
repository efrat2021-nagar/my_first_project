from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators for search results page elements
        self.results_container = (By.CSS_SELECTOR, "div[data-testid='search-results']")
        self.first_product_title = (By.CSS_SELECTOR, "h2[data-testid='product-title']")  # Assuming this locator for product titles
        self.no_results_message = (By.CSS_SELECTOR, "div[data-testid='no-results-message']")

    def check_results_container(self):
        wait = WebDriverWait(self.driver, 10)
        results_element = wait.until(EC.visibility_of_element_located(self.results_container))
        assert results_element.is_displayed(), "Search results container is not displayed."

    def check_first_product_title(self):
        wait = WebDriverWait(self.driver, 10)
        title_element = wait.until(EC.visibility_of_element_located(self.first_product_title))
        assert title_element.is_displayed(), "First product title is not displayed."

    def check_no_results_message(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            no_results_element = wait.until(EC.visibility_of_element_located(self.no_results_message))
            assert no_results_element.is_displayed(), "No results message is not displayed."
        except:
            print("No results message not found, which is expected if there are results.")