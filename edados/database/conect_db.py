from sqlalchemy import create_engine

def connect():

    # Conexão MYSQL
    tipo_db = "mysql+pymysql"
    host="localhost"
    user="icaro"
    passwod="tatakae"
    database="e_dados"
    porta=3306


    # Conexão POSTGRESQL
    # tipo_db = "postgresql"
    # host="ec2-54-82-205-3.compute-1.amazonaws.com"
    # user="sbipzhlapwnedk"
    # passwod="d33c73442cc2ecc9a925c62e492092ef592dc228ad55db5d2ee01ba3258b07ac"
    # database="d50ueqsv9ebsrf"
    # porta= 5432

    conexao = str(tipo_db)+"://"+str(user)+":"+str(passwod)+"@"+str(host)+":" + str(porta)+"/"+str(database)
    
    # Conectando com o Banco de Dados
    engine = create_engine(conexao, pool_pre_ping=True)

    print("Conexãop com o banco bem sucedida!")
    
    return engine
