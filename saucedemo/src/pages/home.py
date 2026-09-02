class HomePage:
    def __init__(self, page):
        self.page = page
        self.search = page.locator("a[href='/search']")  # Se quiser pegar o texto, .inner_text()
        self.about_us = page.locator("a[href='/pages/about-us']")
        self.products_list = page.locator("section[class='product-grid twelve columns alpha omega']")

    def navigate(self):
        self.page.goto("https://sauce-demo.myshopify.com/")

    def select_product(self, product_name=None):
        """
        product_name: Product's name       
        """
        if product_name:
            self.products_list.locator("h3", has_text=product_name).click()
        else:
            self.products_list.locator("div[class='four columns alpha']").click()
