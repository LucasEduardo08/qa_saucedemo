import pytest


PRODUCT_NAME = "Noir jacket"


@pytest.mark.name("CT-007 — Remover produto do carrinho")
def test_remover_produto_carrinho(
    home_page,
    product_page,
    cart_page
):

    # Adicionar produto
    home_page.navigate()

    home_page.select_product(PRODUCT_NAME)

    product_page.add_product_to_cart()

    # Validar produto
    assert cart_page.is_product_in_cart(PRODUCT_NAME)

    # Remover
    cart_page.remove_product(PRODUCT_NAME)

    # Resultado esperado
    assert not cart_page.is_product_in_cart(PRODUCT_NAME), (
        f"Product '{PRODUCT_NAME}' was not removed"
    )
    