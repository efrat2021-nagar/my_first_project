from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators for product page elements
        self.product_title = (By.CSS_SELECTOR, "h1[data-testid='product-title']")
        self.product_price = (By.CSS_SELECTOR, "div[data-testid='product-price']")
        self.add_to_cart_button = (By.XPATH, "//button[contains(text(), 'Add to Cart')]")
        self.product_image = (By.CSS_SELECTOR, "img[data-testid='product-image']")

    def check_product_title(self):
        wait = WebDriverWait(self.driver, 10)
        title_element = wait.until(EC.visibility_of_element_located(self.product_title))
        assert title_element.is_displayed(), "Product title is not displayed."

    def check_product_price(self):
        wait = WebDriverWait(self.driver, 10)
        price_element = wait.until(EC.visibility_of_element_located(self.product_price))
        assert price_element.is_displayed(), "Product price is not displayed."

    def check_add_to_cart_button(self):
        wait = WebDriverWait(self.driver, 10)
        button_element = wait.until(EC.element_to_be_clickable(self.add_to_cart_button))
        assert button_element.is_displayed(), "Add to Cart button is not displayed."

    def check_product_image(self):
        wait = WebDriverWait(self.driver, 10)
        image_element = wait.until(EC.visibility_of_element_located(self.product_image))
        assert image_element.is_displayed(), "Product image is not displayed."