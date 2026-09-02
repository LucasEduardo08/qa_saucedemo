import pytest
from playwright.sync_api import sync_playwright, expect
from src.pages.login_page import LoginPage
from src.pages.home import HomePage
from src.pages.product_page import ProductPage

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        # headless=False permite ver o navegador abrindo na sua tela
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def product_page(page):
    return ProductPage(page)
