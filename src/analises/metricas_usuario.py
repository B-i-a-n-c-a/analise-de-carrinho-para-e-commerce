from sqlalchemy import select, func, or_
from config_bd.dados_banco import Usuario, Session

def definicao_Publico():
   stmt = (select(Usuario.sexo, func.count(Usuario.id_usuario)).group_by(Usuario.sexo))
   with Session() as session:
       resultado = session.execute(stmt).all()
       for sexo, quantidade in resultado:
           print(f"Sexo: {sexo} - Quantidade: {quantidade}")
          
       return resultado

def media_Idade():
    with Session() as session:
        stmt = select(func.avg(Usuario.idade))
        resultado = session.execute(stmt).scalar()
        print(f"A média de idade dos usuários é de: {resultado}")
        return resultado

def faixa_etaria():
    intervalos = [(18, 29), (30, 39), (40, 49), (50, 59), (60, 69), (70, 79)]

    with Session() as session:     
        for inicio, fim in intervalos:
            stmt = select(func.count(Usuario.id_usuario)).where(or_
            (Usuario.idade.between(inicio, fim)))
            total_faixa = session.execute(stmt).scalar()
            print(f"Faixa de idade entre [{inicio}, {fim}] possui {total_faixa} usuarios")


    
        