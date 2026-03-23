from sqlalchemy import select, func
from config_bd.dados_banco import Carrinho, Session

def preco_medio():
    stmt = (select(func.round(func.avg(Carrinho.preco), 2)))
    with Session() as session:
        resultado = session.execute(stmt).scalar()
        print(f"Média total de preço dos produtos no carrinho: {resultado}")
        return resultado

def categoria_frequente():
    categorias = ['Eletrônicos', 'Alimentos', 'Limpeza', 'Pet Shop', 'Moda']
    resultado_final = 0

    with Session() as session:
        for categoria in categorias:
            stmt = (select(func.count(Carrinho.id_carrinho))
                    .where(Carrinho.categoria == categoria))
            resultado = session.execute(stmt).scalar()
            if resultado > resultado_final:
                resultado_final = resultado
                categoria_final = categoria   
   
    print(f"A categoria que mais aparece nos carrinhos é {categoria_final} com {resultado_final} produtos.")
    return resultado_final
                    
def marca_frequente():
    marcas = ['Marca A', 'Marca B', 'Marca C', 'Marca D']
    resultado_final = 0

    with Session() as session:
        for marca in marcas:
            stmt = (select(func.count(Carrinho.id_carrinho))
                    .where(Carrinho.marca_produto == marca))
            resultado = session.execute(stmt).scalar()
            if resultado > resultado_final:
                resultado_final = resultado
                marca_final = marca  

    print(f"A marca que mais aparece nos carrinhos é {marca_final} com {resultado_final} produtos.")
    return resultado_final




    """se stmt for maior que o valor de categoria final, eu substituo o valor atual de 
    cate_final para o valor atual de stmt
    """