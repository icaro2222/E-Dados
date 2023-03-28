from ast import If
import pandas as pd
from edados.database import conect_db

BANCO = conect_db.banco()
LIMIT = ' '

def buscar_dataframe_no_banco(amostra, filtro_sexo = "vazio", filtro_deficiencia = "vazio", filtro_ano = "vazio"):
    engine = conect_db.connect()

    if(filtro_ano == '2018'):
        BANCO = '"enem_2018"'
    else:
        BANCO = conect_db.banco()
    
    retorno_da_query = '"' + '","'.join(amostra) + '"'
    estrutura = 'SELECT ' + retorno_da_query + ' FROM ' + BANCO

    if(filtro_deficiencia == 'todas'):
        filtro_deficiencia = def_filtro_deficiencia('1')
    elif(filtro_deficiencia == 'nenhuma'):
        filtro_deficiencia = def_filtro_deficiencia('0')
    else:
        filtro_deficiencia =  ' WHERE "' + str(filtro_deficiencia) + '" = 1 '

    if(filtro_sexo != 'vazio'):
        filtro_sexo = ' AND "TP_SEXO" = '+"'"+str(filtro_sexo)+"' "
    else:
        filtro_sexo = ''


    # filtrando o ano
    filtro_ano = ' AND "NU_ANO" = ' + str(filtro_ano)
    

    query = estrutura + filtro_deficiencia + filtro_sexo + filtro_ano + LIMIT

    print(query)
    # print(pd.read_sql( ('SELECT count(Q001) FROM ' + BANCO), engine))
    
    df = pd.read_sql(query, engine)
    df = pd.DataFrame(df)
    pd.set_option('display.max_colwidth',4)
    
    return df



def buscar_dataframe_no_banco(amostra, 
                                    filtro_questao = "vazio", 
                                    filtro_sexo = "vazio", 
                                    filtro_deficiencia = "vazio", 
                                    filtro_ano = "vazio", 
                                    filtro_cor = "vazio", 
                                    filtro_estado_civil = "vazio", 
                                    filtro_escola = "vazio", 
                                    filtro_nacionalidade = "vazio"):
    engine = conect_db.connect()

    if(filtro_cor == 'todos'):
        filtro_cor = ''
    else:
        filtro_cor =  ' AND "TP_COR_RACA" =' +"'" +filtro_cor+"'"

    if(filtro_escola == 'todos'):
        filtro_escola = ''
    else:
        filtro_escola =  ' AND "TP_ESCOLA" =' +"'" +filtro_escola+"'"

    if(filtro_nacionalidade == 'todos'):
        filtro_nacionalidade = ''
    else:
        filtro_nacionalidade =  ' AND "TP_NACIONALIDADE" =' +"'" +filtro_nacionalidade+"'"

    if(filtro_sexo == 'todos'):
        filtro_sexo = ''
    else:
        filtro_sexo =  ' AND "TP_SEXO" =' +"'" +filtro_sexo+"'"

    if(filtro_estado_civil == 'todos'):
        filtro_estado_civil = ''
    else:
        filtro_estado_civil =  ' AND "TP_ESTADO_CIVIL" =' +"'" + filtro_estado_civil +"'"

    if(filtro_questao == 'todos'):
        filtro_questao = (' "Q001", "Q002","Q003","Q004","Q005","Q006","Q007","Q008","Q009",'
        '"Q010","Q011","Q012","Q013",'
                '"Q014","Q015","Q016","Q017",'
                '"Q018","Q019","Q020","Q021",'
                '"Q022","Q023","Q024","Q025", ')
    
    elif(filtro_questao == 'nenhum'):
        filtro_questao = ''
    else:
        filtro_questao = ' "' + filtro_questao + '", '


    if(filtro_ano == '2018'):
        BANCO = '"enem_2018"'
    else:
        BANCO = conect_db.banco()
    
    retorno_da_query = filtro_questao
    estrutura = 'SELECT '+ retorno_da_query + ' "TP_SEXO", "TP_COR_RACA", "NU_IDADE", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT" FROM ' + BANCO

    if(filtro_deficiencia == 'todas'):
        filtro_deficiencia = def_filtro_deficiencia('1')
    elif(filtro_deficiencia == 'nenhuma'):
        filtro_deficiencia = def_filtro_deficiencia('0')
    else:
        filtro_deficiencia =  ' WHERE "' + str(filtro_deficiencia) + '" = 1 '

    # filtrando o ano
    filtro_ano = ' AND "NU_ANO" = ' + str(filtro_ano)
    

    query = (estrutura + filtro_deficiencia + 
                filtro_sexo +
                filtro_cor  + 
                filtro_estado_civil +  
                filtro_ano  + 
                filtro_escola  + 
                filtro_nacionalidade  + 
                LIMIT)

    print(query)
    # print(pd.read_sql( ('SELECT count(Q001) FROM ' + BANCO), engine))
    df = pd.read_sql(query, engine)
    df = pd.DataFrame(df)
    
    return df


def def_filtro_deficiencia(filtro):

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









