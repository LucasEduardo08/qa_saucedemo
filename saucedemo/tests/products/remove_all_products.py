import pytest


PRODUCT_1 = "Noir jacket"
PRODUCT_2 = "Grey jacket"


@pytest.mark.name("CT-008 — Remover todos os produtos do carrinho")
def test_remover_todos_produtos(
    home_page,
    product_page,
    cart_page
):

    home_page.navigate()

    # Produto 1
    home_page.select_product(PRODUCT_1)
    product_page.add_product_to_cart()

    product_page.tap_on_home()

    # Produto 2
    home_page.select_product(PRODUCT_2)
    product_page.add_product_to_cart()

    # Remover produtos
    cart_page.remove_product(PRODUCT_1)
    cart_page.remove_product(PRODUCT_2)

    # Resultado esperado
    assert cart_page.is_cart_empty(), (
        "Cart should be empty"
    )
    