from datetime import date, datetime
import mysql.connector
import conexao

db_connection = conexao.conectar()
con = db_connection.cursor()


def insert(nome, telefone, endereco, dataAtual):
    try:
        dataAtual = transformarTexto(dataAtual)
        sql = "insert into pessoa(codigo, nome, telefone, endereco, dataAtual) values('','{}','{}','{}','{}')".format(nome, telefone, endereco, dataAtual)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Inserido!")
    except Exception as erro:
        print(erro)

def selecionar():
    try:
        sel = ("Select * from pessoa")
        con.execute(sel)

        for (codigo, nome, telefone, endereco, dataAtual) in con:
            print(codigo, nome, telefone, endereco, dataAtual)
        print("\n")
    except Exception as erro:
        print(erro)

def atualizarNome(codigo, nome):
    try:
        atu = "update pessoa set nome = '{}' where codigo = '{}'".format(nome,codigo)
        con.execute(atu)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)

def excluir(codigo):
    try:
        exc = "delete from pessoa where codigo = {}".format(codigo)
        con.execute(exc)
        db_connection.commit()
        print(con.rowcount, "Deletada!")
    except Exception as erro:
        print(erro)

def transformarTexto(texto):
    separado = texto.split('/')
    ano = separado[2]
    mes = separado[1]
    dia = separado[0]
    return '{}-{}-{}'.format(ano, mes, dia)