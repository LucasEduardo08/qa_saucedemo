import pytest

@pytest.mark.name("CT-011 — Validar total do carrinho")
def test_validar_total_carrinho(
    home_page,
    product_page,
    cart_page
):

    PRODUCT_1 = "Noir jacket"
    PRODUCT_2 = "Grey jacket"

    home_page.navigate()

    # Produto 1
    home_page.select_product(PRODUCT_1)
    product_page.add_product_to_cart()

    product_page.tap_on_home()

    # Produto 2
    home_page.select_product(PRODUCT_2)
    product_page.add_product_to_cart()

    # Calcular valor esperado
    expected_total = (
        cart_page.get_product_price(PRODUCT_1)
        * cart_page.get_product_quantity(PRODUCT_1)
        +
        cart_page.get_product_price(PRODUCT_2)
        * cart_page.get_product_quantity(PRODUCT_2)
    )

    actual_total = cart_page.get_total()

    assert actual_total == expected_total