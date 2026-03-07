
    class CartPage:
        def __init__(self, page):
            self.page = page

        def open_cart(self):
            print("Opening cart")

            cart_button = self.page.locator("[data-testid='cart-button']")
            cart_button.click()

            self.page.wait_for_load_state("load")

        def check_product_in_cart(self):
            print("Checking product in cart")

            cart_products = self.page.locator("[data-testid='cart-item']")
            count = cart_products.count()

            print(f"Products in cart: {count}")

        def check_product_info(self):
            print("Checking product information")

            product = self.page.locator("[data-testid='cart-item']").first

            title = product.locator("a").inner_text()
            price = product.locator("[data-testid='product-price']").inner_text()

            print(f"Product: {title}, Price: {price}")

