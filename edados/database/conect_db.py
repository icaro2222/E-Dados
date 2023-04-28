from sqlalchemy import create_engine

LIMIT = "LIMIT 1000"

def banco(filtro_ano):

    if(filtro_ano == '2016'):
        BANCO = '"enem_2016"'
    elif(filtro_ano == '2017'):
        BANCO = '"enem_2017"'
    elif(filtro_ano == '2018'):
        BANCO = '"enem_2018"'
    else:
        BANCO = '"enem_2019_1"'

    return BANCO

def connect():


    conexao = str(tipo_db)+"://"+str(user)+":"+str(passwod)+"@"+str(host)+":" + str(porta)+"/"+str(database)
    
    # Conectando com o Banco de Dados
    engine = create_engine(conexao, pool_pre_ping=True)

    print("Conexão com o banco bem sucedida!")
    
    return engine
