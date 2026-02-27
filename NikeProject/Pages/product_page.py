from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators: Product title and Add to Cart button
        self.product_title = (By.ID, "pdp_product_title")
        self.add_to_cart_btn = (By.XPATH, "//button[@aria-label='Add to Bag']")

    def get_product_name(self):
        return self.driver.find_element(*self.product_title).text