from faker import Faker
from faker.providers import DynamicProvider
from random import randint
import psycopg2
from dotenv import load_dotenv
import os

fake = Faker('pt_BR')

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

#Funções ligadas ao banco
def inserção(dicionario, tabela): #função para inserção de dados no banco de dados. Virou função para ter mais reusabilidade sem sujar o código inteiro. TEM QUE ESTAR DEPOIS DA CONEXÃO COM O BANCO. 
        """
        Inserção dos dados vindos de um dicionário para dentro do banco de dados.

        Args:
            dicionario(string): dicionario do qual serão retiradas as informações para inserir no banco de dados
            tabela(string): nome da coluna da tabela do banco de dados na qual serão inseridos os dados do dicionário 

        Returns:
        nada kkkkkkk
        """
        tabelaNome = tabela #tabela na qual as informações serão inseridas
        query = "INSERT INTO " + tabelaNome + "("  #começo da query
        query1 = "" #query com todas as colunas
        query2 = "" #query com todos os valores que serão inseridos
        for chave, valor in dicionario.items(): #navegar pelo dicionario para adicionar os nomes e valores à query
            query1+=   chave + "," #string das colunas exemplo: nome,id,departamento,RA,
            query2+= "'" + valor + "'" + "," #string dos valores | exemplo: jeremias,1234,robotica,24.123.035-8
        query1 = query1.rstrip(",") # tira a última vírgula da string | exemplo: ANTES: nome,id,departamento,RA,  DEPOIS: nome,id,departamento,RA
        query2 = query2.rstrip(",") #mesma coisa do comentário acima(linha 48)

        print(query1) #imprimir cada parte da query para ver como está 
        print(query2)
        query+= query1 + ") VALUES ("  #final da parte INSERT INTO tabela(coluna1,coluna2,coluna3) e começo da inserção dos valores
        query+= query2 + ")" #inserção dos valores na query e fechamento de parenteses do VALUES()
        print(query) #imprimir query completa para checar

    

        cursor.execute(query) #execução da query para inserir no banco de dados 
        cursor.execute("commit") # confirmação da alteração no banco de dados 
def resetarDB():
        cursor.execute('ALTER TABLE filme DROP CONSTRAINT IF EXISTS id;')
        tabelas = [
        'gravacao',
        'elenco',
        'filme',
        'producao',
        'roteirista',
        'diretor',
        'produtor',
        'ator'
        ]
        for tabela in tabelas:
            cursor.execute(f'DROP TABLE IF EXISTS {tabela} CASCADE;')
        cursor.execute("commit")
def criarDB():
     cursor.execute("""
        create table ator(
            id varchar(10)
            ,nome varchar(30)
            ,sexo varchar(10)
            ,idade varchar(3)
            ,primary key (id)
        );

        create table produtor(
            id varchar(10)
            ,nome varchar(30)
            ,sexo varchar(10)
            ,idade varchar(3)
            ,categoria varchar(30)
            ,primary key (id)
        );

        create table diretor(
            id varchar(10)
            ,nome varchar(30)
            ,sexo varchar(10)
            ,idade varchar(3)
            ,primary key (id)
        );

        create table roteirista(
            id varchar(10)
            ,nome varchar(30)
            ,sexo varchar(10)
            ,idade varchar(3)
            ,primary key (id)
        );

        create table producao(
            id varchar(10)
            ,id_set varchar(10)
            ,id_executivo varchar(10)
            ,id_elenco varchar(10)
            ,id_objetos varchar(10)
            ,primary key (id)
            ,foreign key (id_set) references produtor(id)
            ,foreign key (id_executivo) references produtor(id)
            ,foreign key (id_elenco) references produtor(id)
            ,foreign key (id_objetos) references produtor(id)
        );

        create table filme(
            id varchar(10)
            ,genero varchar(30)
            ,nome varchar(30)
            ,ano_lancamento varchar(4)
            ,id_elenco varchar(10)
            ,id_producao varchar(10)
            ,id_diretor varchar(10)
            ,id_roteirista varchar(10)
            --,id_sequencia varchar(10)
            ,primary key (id)
            --,foreign key (id_elenco) references elenco(id)
            ,foreign key (id_producao) references produtor(id)
            ,foreign key (id_diretor) references diretor(id)
            ,foreign key (id_roteirista) references roteirista(id)
        );

        create table elenco(
            id varchar(10)
            ,id_filme varchar(10)
            ,id_ator varchar(10)
            ,primary key (id)
            ,foreign key (id_filme) references filme(id)
            ,foreign key (id_ator) references ator(id)
        );

        create table gravacao(
            data varchar(10)
            ,local varchar(10)
            ,horario varchar(10)
            ,id_filme varchar(10)
            ,foreign key (id_filme) references filme(id)
        );

        ALTER TABLE filme ADD CONSTRAINT id FOREIGN KEY (id_elenco) REFERENCES elenco(id);
    """)
     cursor.execute("commit")

#Funções para gerar os dados

# Connect to the database
try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
    ) #dados para conseguir conectar com o banco de dados (usar arquivo .env)
    print("Connection successful!")
    # Create a cursor to execute SQL queries
    cursor = connection.cursor()
    # Example query
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    print("Current Time:", result)
    
    #main
    resetarDB()
    criarDB()


    cursor.close() #sem cursor
    connection.close() #fim da conexão com o banco de dados 
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")