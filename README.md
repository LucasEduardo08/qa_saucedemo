# QA SauceDemo

Projeto de automação de testes em Quality Assurance (QA) para avaliação do site Sauce Demo.

O objetivo do projeto é validar as principais funcionalidades de um e-commerce, simulando ações realizadas por usuários e verificando se o sistema atende aos comportamentos esperados.

Os testes foram realizados utilizando o site [Sauce Demo](https://sauce-demo.myshopify.com/) como aplicação de estudo.

## Tecnologias utilizadas

- Python
- Pytest
- Playwright
- Poetry

## Tipo de testes

O projeto é composto por testes funcionais End-to-End (E2E).

Os testes simulam a interação do usuário com a aplicação através do navegador, validando funcionalidades como:

- Navegação entre páginas;
- Visualização de produtos;
- Seleção de produtos;
- Adição de produtos ao carrinho;
- Funcionalidades do carrinho;
- Processo de checkout.

## Estrutura do projeto

```text
qa_saucedemo/
│
├── saucedemo/
│   ├── src/
│   │   └── saucedemo/
│   │       └── pages/
│   │
│   └── tests/
│       ├── checkout/
│       ├── navigate/
│       └── products/
│
├── pyproject.toml
├── poetry.lock
├── pytest.ini
└── README.md
