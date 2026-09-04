import pytest


@pytest.mark.name("CT-010 — Validar subtotal do carrinho")
def test_validar_subtotal(
    home_page,
    product_page,
    cart_page
):

    PRODUCT_NAME = "Noir jacket"

    home_page.navigate()

    home_page.select_product(PRODUCT_NAME)

    product_page.add_product_to_cart()

    cart_page.update_quantity(
        PRODUCT_NAME,
        quantity=2
    )

    price = cart_page.get_product_price(PRODUCT_NAME)

    quantity = cart_page.get_product_quantity(PRODUCT_NAME)

    expected_subtotal = price * quantity

    actual_subtotal = cart_page.get_subtotal()

    assert actual_subtotal == expected_subtotal, (
        f"Expected subtotal {expected_subtotal}, "
        f"but got {actual_subtotal}"
    )
    