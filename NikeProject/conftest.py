import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    # Advanced settings to prevent bot detection
    chrome_options = Options()

    # Removes the "controlled by automated software" flag
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # Setting a standard browser User-Agent
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

    # Initialize Chrome with options
    driver = webdriver.Chrome(options=chrome_options)

    # JavaScript command to further hide the 'webdriver' property
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    # Close browser after test session
    driver.quit()