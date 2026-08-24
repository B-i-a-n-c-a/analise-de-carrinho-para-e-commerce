# 🛒 Análise de Carrinho para E-commerce

Sistema de análise de comportamento de compra de usuários em e-commerce, com geração de dados sintéticos e extração de métricas via SQL/ORM para apoiar decisões estratégicas de negócio.

---

## 📌 Sobre o Projeto

Este projeto simula um ambiente de e-commerce com dados fictícios de usuários e seus carrinhos de compra, permitindo extrair **insights sobre padrões de consumo**. A ideia central é entender quais produtos, categorias e marcas aparecem com mais frequência nos carrinhos, além de cruzar essas informações com o perfil demográfico dos compradores.

Os dados são gerados automaticamente com a biblioteca **Faker** (em português brasileiro) e armazenados em um banco **SQLite** local. As análises são feitas diretamente via queries SQL construídas com **SQLAlchemy 2.0**.

---

## 🗂️ Estrutura do Projeto

```
analise-de-carrinho-para-e-commerce/
├── dados/
│   └── carrinho.db              # Banco de dados SQLite gerado automaticamente
├── src/
│   ├── main.py                  # Ponto de entrada — popula o banco de dados
│   ├── config_bd/
│   │   ├── __init__.py
│   │   └── dados_banco.py       # Modelos ORM (Carrinho, Usuario) e funções de setup
│   └── analises/
│       ├── metricas_usuario.py  # Métricas de perfil dos usuários
│       ├── metricas_carrinho.py # Métricas dos itens no carrinho
│       └── metricas_cruzadas.py # Análises cruzadas (usuário × carrinho)
├── requeriments.txt
└── README.md
```

---

## ⚙️ Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3 | Linguagem principal |
| SQLite | Banco de dados local |
| SQLAlchemy 2.0 | ORM para criação e consulta das tabelas |
| Faker (`pt_BR`) | Geração de dados fictícios em português |
| Pandas / NumPy | Suporte a operações de dados |

---

## 📊 Funcionalidades e Métricas

### 👤 `metricas_usuario.py` — Perfil dos compradores
- Distribuição de usuários por **sexo**
- **Média de idade** dos usuários
- Contagem por **faixa etária** (18–29, 30–39, 40–49, 50–59, 60–69, 70–79)

### 🛒 `metricas_carrinho.py` — Comportamento de compra
- **Preço médio** dos produtos adicionados ao carrinho
- **Categoria mais frequente** entre os itens
- **Marca com maior volume** de aparições

### 🔀 `metricas_cruzadas.py` — Cruzamento usuário × carrinho
- **Gasto médio por sexo** (join entre tabelas `usuario` e `carrinho`)
- **Categoria favorita por faixa etária** (Jovens, Adultos Jovens, Adultos, Idosos)

---

## 🚀 Como executar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/analise-de-carrinho-para-e-commerce.git
cd analise-de-carrinho-para-e-commerce
```

### 2. Crie e ative um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requeriments.txt
```

### 4. Popule o banco de dados
```bash
cd src
python main.py
```

> Isso criará o arquivo `dados/carrinho.db` e o populará com **50 usuários** e seus respectivos itens de carrinho (entre 1 e 5 itens por usuário), gerados aleatoriamente.

### 5. Execute as análises desejadas
Importe e chame as funções diretamente no terminal Python ou em um script:

```python
from analises.metricas_carrinho import preco_medio, categoria_frequente, marca_frequente
from analises.metricas_usuario import definicao_Publico, media_Idade, faixa_etaria
from analises.metricas_cruzadas import gasto_medio_por_sexo, categoria_favorita_por_idade
```

---

## 🗃️ Modelo de Dados

**Tabela `usuario`**

| Campo | Tipo | Descrição |
|---|---|---|
| id_usuario | Integer (PK) | Identificador único |
| nome | String | Nome gerado pelo Faker |
| cpf | String | CPF fictício único |
| sexo | String (M/F) | Sexo do usuário |
| idade | Integer | Idade (18–70) |
| carrinho | Integer | Referência ao carrinho do usuário |

**Tabela `carrinho`**

| Campo | Tipo | Descrição |
|---|---|---|
| id_item | Integer (PK) | Identificador do item |
| id_carrinho | Integer | Referência ao usuário dono do carrinho |
| nome_produto | String | Nome do produto |
| categoria | String | Eletrônicos, Alimentos, Limpeza, Pet Shop ou Moda |
| preco | Float | Preço entre R$ 10,00 e R$ 500,00 |
| marca_produto | String | Marca A, B, C ou D |
| data_favorito | DateTime | Data em que o item foi adicionado |
