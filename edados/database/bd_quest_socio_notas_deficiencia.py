from ast import If
import pandas as pd
from edados.database import conect_db

LIMIT = ' LIMIT 10000'

def buscar_dataframe_no_banco(amostra, filtro_sexo = "vazio", filtro_deficiencia = "vazio", filtro_ano = "vazio"):
    engine = conect_db.connect()
    
    if(filtro_ano == '2018'):
        BANCO = '"enem_2018"'
    else:
        BANCO = conect_db.banco()

    RESTRICAO = ' AND "' + amostra[0] + '" > 0 '

    # filtrando o ano
    if(filtro_ano != "todos"):
        ano = ' WHERE "NU_ANO" = ' + str(filtro_ano)
        filtro_ano = ' AND "NU_ANO" = ' + str(filtro_ano)
    else:
        ano = ' WHERE "' + amostra[0] + '" > 0 '
        filtro_ano = ''
        pass

    retorno_da_query = '"' + '","'.join(amostra) + '"'

    if(filtro_sexo != "vazio"):
        if(filtro_deficiencia != "vazio"):
            query = 'SELECT ' + retorno_da_query + ' FROM ' + BANCO + '  WHERE  "' + str(filtro_deficiencia) + '" = 1 AND "TP_SEXO" = '+"'"+str(filtro_sexo)+"'" + filtro_ano
        else:
            query = 'SELECT ' + retorno_da_query + ' FROM ' + BANCO + ' WHERE "TP_SEXO" = '+"'"+str(filtro_sexo)+"'" + filtro_ano
    else:
        if(filtro_deficiencia != "vazio"):
            query = 'SELECT ' + retorno_da_query + ' FROM ' + BANCO + ' WHERE "' + str(filtro_deficiencia) + '" = 1' + filtro_ano
        else:
            query = 'SELECT "' + '","'.join(amostra) + '" FROM ' +  BANCO + ano
    
    query = query + RESTRICAO + LIMIT

    print(query)
    # print(pd.read_sql( ('SELECT count(Q001) FROM ' + BANCO), engine))
    df = pd.read_sql(query, engine)
    df = pd.DataFrame(df)
    
    return df












