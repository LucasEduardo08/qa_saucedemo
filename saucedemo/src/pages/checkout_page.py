class CheckoutPage:

    def __init__(self, page):
        self.page = page
        self.cart = page.locator("a[class='active']")
        self.continue_button = page.get_by_text("Continue")
        self.product_on_cart = page.locator("div[class='twelve columns alpha omega']")

    def is_checkout_page(self):
        return self.cart.is_visible()

    def is_product_in_cart(self, product_name):
        return self.product_on_cart.filter(has_text=product_name)

    def continue_checkout(self):
        self.continue_button.click()

    def has_validation_error(self):
        return self.page.locator(
            "[role='alert']"
        ).is_visible()
    