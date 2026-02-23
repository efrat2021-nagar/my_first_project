from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.ebay.com/")

    search =page.locator("[id='gh-ac']")
    search.click()
    search.fill("Camera")
    search_button = page.locator("[id='gh-ac']")
    search_button.click()
    # page.keyboard.press("Enter")
    current_url = page.url
    assert page.url.__contains__('ebay'),'page URL did not contains E0bay after search'

    browser.close()
    print ("Test end")