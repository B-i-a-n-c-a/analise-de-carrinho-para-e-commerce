import os
import random
import traceback
from datetime import datetime
from faker import Faker 
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///dados/carrinho.db")
Base = declarative_base()
fake = Faker('pt_BR')
Session = sessionmaker(bind=engine)

session = Session()

class Carrinho(Base):
    __tablename__ = 'carrinho'
    id_item = Column (Integer, primary_key=True, autoincrement=True)
    id_carrinho = Column(Integer)    
    nome_produto = Column(String(100))
    categoria = Column(String(50))
    preco = Column(Float)
    marca_produto = Column(String(50))
    data_favorito = Column(DateTime, default=datetime.now)

class Usuario(Base):
    __tablename__ = 'usuario'
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    cpf = Column(String(14), unique=True)
    sexo = Column(String(1))
    idade = Column(Integer)
    carrinho = Column(Integer)

def cria_tabela():
    if not os.path.exists('dados'): 
        os.makedirs('dados')
    try:
        Base.metadata.create_all(engine)
        session.commit()
        session.close()
    except Exception:
        # informações de erro 
        traceback.print_exc()

def preenche_banco():
    print("Iniciando o povoamento com 50 usuários...")
    
    categorias = ['Eletrônicos', 'Alimentos', 'Limpeza', 'Pet Shop', 'Moda']
    marcas = ['Marca A', 'Marca B', 'Marca C', 'Marca D']

    for i in range(1, 51):
        novo_usuario = Usuario(
            nome=fake.name(),
            cpf=fake.cpf(),
            sexo=random.choice(['M', 'F']),
            idade=random.randint(18, 70),
            carrinho=i 
        )
        session.add(novo_usuario)
        
        for _ in range(random.randint(1, 5)):
            novo_item = Carrinho(
                id_carrinho=i, # Mesmo ID do usuário
                nome_produto=fake.word().capitalize(),
                categoria=random.choice(categorias),
                preco=round(random.uniform(10.0, 500.0), 2),
                marca_produto=random.choice(marcas),
                data_favorito=fake.date_time_between(start_date='-30d', end_date='now')
            )
            session.add(novo_item)
 
    session.commit()
    session.close()


