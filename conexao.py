import mysql.connector
from mysql.connector import errorcode
import this
this.con = ""

def conectar():
    try:
        db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='bancoDeDados')
        print('Conectado com sucesso!')
        return db_connection
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print('Banco de Dados não existe')
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Nome de usuário ou senha não são válidos!')
        else:
            print(error)
    else:
        db_connection.close()

