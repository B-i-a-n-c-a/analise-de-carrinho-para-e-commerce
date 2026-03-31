# Projeto: Análise de carrinhos para e-commerce

## Objetivo:

Desenvolver um pequeno sistema que permita a verificação dos itens de compra que mais são adicionados ao carrinho a fim de entender melhor as escolhas dos consumidores e centralizar estratégias que possam trazer mais efetividade de compra para os produtos frequentemente adicionados ao carrinho.

## 🛠 Tecnologias
* **Linguagem**: Lingua Python
* **Banco de Dados**: SQL
* **ORM**: SQLAlchemy 2.0
* **Biblioteca**: Faker


## 📁 Arquitetura e organização das pastas
```src/config_bd```: Configuração de conexão e modelos.

```src/analises```: Lógica de extração de métricas e SQL.

```src/dados```: Local onde o banco SQLite é gerado.

## 💻 Funcionalidades principais 
Métricas agrupadas por entidade ou por objetivo. 

1. `analises/metricas_usuario.py`

* Cálculo de média de idade.
* Distribuição por sexo.
* Contagem de usuários por faixa etária.

2. `analises/metricas_carrinho.py`

* Preço médio dos produtos.
* Categorias mais frequentes.
* Marcas com maior volume.

3. `analises/metricas_cruzadas.py`

* Gasto médio por sexo.
* Categorias favoritas por idade.



