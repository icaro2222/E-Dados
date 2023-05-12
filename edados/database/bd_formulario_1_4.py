import pandas as pd
from edados.database import conect_db
from edados.database import bd_filtro

def buscar_dataframe_no_banco(amostra, 
                                    filtro_questao = "vazio", 
                                    filtro_recurso = "vazio", 
                                    filtro_localizacao_da_escola = "vazio", 
                                    filtro_amostra = "vazio", 
                                    filtro_ltp_adm_escola="vazio",              
                                    filtro_ano_de_conclusao="vazio",             
                                    filtro_estado = "vazio", 
                                    filtro_sexo = "vazio", 
                                    filtro_deficiencia = "vazio", 
                                    filtro_ano = "vazio", 
                                    filtro_cor = "vazio", 
                                    filtro_estado_civil = "vazio", 
                                    filtro_escola = "vazio", 
                                    filtro_nacionalidade = "vazio"):
    engine = conect_db.connect()

    filtro = bd_filtro.filtro(
            filtro_ltp_adm_escola=filtro_ltp_adm_escola,            
            filtro_ano_de_conclusao=filtro_ano_de_conclusao, 
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
            filtro_nacionalidade=filtro_nacionalidade)
    
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


    BANCO = conect_db.banco(filtro_ano=filtro_ano)
    
    retorno_da_query = filtro_questao
    estrutura = 'SELECT '+ retorno_da_query + ' "TP_SEXO", "TP_COR_RACA", "NU_IDADE", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT" FROM ' + BANCO

    query = (estrutura + filtro)

    print(query)
    df = pd.read_sql(query, engine)
    df = pd.DataFrame(df)
    
    return df