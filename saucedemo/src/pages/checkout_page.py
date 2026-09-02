class CheckoutPage:

    def __init__(self, page):
        self.page = page

        self.email = page.locator("#checkout_email")
        self.first_name = page.locator(
            "#checkout_shipping_address_first_name"
        )
        self.last_name = page.locator(
            "#checkout_shipping_address_last_name"
        )

        self.continue_button = page.get_by_text(
            "Continue"
        )

    def is_checkout_page(self):
        return self.email.is_visible()

    def fill_email(self, email):
        self.email.fill(email)

    def fill_first_name(self, name):
        self.first_name.fill(name)

    def fill_last_name(self, last_name):
        self.last_name.fill(last_name)

    def continue_checkout(self):
        self.continue_button.click()

    def has_validation_error(self):
        return self.page.locator(
            "[role='alert']"
        ).is_visible()

    def has_email_error(self):
        return self.page.locator(
            "#error-for-email"
        ).is_visible()

    def get_email_value(self):
        return self.email.input_value()
    