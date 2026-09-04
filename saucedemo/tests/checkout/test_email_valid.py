import pytest


@pytest.mark.parametrize(
    "valid_email",
    [
        "qa@example.com",
        "teste.user@example.com",
        "qa_automation@example.com"
    ]
)
@pytest.mark.name("CT-015 — Validar e-mails válidos")
def test_email_valido(
    valid_email,
    home_page,
    product_page,
    cart_page,
    checkout_page
):

    PRODUCT_NAME = "Noir jacket"

    home_page.navigate()

    home_page.select_product(PRODUCT_NAME)

    product_page.add_product_to_cart()

    cart_page.proceed_to_checkout()

    checkout_page.fill_email(valid_email)

    assert checkout_page.get_email_value() == valid_email