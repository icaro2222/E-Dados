from ast import If
import pandas as pd
from edados.database import conect_db

def buscar_dataframe_no_banco(amostra, filtro_cor_da_prova, filtro_sexo = "vazio", filtro_deficiencia = "vazio", filtro_ano = "vazio"):
    engine = conect_db.connect()

    print(filtro_ano)

    BANCO = conect_db.banco(filtro_ano=filtro_ano)
    
    print(BANCO)
    
    retorno_da_query = '"' + '","'.join(amostra) + '"'
    estrutura = 'SELECT ' + retorno_da_query + ' FROM ' + BANCO

    filtro_cor_da_prova = ' AND "' + amostra[0]+'"='+"'"+filtro_cor_da_prova+"'"

    if(filtro_deficiencia == 'todas'):
        filtro_deficiencia = conect_db.filtro_de_ficiencia('1')
    elif(filtro_deficiencia == 'nenhuma'):
        filtro_deficiencia = conect_db.filtro_de_ficiencia('0')
    else:
        filtro_deficiencia =  ' WHERE "' + filtro_deficiencia + '" = 1 '

    if(filtro_sexo != 'vazio'):
        filtro_sexo = ' AND "TP_SEXO" = '+"'"+ filtro_sexo +"' "
    else:
        filtro_sexo = ''

    # filtrando o ano
    filtro_ano = ' AND "NU_ANO" = ' + str(filtro_ano)
    
    
    query = estrutura + filtro_deficiencia + filtro_sexo + filtro_ano + filtro_cor_da_prova + conect_db.LIMIT

    print(query)
    # print(pd.read_sql( ('SELECT count(Q001) FROM ' + BANCO), engine))
    df = pd.read_sql(query, engine)
    df = pd.DataFrame(df)
    
    return df