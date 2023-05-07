import pandas as pd
from edados.database import conect_db
from edados.database import bd_filtro


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
    
    # filtros
    BANCO = conect_db.banco(filtro_ano=filtro_ano)
    
    RESTRICAO = ' AND "' + amostra[0] + '" > 0 '
    
    filtro = bd_filtro.filtro(
            filtro_questao=filtro_questao, 
            filtro_recurso=filtro_recurso, 
            filtro_localizacao_da_escola=filtro_localizacao_da_escola, 
            filtro_amostra=filtro_amostra, 
            filtro_estado=filtro_estado, 
            filtro_sexo=filtro_sexo, 
            filtro_deficiencia=filtro_deficiencia, 
            filtro_cor=filtro_cor, 
            filtro_estado_civil=filtro_estado_civil, 
            filtro_escola=filtro_escola, 
            filtro_nacionalidade=filtro_nacionalidade,
            restricao=RESTRICAO)
    
    
    # retorno_da_query = '"' + '","'.join(amostra) + '"'

    query = 'SELECT "' + '","'.join(amostra) + '" FROM ' +  BANCO
    
    query = (query + filtro)
    print(query)
    
    df = pd.read_sql(query, engine)
    df = pd.DataFrame(df)
    
    return df












