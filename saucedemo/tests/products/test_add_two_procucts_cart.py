import pytest


PRODUCT_1 = "Noir jacket"
PRODUCT_2 = "Grey jacket"


@pytest.mark.name("CT-006 — Adicionar dois produtos ao carrinho")
def test_adicionar_dois_produtos(
    home_page,
    product_page,
    cart_page
):

    # Produto 1
    home_page.navigate()
    home_page.select_product(PRODUCT_1)

    product_page.add_product_to_cart()

    # Voltar para home
    product_page.tap_on_home()

    # Produto 2
    home_page.select_product(PRODUCT_2)

    product_page.add_product_to_cart()

    # Validações
    assert cart_page.is_product_in_cart(PRODUCT_1), (
        f"Product '{PRODUCT_1}' was not added"
    )

    assert cart_page.is_product_in_cart(PRODUCT_2), (
        f"Product '{PRODUCT_2}' was not added"
    )
    