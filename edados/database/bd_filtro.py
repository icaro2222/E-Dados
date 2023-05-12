from ast import If
import pandas as pd
from edados.database import conect_db

def filtro(                       
            filtro_ltp_adm_escola="vazio",              
            filtro_ano_de_conclusao="vazio",   
            filtro_questao = "nenhum", 
            filtro_recurso = "vazio", 
            filtro_localizacao_da_escola = "vazio", 
            filtro_amostra = "vazio", 
            filtro_estado = "vazio", 
            filtro_sexo = "vazio", 
            filtro_deficiencia = "vazio", 
            filtro_cor = "vazio", 
            filtro_estado_civil = "vazio", 
            filtro_escola = "vazio", 
            filtro_nacionalidade = "vazio", 
            restricao = "", 
            filtro_cor_da_prova = ""
            ):
    
    if(filtro_ano_de_conclusao=="vazio"):   
        filtro_ano_de_conclusao = ''
    else:
        filtro_ano_de_conclusao = ' AND "TP_ANO_CONCLUIU" = ' +"'" + filtro_ano_de_conclusao+"'"
    
    if(filtro_ltp_adm_escola=="vazio"):   
        filtro_ltp_adm_escola = ''
    else:
        filtro_ltp_adm_escola = ' AND "TP_DEPENDENCIA_ADM_ESC" = ' +"'" + filtro_ltp_adm_escola+"'"
    
    if(filtro_amostra!="todos_os_dados"):   
        conect_db.LIMIT = filtro_amostra
    else:
        conect_db.LIMIT = ""
    
    filtro_deficiencia = conect_db.filtro_de_ficiencia(filtro_deficiencia)
    
    if(filtro_cor == 'todos'):
        filtro_cor = ''
    else:
        filtro_cor =  ' AND "TP_COR_RACA" =' +"'" +filtro_cor+"'"
        
    if(filtro_recurso == 'nenhum'):
        filtro_recurso = """ AND
            ("IN_BRAILLE" = 0 OR
            "IN_AMPLIADA_24" = 0 OR
            "IN_AMPLIADA_18" = 0 OR
            "IN_LEDOR" = 0 OR
            "IN_ACESSO" = 0 OR
            "IN_TRANSCRICAO"= 0 OR
            "IN_LIBRAS" = 0 OR
            "IN_TEMPO_ADICIONAL" = 0)
            """
    elif(filtro_recurso == 'todos'):
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

  


    if(filtro_sexo != 'vazio' and filtro_sexo != 'todos'):
        filtro_sexo = ' AND "TP_SEXO" = '+"'"+str(filtro_sexo)+"' "
    else:
        filtro_sexo = ''

    filtro = (  filtro_deficiencia + 
                filtro_sexo +
                filtro_cor  + 
                filtro_estado_civil +  
                filtro_escola  + 
                filtro_nacionalidade  + 
                filtro_estado  + 
                filtro_recurso  + 
                filtro_localizacao_da_escola  + 
                filtro_cor_da_prova +
                restricao +
                filtro_ano_de_conclusao +
                filtro_ltp_adm_escola +
                conect_db.LIMIT)
    
    print('*************************************************************************')    
    print(filtro)    
    print('*************************************************************************')
    return filtro