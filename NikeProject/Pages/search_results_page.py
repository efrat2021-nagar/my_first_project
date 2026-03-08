import time


class search_results_page:
    def __init__(self,page):
        self.page = page

    def search_for_item(self,item: str):
        search_menu = self.page.locator("[id-'gn-search-input']")
        search_menu.click()
        search_menu.fill('item')
        search_menu.prees('Enter')

    def check_football_category(self,item: str):
        categories = self.page.locator("text=Football")
        count = categories.count()
        if count > 0:
           print("Football category exists")
           return True
        else:
           print("Football category NOT found")
           return False

    def check_products_have_info(self):
        print("checking that every product has information")
        time.sleep(3)

        products = self.page.locator("[data-testid='product-card']")
        count = products.count()

        print(f"Found {count} products")

        for i in range(count):
            product = products.nth(i)
            title = product.locator("a").text_content()
            price = product.locator("[data-testid='product-price']").text_content()
            image = product.locator("img").get_attribute("src")

            print(f"Product {i + 1}: {title} | {price}")




