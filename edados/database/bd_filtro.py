from edados.database import conect_db

def filtro(                       
           filtro_cidade='vazio',  
           filtro_ano='vazio',
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
    
    filtro_deficiencia = conect_db.filtro_de_ficiencia(filtro_deficiencia)
    
    if(filtro_ano_de_conclusao=="vazio"):   
        filtro_ano_de_conclusao = ''
    else:
        filtro_ano_de_conclusao = ' AND "TP_ANO_CONCLUIU" = ' +"'" + filtro_ano_de_conclusao+"'"
    
    if(filtro_ltp_adm_escola=="vazio"):   
        filtro_ltp_adm_escola = ''
    else:
        filtro_ltp_adm_escola = ' AND "TP_DEPENDENCIA_ADM_ESC" = ' +"'" + filtro_ltp_adm_escola+"'"
    
    if(filtro_cor == 'todos'):
        filtro_cor = ''
    else:
        filtro_cor =  ' AND "TP_COR_RACA" =' +"'" +filtro_cor+"'"
        
    if(filtro_cidade == 'todos'):
        filtro_cidade = ''
    else:
        filtro_cidade =  ' AND "NO_MUNICIPIO_RESIDENCIA" =' +"'" +filtro_cidade+"'"
        
    if(filtro_recurso == 'vazio'):
        filtro_recurso = ""
    elif(filtro_recurso == 'todos'):
        filtro_recurso = """ AND
            ("IN_BRAILLE" = 1 OR
            "IN_AMPLIADA_24" = 1 OR
            "IN_AMPLIADA_18" = 1 OR
            "IN_LEDOR" = 1 OR
            "IN_ACESSO" = 1 OR
            "IN_TRANSCRICAO"= 1 OR
            "IN_LIBRAS" = 1 OR
            "IN_TEMPO_ADICIONAL" = 1 OR
            "IN_LEITURA_LABIAL" = 1 OR
            "IN_MESA_CADEIRA_RODAS" = 1)
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

    if(filtro_escola == 'todos' or filtro_escola == 'vazio' ):
        filtro_escola = ''
    else:
        filtro_escola =  ' AND "TP_ESCOLA" =' +"'" +filtro_escola+"'"

    if(filtro_nacionalidade == 'todos' or filtro_nacionalidade == 'vazio' ):
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
    elif(filtro_questao == 'nenhum' or filtro_questao == 'vazio'):
        filtro_questao = ''
    else:
        filtro_questao = ' "' + filtro_questao + '", '

    if(filtro_sexo != 'vazio' and filtro_sexo != 'todos'):
        filtro_sexo = ' AND "TP_SEXO" = '+"'"+str(filtro_sexo)+"' "
    else:
        filtro_sexo = ''
        
    amostragem = ''
    if(filtro_amostra!="todos_os_dados"):  
        conect_db.LIMIT = filtro_amostra    
        valor=0 
        if(conect_db.LIMIT == 'a_5_90'):
            if(filtro_ano=='2019'):
                valor = 273
            elif(filtro_ano=='2018'):
                valor = 273
            elif(filtro_ano=='2017'):
                valor = 273
        elif(conect_db.LIMIT == 'a_3_95'):
            if(filtro_ano=='2019'):
                valor = 1067
            elif(filtro_ano=='2018'):
                valor = 1067
            elif(filtro_ano=='2017'):
                valor = 1067
        elif(conect_db.LIMIT == 'a_1_99'):
            if(filtro_ano=='2019'):
                valor = 16567
            elif(filtro_ano=='2018'):
                valor = 16571
            elif(filtro_ano=='2017'):
                valor = 16579
        if(valor!=0):
            conect_db.LIMIT = (" LIMIT "+str(valor))
            amostragem = ' ORDER BY RANDOM() '
    else:
        conect_db.LIMIT = ""
    
    # if(conect_db.LIMIT == ' LIMIT 1000' or conect_db.LIMIT == ' LIMIT 0' or conect_db.LIMIT == ""):
    #     amostragem =''
    # else:
    #     pass

    filtro = (  filtro_deficiencia + 
                filtro_sexo +
                filtro_cidade +
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
                amostragem +
                conect_db.LIMIT)
    
    return filtro


def filtro_para_o_mapa(                       
           filtro_variavel_de_analise='vazio',          
           filtro_cidade='vazio',  
           filtro_ano='vazio',
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
    
    filtro_deficiencia = conect_db.filtro_de_ficiencia(filtro_deficiencia)
    
    if(filtro_variavel_de_analise=="vazio" or filtro_variavel_de_analise=="TP_COR_RACA" or filtro_variavel_de_analise=="TP_ESTADO_CIVIL"):   
        filtro_variavel_de_analise = ''
    else:
        filtro_variavel_de_analise = ' AND "'+ filtro_variavel_de_analise+'" > 0 '
    
    if(filtro_ano_de_conclusao=="vazio"):   
        filtro_ano_de_conclusao = ''
    else:
        filtro_ano_de_conclusao = ' AND "TP_ANO_CONCLUIU" = ' +"'" + filtro_ano_de_conclusao+"'"
    
    if(filtro_ltp_adm_escola=="vazio"):   
        filtro_ltp_adm_escola = ''
    else:
        filtro_ltp_adm_escola = ' AND "TP_DEPENDENCIA_ADM_ESC" = ' +"'" + filtro_ltp_adm_escola+"'"
    
    if(filtro_cor == 'todos'):
        filtro_cor = ''
    else:
        filtro_cor =  ' AND "TP_COR_RACA" =' +"'" +filtro_cor+"'"
        
    if(filtro_cidade == 'todos'):
        filtro_cidade = ''
    else:
        filtro_cidade =  ' AND "NO_MUNICIPIO_RESIDENCIA" =' +"'" +filtro_cidade+"'"
        
    if(filtro_recurso == 'vazio'):
        filtro_recurso = ""
    elif(filtro_recurso == 'todos'):
        filtro_recurso = """ AND
            ("IN_BRAILLE" = 1 OR
            "IN_AMPLIADA_24" = 1 OR
            "IN_AMPLIADA_18" = 1 OR
            "IN_LEDOR" = 1 OR
            "IN_ACESSO" = 1 OR
            "IN_TRANSCRICAO"= 1 OR
            "IN_LIBRAS" = 1 OR
            "IN_TEMPO_ADICIONAL" = 1 OR
            "IN_LEITURA_LABIAL" = 1 OR
            "IN_MESA_CADEIRA_RODAS" = 1)
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
    elif(filtro_questao == 'nenhum' or filtro_questao == 'vazio'):
        filtro_questao = ''
    else:
        filtro_questao = ' "' + filtro_questao + '", '

    if(filtro_sexo != 'vazio' and filtro_sexo != 'todos'):
        filtro_sexo = ' AND "TP_SEXO" = '+"'"+str(filtro_sexo)+"' "
    else:
        filtro_sexo = ''
        
    amostragem = ''
    if(filtro_amostra!="todos_os_dados"):  
        conect_db.LIMIT = filtro_amostra    
        valor=0 
        if(conect_db.LIMIT == 'a_5_90'):
            if(filtro_ano=='2019'):
                valor = 273
            elif(filtro_ano=='2018'):
                valor = 273
            elif(filtro_ano=='2017'):
                valor = 273
        elif(conect_db.LIMIT == 'a_3_95'):
            if(filtro_ano=='2019'):
                valor = 1067
            elif(filtro_ano=='2018'):
                valor = 1067
            elif(filtro_ano=='2017'):
                valor = 1067
        elif(conect_db.LIMIT == 'a_1_99'):
            if(filtro_ano=='2019'):
                valor = 16567
            elif(filtro_ano=='2018'):
                valor = 16571
            elif(filtro_ano=='2017'):
                valor = 16579
        if(valor!=0):
            conect_db.LIMIT = (" LIMIT "+str(valor))
            amostragem = ' ORDER BY RANDOM() '
    else:
        conect_db.LIMIT = ""
    
    # if(conect_db.LIMIT == ' LIMIT 1000' or conect_db.LIMIT == ' LIMIT 0' or conect_db.LIMIT == ""):
    #     amostragem =''
    # else:
    #     pass

    filtro = (  filtro_deficiencia + 
                filtro_sexo +
                filtro_cidade +
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
                filtro_variavel_de_analise +
                amostragem +
                conect_db.LIMIT)
    
    return filtro
