import pytest


@pytest.mark.name("CT-012 — Ir para checkout")
def test_ir_para_checkout(
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

    assert checkout_page.is_checkout_page(), (
        "User was not redirected to checkout"
    )
    