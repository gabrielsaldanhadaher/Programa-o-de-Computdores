# 📈 Simulador de Investimentos em Bancos

## 📝 Descrição do Projeto

Este projeto consiste em uma aplicação de análise financeira que simula investimentos em ações de bancos brasileiros listados na bolsa de valores. O sistema permite ao usuário selecionar duas instituições bancárias e comparar visualmente a evolução de um investimento ao longo do tempo com base em dados reais do mercado.

Desenvolvido como parte de estudos em **Python para análise de dados e visualização financeira**, o sistema coleta informações históricas diretamente do mercado financeiro, calcula retornos percentuais diários e simula o crescimento de uma carteira de investimentos.

O objetivo principal é demonstrar, de forma prática, conceitos como:

- Coleta de dados financeiros em tempo real
- Cálculo de rentabilidade
- Simulação de carteira de investimentos
- Visualização interativa de dados

---

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python 3.14.3

* **Bibliotecas:**
  * NumPy
  * Pandas
  * Plotly
  * yFinance

* **Ferramentas:**
  * Visual Studio Code
  * Jupyter Notebook (opcional)

---

## ⚙️ Funcionalidades do Sistema

O programa executa automaticamente as seguintes etapas:

✔ Exibe uma lista de bancos disponíveis para investimento.

✔ Permite ao usuário selecionar dois ativos bancários.

✔ Baixa dados históricos reais da bolsa de valores.

✔ Calcula os retornos percentuais diários.

✔ Simula um investimento inicial de **R$ 10.000** dividido igualmente entre os ativos.

✔ Gera um gráfico interativo comparando:

- Evolução individual de cada banco
- Performance da carteira combinada

---

## 📊 Resultados e Aprendizados

Durante o desenvolvimento, foi possível aplicar diversos conceitos de programação e análise de dados:

* **Integração com APIs financeiras:** Uso do Yahoo Finance para obtenção de dados reais.

* **Tratamento de exceções:** Implementação de validações para evitar falhas de conexão ou ativos inválidos.

* **Modelagem matemática:** Cálculo de retornos percentuais e composição de carteira.

* **Visualização interativa:** Uso do Plotly para gerar gráficos com zoom, hover e filtros visuais.

---

## 🏦 Bancos Disponíveis

Atualmente, o sistema permite simulação com:

- Itaú (`ITUB4.SA`)
- Bradesco (`BBDC4.SA`)
- Banco do Brasil (`BBAS3.SA`)
- Santander (`SANB11.SA`)

---

## 🔧 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
