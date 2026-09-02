import pytest


@pytest.mark.parametrize(
    "invalid_email",
    [
        "abc",
        "abc@",
        "abc.com",
        "@email.com"
    ]
)
@pytest.mark.name("CT-014 — Validar e-mails inválidos")
def test_email_invalido(
    invalid_email,
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

    checkout_page.fill_email(invalid_email)

    checkout_page.continue_checkout()

    assert checkout_page.has_email_error(), (
        f"Email '{invalid_email}' should be invalid"
    )