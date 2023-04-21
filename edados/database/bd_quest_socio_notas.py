from ast import If
import pandas as pd
from edados.database import conect_db


def buscar_dataframe_no_banco(amostra, filtro_sexo = "vazio", filtro_deficiencia = "todos", filtro_ano = "vazio"):
    engine = conect_db.connect()

    BANCO = conect_db.banco(filtro_ano=filtro_ano)

    # Mysql
    retorno = '","'.join(amostra)

    # Postgresql
    # retorno = '"'+'","'.join(amostra)+'"'

    # filtrando o ano
    if(filtro_ano != "todos"):
        filtro_ano = ' AND "NU_ANO" = ' + str(filtro_ano)
    else:
        filtro_ano = ''

    if(filtro_sexo != "vazio"):
        if(filtro_deficiencia != "vazio"):
            query = 'SELECT "' + retorno +'","'+ str(filtro_deficiencia)+ '" FROM  ' + BANCO + '  WHERE TP_SEXO ="' + str(filtro_sexo) + '" AND ' + str(filtro_deficiencia) + ' = "1" '
        else:
            query = 'SELECT "' + retorno + '" FROM  ' + BANCO + '  WHERE TP_SEXO ="' + str(filtro_sexo) + '" '
    else:
        if(filtro_deficiencia != "vazio"):
            query = 'SELECT "' + retorno +'","'+ str(filtro_deficiencia)+ '" FROM ' + BANCO + ' WHERE ' + str(filtro_deficiencia) + ' = 1'
        else:
            query = 'SELECT "' + retorno + '" FROM ' + BANCO
    
    query = query + filtro_ano + conect_db.LIMIT

    print(query)
    # print(pd.read_sql( ('SELECT count(Q001) FROM ' + BANCO), engine))
    df = pd.read_sql(query, engine)
    df = pd.DataFrame(df)
    
    return df












