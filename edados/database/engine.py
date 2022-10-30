from ast import If
import pandas as pd
import mysql.connector
import sqlalchemy
from sqlalchemy import create_engine

BANCO = 'enem2 '
LIMIT = ' LIMIT 10000'

def buscar_dataframe_no_banco(amostra, filtro_sexo = "vazio", filtro_deficiencia = "vazio"):
    engine = create_engine("mysql+pymysql://icaro:tatakae@localhost/e_dados", pool_pre_ping=True)

    if(filtro_sexo != "vazio"):
        if(filtro_deficiencia != "vazio"):
            query = 'SELECT ' + ",".join(amostra) + ','+ str(filtro_deficiencia)+ ' FROM  ' + BANCO + '  WHERE TP_SEXO ="' + str(filtro_sexo) + '" AND ' + str(filtro_deficiencia) + ' = "1" ' + LIMIT
        else:
            query = 'SELECT ' + ",".join(amostra) + ' FROM  ' + BANCO + '  WHERE TP_SEXO ="' + str(filtro_sexo) + '" ' + LIMIT
    else:
        if(filtro_deficiencia != "vazio"):
            query = 'SELECT ' + ",".join(amostra) + ','+ str(filtro_deficiencia)+ ' FROM ' + BANCO + ' WHERE ' + str(filtro_deficiencia) + ' = 1' + LIMIT
        else:
            query = 'SELECT ' + ",".join(amostra) + ' FROM ' + BANCO + LIMIT
    
    print(query)
    print(pd.read_sql( ('SELECT count(Q001) FROM ' + BANCO), engine))
    df = pd.read_sql(query, engine)
    df = pd.DataFrame(df)
    
    return df












