import pytest

@pytest.mark.name("CT-009 — Alterar quantidade do produto")
def test_alterar_quantidade_produto(
    home_page,
    product_page,
    cart_page
):

    PRODUCT_NAME = "Noir jacket"

    home_page.navigate()

    home_page.select_product(PRODUCT_NAME)

    product_page.add_product_to_cart()

    # Alterar quantidade
    cart_page.update_quantity(
        PRODUCT_NAME,
        quantity=2
    )

    # Resultado esperado
    assert cart_page.get_product_quantity(
        PRODUCT_NAME
    ) == "2"
    