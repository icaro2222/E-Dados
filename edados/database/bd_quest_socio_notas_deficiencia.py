from ast import If
import pandas as pd
from edados.database import conect_db

# Mysql
# BANCO = 'enem2 '

# Postgres
BANCO = '"enem" '
LIMIT = ' LIMIT 1000'

def buscar_dataframe_no_banco(amostra, filtro_sexo = "vazio", filtro_deficiencia = "vazio"):
    engine = conect_db.connect()


    retorno_da_query = '"' + '","'.join(amostra) + '"'

    if(filtro_sexo != "vazio"):
        if(filtro_deficiencia != "vazio"):
            query = 'SELECT ' + retorno_da_query + ',"'+ str(filtro_deficiencia)+ '" FROM  ' + BANCO + '  WHERE "TP_SEXO" ="' + str(filtro_sexo) + '" AND "' + str(filtro_deficiencia) + '" = "1" '
        else:
            query = 'SELECT ' + retorno_da_query + ' FROM ' + BANCO + ' WHERE "TP_SEXO" ="' + str(filtro_sexo) + '" '
    else:
        if(filtro_deficiencia != "vazio"):
            query = 'SELECT ' + retorno_da_query + ',"'+ str(filtro_deficiencia)+ '" FROM ' + BANCO + ' WHERE "' + str(filtro_deficiencia) + '" = 1'
        else:
            query = 'SELECT "' + '","'.join(amostra) + '" FROM ' + BANCO
    
    query = query + LIMIT

    print(query)
    # print(pd.read_sql( ('SELECT count(Q001) FROM ' + BANCO), engine))
    df = pd.read_sql(query, engine)
    df = pd.DataFrame(df)
    
    return df












