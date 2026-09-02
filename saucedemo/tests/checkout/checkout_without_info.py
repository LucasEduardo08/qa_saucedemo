@pytest.mark.name("CT-013 — Checkout sem preencher dados")
def test_checkout_campos_vazios(
    home_page,
    product_page,
    cart_page,
    checkout_page
):

    PRODUCT_NAME = "Noir jacket"

    home_page.navigate()

    home_page.select_product(PRODUCT_NAME)

    product_page.add_product_to_cart()

    cart_page.proceed_to_checkout()

    # Não preencher dados
    checkout_page.continue_checkout()

    # Resultado esperado
    assert checkout_page.has_validation_error(), (
        "Validation errors were not displayed"
    )
    