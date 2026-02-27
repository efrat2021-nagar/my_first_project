from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        # New, more reliable locators for Nike
        self.search_button = (By.ID, "VisualSearchInput")  # The clickable area
        self.accept_cookies_btn = (By.XPATH, "//button[contains(@data-testid, 'advisory-banner-dismiss-btn')]")

    def load(self):
        self.driver.get("https://www.nike.com/il/")
        self.dismiss_cookies()

    def dismiss_cookies(self):
        try:
            wait = WebDriverWait(self.driver, 5)
            cookie_btn = wait.until(EC.element_to_be_clickable(self.accept_cookies_btn))
            cookie_btn.click()
            print("Cookies banner dismissed.")
        except:
            print("No cookies banner found.")

    def search_for(self, item_name):
        wait = WebDriverWait(self.driver, 15)

        # 1. Wait for the search element to be present
        search_element = wait.until(EC.element_to_be_clickable(self.search_button))

        # 2. Click it to make sure it's active
        search_element.click()

        # 3. Type the text and press Enter
        search_element.send_keys(item_name)
        search_element.send_keys(Keys.ENTER)
        print(f"Typed '{item_name}' and pressed Enter.")