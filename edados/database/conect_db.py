from sqlalchemy import create_engine

def connect():

    # Conexão MYSQL
    # tipo_db = "mysql+pymysql"
    # host="localhost"
    # user="icaro"
    # passwod="tatakae"
    # database="e_dados"
    # porta=3306


    # Conexão POSTGRESQL
    tipo_db = "postgresql"
    host="ec2-44-195-132-31.compute-1.amazonaws.com"
    user="glbksewieqangq"
    passwod="9d27ed821da4e10718d0b602c631c3a3a3f546ad4f130843abdd1f96a7f7d45d"
    database="da05j5cn1d843o"
    porta= 5432

    conexao = str(tipo_db)+"://"+str(user)+":"+str(passwod)+"@"+str(host)+":" + str(porta)+"/"+str(database)
    
    # Conectando com o Banco de Dados
    engine = create_engine(conexao, pool_pre_ping=True)

    print("Conexãop com o banco bem sucedida!")
    
    return engine
