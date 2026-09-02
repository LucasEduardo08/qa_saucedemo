import pytest


@pytest.mark.name("CT-016 — Atualizar página mantendo produto no carrinho")
def test_atualizar_pagina_carrinho(
    home_page,
    product_page,
    cart_page,
    page
):

    PRODUCT_NAME = "Noir jacket"

    home_page.navigate()

    home_page.select_product(PRODUCT_NAME)

    product_page.add_product_to_cart()

    # Atualizar página
    page.reload()

    # Produto deve continuar no carrinho
    assert cart_page.is_product_in_cart(PRODUCT_NAME), (
        "Product disappeared after page reload"
    )
