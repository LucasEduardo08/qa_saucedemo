# QA SauceDemo - SauceDemo

Projeto de automação de testes funcionais End-to-End (E2E) desenvolvido
para validação de uma aplicação de e-commerce.

O projeto tem como objetivo aplicar práticas de Quality Assurance (QA),
automação de testes e integração contínua, simulando cenários de uso
realizados por usuários em uma aplicação web.

A aplicação utilizada para os testes é o [Sauce Demo](https://sauce-demo.myshopify.com/),
utilizado como ambiente de estudo para automação de testes.

## Tecnologias utilizadas

- Python
- Pytest
- Playwright
- Poetry
- Docker
- GitHub Actions

## Testes automatizados

Os testes são realizados utilizando o navegador e simulam interações
de usuários com a aplicação.

Os principais cenários contemplados são:

- Navegação entre páginas;
- Visualização de produtos;
- Seleção de produtos;
- Adição de produtos ao carrinho;
- Remoção de produtos do carrinho;
- Validação do carrinho;
- Processo de checkout;
- Navegação entre diferentes páginas da aplicação.

## Estrutura do projeto

```text
qa_saucedemo/
│
├── saucedemo/
│   ├── src/
│   │   └── saucedemo/
│   │       └── pages/
│   │
│   ├── tests/
│   │   ├── checkout/
│   │   ├── navigate/
│   │   └── products/
│   │
│   ├── Dockerfile
│   ├── pyproject.toml
│   ├── poetry.lock
│   └── pytest.ini
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── reports/
│
├── .gitignore
└── README.md