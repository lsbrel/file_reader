import mysql.connector as mysql
from dotenv import load_dotenv
import os


class Database:

    ### CLASSSE QUE VAI TRATAR DE FAZER A CONEXAO COM O BANCO DE DADOS
    ### BUSCANDO OS DADOS DA VARIAVEL DE AMBIENTE .env

    def __init__(self) -> None:
        # carregando variaveis de ambiente
        load_dotenv()
        self.sql_connection = mysql.connect(
            host = os.environ['DB_HOST'],
            user = os.environ['DB_USER'],
            password = os.environ['DB_PASSWORD'],
            database = os.environ['DB_DATABASE']
        )


    def getCursor(self):
        return self.sql_connection.cursor()

    def store(self):
        self.sql_connection.commit()
