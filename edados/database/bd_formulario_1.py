from ast import If
import pandas as pd
from edados.database import conect_db

def buscar_dataframe_no_banco(amostra, filtro_sexo = "vazio", 
                                    filtro_amostra = "vazio",  filtro_deficiencia = "vazio", filtro_ano = "vazio"):
    engine = conect_db.connect()

    BANCO = conect_db.banco(filtro_ano=filtro_ano)
    # conect_db.LIMIT = filtro_amostra
    
    
    retorno_da_query = '"' + '","'.join(amostra) + '"'
    estrutura = 'SELECT ' + retorno_da_query + ' FROM ' + BANCO

    if(filtro_deficiencia == 'todas'):
        filtro_deficiencia = conect_db.filtro_de_ficiencia('1')
    elif(filtro_deficiencia == 'nenhuma'):
        filtro_deficiencia = conect_db.filtro_de_ficiencia('0')
    else:
        filtro_deficiencia =  ' WHERE "' + str(filtro_deficiencia) + '" = 1 '

    if(filtro_sexo != 'vazio'):
        filtro_sexo = ' AND "TP_SEXO" = '+"'"+str(filtro_sexo)+"' "
    else:
        filtro_sexo = ''


    # filtrando o ano
    filtro_ano = ' AND "NU_ANO" = ' + str(filtro_ano)
    

    query = estrutura + filtro_deficiencia + filtro_sexo + filtro_ano + conect_db.LIMIT

    print(query)
    # print(pd.read_sql( ('SELECT count(Q001) FROM ' + BANCO), engine))
    df = pd.read_sql(query, engine)
    df = pd.DataFrame(df)
    
    return df



def buscar_dataframe_no_banco_1_2(amostra, filtro_sexo = "vazio",
                                    filtro_amostra = "vazio",  filtro_deficiencia = "vazio", filtro_ano = "vazio"):
    engine = conect_db.connect()

    BANCO = conect_db.banco(filtro_ano=filtro_ano)
    conect_db.LIMIT = filtro_amostra
    
    
    retorno_da_query = '"' + '","'.join(amostra) + '"'
    estrutura = 'SELECT ' + retorno_da_query + ' ,"NU_IDADE" , "NO_MUNICIPIO_PROVA" ,"SG_UF_PROVA" , "TP_LINGUA" FROM ' + BANCO

    if(filtro_deficiencia == 'todas'):
        filtro_deficiencia = conect_db.filtro_de_ficiencia('1')
    elif(filtro_deficiencia == 'nenhuma'):
        filtro_deficiencia = conect_db.filtro_de_ficiencia('0')
    else:
        filtro_deficiencia =  ' WHERE "' + str(filtro_deficiencia) + '" = 1 '

    if(filtro_sexo != 'vazio'):
        filtro_sexo = ' AND "TP_SEXO" = '+"'"+str(filtro_sexo)+"' "
    else:
        filtro_sexo = ''


    # filtrando o ano
    filtro_ano = ' AND "NU_ANO" = ' + str(filtro_ano)
    

    query = estrutura + filtro_deficiencia + filtro_sexo + filtro_ano + conect_db.LIMIT

    print(query)
    # print(pd.read_sql( ('SELECT count(Q001) FROM ' + BANCO), engine))
    df = pd.read_sql(query, engine)
    df = pd.DataFrame(df)
    
    return df