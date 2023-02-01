import pymysql
import sqlalchemy as db
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

engine = db.create_engine("mysql+pymysql://root:@localhost:3306/aula02")
Base = declarative_base()

class livro(Base):
    __tablename__ = 'livros'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(90))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

while True:
    print("====== MENU ======")
    menu = int(input(f"Escolha uma opção:\n[1] Inserir\n[2] Alterar\n[3] Consultar\n[4] Deletar\n[5] Sair\n "))
    if menu == 1:
        nome_livro = input(f"Escreva o título do livro que deseja inserir:\n ")
        objeto = livro(titulo=nome_livro)
        session.add(objeto)
        session.commit()
    elif menu == 2:
        consulta = session.query(livro).all()
        for titulo in consulta:
            print(titulo.id, titulo.titulo)
        identificador = int(input("Indique o 'Id' do título que deseja alterar\n"))
        consulta2 = session.query(livro).filter(livro.id == identificador).first()
        titulo_alterado = input("Insira o novo título: ")
        consulta2.titulo = titulo_alterado
        session.add(consulta2)
        session.commit()
        print(f'Pronto! {titulo_alterado} adicionado com sucesso!')
    elif menu == 3:
        consulta = session.query(livro).all()
        for titulo in consulta:
            print(titulo.id, titulo.titulo)
    elif menu == 4:
        consulta = session.query(livro).all()
        for titulo in consulta:
            print(f'{titulo.id} {titulo.titulo}')

        deletando = int(input(f"Indique o 'Id' do livro que deseja DELETAR:\n"))
        consulta = session.query(livro).filter(livro.id == deletando).first()
        session.delete(consulta)
        session.commit()
    elif menu == 5:
        break








