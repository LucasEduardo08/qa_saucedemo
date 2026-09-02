class ProductPage:
    def __init__(self, page):
        self.page = page
        self.product = page.locator("section[id='buy']")
        self.price_product = page.locator("span[class='product-price']")
        self.add_to_cart = page.locator("input[value='Add to Cart']")
        self.home = page.locator("nav")

    def is_product_selected(self, product_name) -> bool:
        """
        product_name: Product's name
        """
        return bool(self.product.locator("h1", has_text=product_name))

    def has_price(self) -> bool:
        return self.price_product.is_visible()

    def has_add_to_cart(self) -> bool:
        return self.add_to_cart.is_visible()

    def tap_on_home(self):
        self.home.locator("a[href='/']").click()

    def add_product_to_cart(self):
        self.add_to_cart.click()

    def remove_product(self, product_name):
        self.page.locator(
            "tr",
            has_text=product_name
        ).get_by_text("Remove").click()
