from sqlalchemy import create_engine



def banco():
    # Mysql
    # BANCO = 'enem2 '

    # Postgres
    BANCO = '"enem_2019" '

    return BANCO

def connect():

    # Conexão MYSQL
    # tipo_db = "mysql+pymysql"
    # host="localhost"
    # user="icaro"
    # passwod="tatakae"
    # database="e_dados"
    # porta=3306


    # Conexão POSTGRESQL do Heroku
    # tipo_db = "postgresql"
    # host="ec2-54-87-179-4.compute-1.amazonaws.com"
    # user="ccgapwggqseseb"
    # passwod="bf9adeb9b12252a5a9377ede93702f53f404d6f23a9db8aeb77f3d2704a820f4"
    # database="da0rf6a9o8h8v3"
    # porta= 5432


    # Conexão POSTGRESQL
    tipo_db = "postgresql"
    host="localhost"
    user="postgres"
    passwod="tatakae22"
    database="e-dados"
    porta= 5432

    conexao = str(tipo_db)+"://"+str(user)+":"+str(passwod)+"@"+str(host)+":" + str(porta)+"/"+str(database)
    
    # Conectando com o Banco de Dados
    engine = create_engine(conexao, pool_pre_ping=True)

    print("Conexão com o banco bem sucedida!")
    
    return engine
