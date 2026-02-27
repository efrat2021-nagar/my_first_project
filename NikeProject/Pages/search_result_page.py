from selenium.webdriver.common.by import By

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators: Finding the first shoe product in the list
        self.first_product = (By.CLASS_NAME, "product-card__link-overlay")

    def click_first_result(self):
        self.driver.find_element(*self.first_product).click()