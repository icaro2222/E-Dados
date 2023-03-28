from ast import If
import pandas as pd
from edados.database import conect_db

BANCO = conect_db.banco()
LIMIT = ' LIMIT 100'

def buscar_dataframe_no_banco(ano = "todos"):
    engine = conect_db.connect()

    if(ano != "todos"):
        query = 'SELECT count(Q001) FROM ' + BANCO
    else:
        query = 'SELECT count(Q001) FROM ' + BANCO
    
    query = query + LIMIT

    print(query)
    # print(pd.read_sql( ('SELECT count(Q001) FROM ' + BANCO), engine))
    df = pd.read_sql(query, engine)
    df = pd.DataFrame(df)
    
    return df












