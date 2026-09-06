import pytest
from playwright.sync_api import sync_playwright, expect
from src.pages.home import HomePage
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        # headless=False permite ver o navegador abrindo na sua tela
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def product_page(page):
    return ProductPage(page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)

@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)
