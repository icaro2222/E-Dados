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
        filtro_deficiencia = filtro_de_ficiencia('1')
    elif(filtro_deficiencia == 'nenhuma'):
        filtro_deficiencia = filtro_de_ficiencia('0')
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


def filtro_de_ficiencia(filtro):

    if(filtro=='1'):
        variavel_filtro_deficiencia = (' WHERE ("IN_BAIXA_VISAO" =' + filtro +
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
            ' OR "IN_OUTRA_DEF" =' + filtro + ')')
    else:
        variavel_filtro_deficiencia = (' WHERE ("IN_BAIXA_VISAO" =' + filtro +
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
            ' AND "IN_OUTRA_DEF" =' + filtro + ')')

    return variavel_filtro_deficiencia









