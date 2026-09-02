class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart = page.locator("#cart")
        self.checkout_button = page.locator(
            "input[name='checkout']"
        )

    def is_product_in_cart(self, product_name):
        return self.page.get_by_text(
            product_name,
            exact=True
        ).is_visible()

    def get_product_quantity(self):
        return self.page.locator(
            "input[type='number']"
        ).input_value()

    def remove_product(self, product_name):
        product = self.page.locator(
            ".cart-item",
            has_text=product_name
        )

        product.locator(
            "a",
            has_text="Remove"
        ).click()

    def proceed_to_checkout(self):
        self.checkout_button.click()

    def is_cart_empty(self):
        return self.page.get_by_text(
            "Your cart is currently empty"
        ).is_visible()

    def update_quantity(self, product_name, quantity):
        product = self.page.locator(
            "tr",
            has_text=product_name
        )

        quantity_input = product.locator(
            "input[type='number']"
        )

        quantity_input.fill(str(quantity))

        quantity_input.press("Enter")

    def get_product_price(self, product_name):
        product = self.page.locator(
            "tr",
            has_text=product_name
        )

        price_text = product.locator(
            ".price"
        ).inner_text()

        return float(
            price_text
            .replace("£", "")
            .strip()
        )

    def get_product_quantity(self, product_name):
        product = self.page.locator(
            "tr",
            has_text=product_name
        )

        return int(
            product.locator(
                "input[type='number']"
            ).input_value()
        )

    def get_subtotal(self):
        subtotal = self.page.locator(
            ".subtotal"
        ).inner_text()

        return float(
            subtotal
            .replace("£", "")
            .strip()
        )

    def proceed_to_checkout(self):
        self.checkout_button.click()
