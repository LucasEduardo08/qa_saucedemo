import pytest

@pytest.mark.name("CT-001 — Acessar a página inicial")
def test_acessar_home(home_page):
    # Passo 1: Abrir o navegador.
    # Passo 2: Acessar o site.
    # Passo 3: Aguardar o carregamento.
    home_page.navigate()
    