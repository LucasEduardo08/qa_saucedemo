import pytest

PRODUCT_NAME = "Noir jacket"

@pytest.mark.name("CT-003 — Voltar para a página anterior")
def test_selecionar_produto(home_page, product_page, page):
    # Passo 1: Acessar um produto.
    home_page.navigate()
    home_page.select_product(PRODUCT_NAME)

    # Passo 2: Utilizar o botão "Voltar" do navegador
    with page.expect_navigation() as navigation_info:
        product_page.tap_on_home()
    assert navigation_info.value.url == "https://sauce-demo.myshopify.com/", "The current screen ins't home page"
