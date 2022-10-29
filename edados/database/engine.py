import pandas as pd
import mysql.connector
import sqlalchemy
from sqlalchemy import create_engine


def buscar_dataframe_no_banco():
    engine = create_engine("mysql+pymysql://icaro:tatakae@localhost/e_dados", pool_pre_ping=True)


    df = pd.read_sql('SELECT * FROM enem LIMIT 20000', engine)
    df = pd.DataFrame(df)
    
    return df












