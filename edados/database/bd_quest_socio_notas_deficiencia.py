from ast import If
import pandas as pd
from edados.database import conect_db


def buscar_dataframe_no_banco(amostra,                            
                              filtro_questao = "vazio", 
                            filtro_recurso = "vazio", 
                            filtro_localizacao_da_escola = "vazio", 
                            filtro_amostra = "vazio", 
                            filtro_estado = "vazio", 
                            filtro_sexo = "vazio", 
                            filtro_deficiencia = "vazio", 
                            filtro_ano = "vazio", 
                            filtro_cor = "vazio", 
                            filtro_estado_civil = "vazio", 
                            filtro_escola = "vazio", 
                            filtro_nacionalidade = "vazio"
                            ):
    
    engine = conect_db.connect()
    conect_db.LIMIT = filtro_amostra
    
    BANCO = conect_db.banco(filtro_ano=filtro_ano)

    RESTRICAO = ' AND "' + amostra[0] + '" > 0 '

    # filtrando o ano
    
    # filtros
    if(filtro_cor == 'todos'):
        filtro_cor = ''
    else:
        filtro_cor =  ' AND "TP_COR_RACA" =' +"'" +filtro_cor+"'"
        
    if(filtro_recurso == 'todos'):
        filtro_recurso = ''
    elif(filtro_recurso == 'nenhum'):
        filtro_recurso = """ AND
            ("IN_BRAILLE" = 1 OR
            "IN_AMPLIADA_24" = 1 OR
            "IN_AMPLIADA_18" = 1 OR
            "IN_LEDOR" = 1 OR
            "IN_ACESSO" = 1 OR
            "IN_TRANSCRICAO"= 1 OR
            "IN_LIBRAS" = 1 OR
            "IN_TEMPO_ADICIONAL" = 1)
            """
    else:
        filtro_recurso =  ' AND "'+ filtro_recurso +'" =1'
        
    if(filtro_localizacao_da_escola == 'todos'):
        filtro_localizacao_da_escola = ''
    else:
        filtro_localizacao_da_escola =  ' AND "TP_LOCALIZACAO_ESC" =' +"'" +filtro_localizacao_da_escola+"'"

    if(filtro_estado == 'todos'):
        filtro_estado = ''
    else:
        filtro_estado =  ' AND "SG_UF_RESIDENCIA" =' +"'" +filtro_estado+"'"

    if(filtro_escola == 'todos'):
        filtro_escola = ''
    else:
        filtro_escola =  ' AND "TP_ESCOLA" =' +"'" +filtro_escola+"'"

    if(filtro_nacionalidade == 'todos'):
        filtro_nacionalidade = ''
    else:
        filtro_nacionalidade =  ' AND "TP_NACIONALIDADE" =' +"'" +filtro_nacionalidade+"'"

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
    
    query = (query + 
                RESTRICAO +
                filtro_cor  + 
                filtro_estado_civil +  
                filtro_escola  + 
                filtro_nacionalidade  + 
                filtro_estado  + 
                filtro_recurso  + 
                filtro_localizacao_da_escola  + 
                conect_db.LIMIT)
    print(query)
    # print(pd.read_sql( ('SELECT count(Q001) FROM ' + BANCO), engine))
    df = pd.read_sql(query, engine)
    df = pd.DataFrame(df)
    
    return df












