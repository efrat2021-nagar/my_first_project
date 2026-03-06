from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Homepage:
    def __init__(self,page):
        self.page = page

    def load(self):
        print("Opening Nike homepage")
        self.page.goto("https://www.nike.com/il/")

    def search_for_item(self,item):
        print(f"trying to search for {item}")

        search_icon = self.page.locator("[id='nav-search-icon']")
        search_icon.click()
        search_menu = self.page.locator("[id='id=gn-search-input']")
        search_menu.click()
        search_menu.fill(item)
        page.keyboard.press('Enter')
