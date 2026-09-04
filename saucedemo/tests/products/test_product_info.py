import pytest

PRODUCT_NAME = "Noir jacket"


@pytest.mark.name("CT-004 — Validar informações do produto")
def test_validar_informacoes_produto(home_page, product_page):

    # Passo 1: Acessar a página inicial
    home_page.navigate()

    # Passo 2: Selecionar produto
    home_page.select_product(PRODUCT_NAME)

    # Resultados esperados
    assert product_page.is_product_selected(PRODUCT_NAME), (
        f"Product '{PRODUCT_NAME}' was not displayed"
    )

    assert product_page.has_price(), (
        "Product price was not displayed"
    )

    assert product_page.has_add_to_cart(), (
        "Add to Cart button was not displayed"
    )