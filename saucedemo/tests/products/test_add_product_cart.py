import pytest


PRODUCT_NAME = "Noir jacket"


@pytest.mark.name("CT-005 — Adicionar produto ao carrinho")
def test_adicionar_produto_carrinho(
    home_page,
    product_page,
    cart_page
):

    # Passo 1: Acessar página inicial
    home_page.navigate()

    # Passo 2: Selecionar produto
    home_page.select_product(PRODUCT_NAME)

    # Passo 3: Adicionar ao carrinho
    product_page.add_product_to_cart()

    # Resultado esperado
    assert cart_page.is_product_in_cart(PRODUCT_NAME), (
        f"Product '{PRODUCT_NAME}' was not added to cart"
    )
    