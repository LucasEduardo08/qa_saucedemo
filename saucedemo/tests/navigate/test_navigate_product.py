import pytest

PRODUCT_NAME = "Noir jacket"

@pytest.mark.name("CT-002 — Navegar para um produto")
def test_selecionar_produto(home_page, product_page):
    # Passo 1: Acessar a página inicial
    home_page.navigate()

    # Passo 2: Clicar em um produto.
    home_page.select_product(PRODUCT_NAME)
    assert product_page.is_product_selected(PRODUCT_NAME), f"The {PRODUCT_NAME} product ins't show"
    assert product_page.has_price(), f"The {PRODUCT_NAME} product haven't price"
    assert product_page.has_add_to_cart(), f"The {PRODUCT_NAME} product haven't ADD TO CART button"
