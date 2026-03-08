import pytest
from playwright.sync_api import sync_playwright

URL = "https://www.nike.com"


@pytest.fixture(scope="session")
def setup_playwright_project():
    print("starting playwright")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(URL)

        yield page
        page.close()
        browser.close()
        print("####Test end###")
