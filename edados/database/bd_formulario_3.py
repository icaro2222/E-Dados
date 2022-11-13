from ast import If
import pandas as pd
from edados.database import conect_db

BANCO = conect_db.banco()
LIMIT = ' '

def buscar_dataframe_no_banco(amostra, filtro_cor_da_prova, filtro_sexo = "vazio", filtro_deficiencia = "vazio", filtro_ano = "vazio"):
    engine = conect_db.connect()

    filtro_cor_da_prova = ' AND "' + amostra[0]+'"='+"'"+filtro_cor_da_prova+"'"

    if(filtro_deficiencia == 'todas'):
        filtro_deficiencias = filtro_de_ficiencia('1')
    elif(filtro_deficiencia == 'nenhuma'):
        filtro_deficiencias = filtro_de_ficiencia('0')
    else:
        filtro_deficiencias = ''
        filtro_deficiencias = ''

    # filtrando o ano and 
    if(filtro_ano != "todos"):
        ano = ' WHERE "NU_ANO" = ' + str(filtro_ano)
        filtro_ano = ' AND "NU_ANO" = ' + str(filtro_ano)
    else:
        ano = ''
        filtro_ano = ''

    retorno_da_query = '"' + '","'.join(amostra) + '"'

    if(filtro_sexo != "vazio"):
        if(filtro_deficiencia != "todas" and filtro_deficiencia!= "nenhuma"):
            query = 'SELECT ' + retorno_da_query + ' FROM ' + BANCO + '  WHERE  "' + str(filtro_deficiencia) + '" = 1 AND "TP_SEXO" = '+"'"+str(filtro_sexo)+"'" + filtro_ano
        else:
            query = 'SELECT ' + retorno_da_query + ' FROM ' + BANCO + ' WHERE "TP_SEXO" = '+"'"+str(filtro_sexo)+"'" + filtro_ano
    else:
        if(filtro_deficiencia != "todas" and filtro_deficiencia!= "nenhuma"):
            query = 'SELECT ' + retorno_da_query + ' FROM ' + BANCO + ' WHERE "' + str(filtro_deficiencia) + '" = 1' + filtro_ano
        else:
            query = 'SELECT "' + '","'.join(amostra) + '" FROM ' +  BANCO + ano
    
    query = query + filtro_deficiencias + filtro_cor_da_prova + LIMIT

    print(query)
    # print(pd.read_sql( ('SELECT count(Q001) FROM ' + BANCO), engine))
    df = pd.read_sql(query, engine)
    df = pd.DataFrame(df)
    
    return df


def filtro_de_ficiencia(filtro):

    if(filtro=='1'):
        variavel_filtro_deficiencia = (' WHERE "IN_BAIXA_VISAO" =' + filtro +
            ' OR "IN_CEGUEIRA" =' + filtro +
            ' OR "IN_SURDEZ" =' + filtro +
            ' OR "IN_DEFICIENCIA_AUDITIVA" =' + filtro +
            ' OR "IN_SURDO_CEGUEIRA" =' + filtro +
            ' OR "IN_DEFICIENCIA_FISICA" =' + filtro +
            ' OR "IN_DEFICIENCIA_MENTAL" =' + filtro +
            ' OR "IN_DEFICIT_ATENCAO" =' + filtro +
            ' OR "IN_DISLEXIA" =' + filtro +
            ' OR "IN_DISCALCULIA" =' + filtro +
            ' OR "IN_AUTISMO" =' + filtro +
            ' OR "IN_VISAO_MONOCULAR" =' + filtro +
            ' OR "IN_OUTRA_DEF" =' + filtro)
    else:
        variavel_filtro_deficiencia = (' WHERE "IN_BAIXA_VISAO" =' + filtro +
            ' AND "IN_CEGUEIRA" =' + filtro +
            ' AND "IN_SURDEZ" =' + filtro +
            ' AND "IN_DEFICIENCIA_AUDITIVA" =' + filtro +
            ' AND "IN_SURDO_CEGUEIRA" =' + filtro +
            ' AND "IN_DEFICIENCIA_FISICA" =' + filtro +
            ' AND "IN_DEFICIENCIA_MENTAL" =' + filtro +
            ' AND "IN_DEFICIT_ATENCAO" =' + filtro +
            ' AND "IN_DISLEXIA" =' + filtro +
            ' AND "IN_DISCALCULIA" =' + filtro +
            ' AND "IN_AUTISMO" =' + filtro +
            ' AND "IN_VISAO_MONOCULAR" =' + filtro +
            ' AND "IN_OUTRA_DEF" =' + filtro)

    return variavel_filtro_deficiencia









