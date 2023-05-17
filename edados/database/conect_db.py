from sqlalchemy import create_engine

LIMIT = ""

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

def filtro_de_ficiencia(filtro_valor):
    
    
    if(filtro_valor=='todas'):
        variavel_filtro_deficiencia = (""" WHERE "TP_PRESENCA_CN"='1'
                AND "TP_PRESENCA_CN"='1'
                AND "TP_PRESENCA_CH"='1'
                AND "TP_PRESENCA_LC"='1'
                AND "TP_PRESENCA_MT"='1'  
                AND ("IN_BAIXA_VISAO" = '1'  
                OR "IN_CEGUEIRA" ='1'  
                OR "IN_SURDEZ" ='1'  
                OR "IN_DEFICIENCIA_AUDITIVA" ='1'  
                OR "IN_SURDO_CEGUEIRA" ='1'  
                OR "IN_DEFICIENCIA_FISICA" ='1'  
                OR "IN_DEFICIENCIA_MENTAL" ='1'  
                OR "IN_DEFICIT_ATENCAO" ='1'  
                OR "IN_DISLEXIA" ='1'  
                OR "IN_DISCALCULIA" ='1'  
                OR "IN_AUTISMO" ='1'  
                OR "IN_VISAO_MONOCULAR" ='1'  
                OR "IN_OUTRA_DEF" ='1' )""")
    elif(filtro_valor=='nenhuma' or filtro_valor=='vazio'):
        variavel_filtro_deficiencia = (""" WHERE "TP_PRESENCA_CN"='1'
                AND "TP_PRESENCA_CN"='1'
                AND "TP_PRESENCA_CH"='1'
                AND "TP_PRESENCA_LC"='1'
                AND "TP_PRESENCA_MT"='1'  
                AND ("IN_BAIXA_VISAO" ='0'
                AND "IN_CEGUEIRA" ='0'
                AND "IN_SURDEZ" ='0'
                AND "IN_DEFICIENCIA_AUDITIVA" ='0'
                AND "IN_SURDO_CEGUEIRA" ='0'
                AND "IN_DEFICIENCIA_FISICA" ='0'
                AND "IN_DEFICIENCIA_MENTAL" ='0'
                AND "IN_DEFICIT_ATENCAO" ='0'
                AND "IN_DISLEXIA" ='0'
                AND "IN_DISCALCULIA" ='0'
                AND "IN_AUTISMO" ='0'
                AND "IN_VISAO_MONOCULAR" ='0'
                AND "IN_OUTRA_DEF" ='0')""")
    elif(filtro_valor=='todos'):
        variavel_filtro_deficiencia =  """WHERE "TP_PRESENCA_CN"='1'
                AND "TP_PRESENCA_CN"='1'
                AND "TP_PRESENCA_CH"='1'
                AND "TP_PRESENCA_LC"='1'
                AND "TP_PRESENCA_MT"='1'  """
    else:
        variavel_filtro_deficiencia =  ' WHERE "' + str(filtro_valor) + '" = 1 '

    return variavel_filtro_deficiencia


