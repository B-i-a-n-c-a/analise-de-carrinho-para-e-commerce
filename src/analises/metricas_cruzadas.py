from sqlalchemy import select, func, case, asc
from config_bd.dados_banco import Carrinho, Usuario, Session
from analises.metricas_usuario import faixa_etaria

def gasto_medio_por_sexo():
    with Session() as session:
        stmt = (select(Usuario.sexo, func.round(func.avg(Carrinho.preco), 2).label("media_preco"))
            .join(Carrinho, Carrinho.id_carrinho == Usuario.id_usuario)
            .group_by(Usuario.sexo)
            .order_by(Usuario.sexo)
        )
        resultado = session.execute(stmt).all()
        for valor in resultado:
            print(f"Sexo {valor.sexo} possui média de valor no carrinho de {valor.media_preco} reais")

def categoria_favorita_por_idade():
    condicao_faixa = case(
        (Usuario.idade <= 18, "Jovens"),
        (Usuario.idade <= 35, "Adultos Jovens"),
        (Usuario.idade <= 60, "Adultos"),
        else_="Idosos"
    ).label("faixa_etaria")

    with Session() as session:
        stmt = (
            select(
                condicao_faixa, Carrinho.categoria, func.count(Carrinho.id_carrinho).label("total")
            )
                .join(Usuario, Usuario.id_usuario == Carrinho.id_carrinho)
                .group_by("faixa_etaria", Carrinho.categoria)
                .order_by("faixa_etaria", asc("total"))
        )
        resultado = session.execute(stmt).all()
        imprimir_vendas_por_faixa(resultado)

def imprimir_vendas_por_faixa(tuplas):
    print(f"{'FAIXA ETÁRIA':<20} | {'CATEGORIA LÍDER':<20} | {'VENDAS':<10}")
    print("-" * 55)
    
    for linhas in tuplas:
        print(f"{linhas.faixa_etaria:<20} | {linhas.categoria:<20} | {linhas.total:<10}")