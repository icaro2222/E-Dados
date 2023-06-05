
from edados.formularios.filtros.formulario_1_filtros import Formulario_filtros
from edados.formularios.formulario_1.formulario_1_4 import Formulario
from sqlalchemy.orm import sessionmaker
from django.http import JsonResponse
from edados.database import bd_formulario_1_4
from celery import shared_task
from edados.database import conect_db
import os

def verificar_csv(request):
    # Aqui você pode executar a consulta SQL para obter o status atual do CSV
    
    engine = conect_db.connect()
    # Conectando com o Banco de Dados
    Session = sessionmaker(bind=engine)
    session = Session()
    comando_sql = """SELECT "status" FROM "csv" WHERE "nome"= '"""+ request.user.username+"';"
    print(comando_sql)
    

    result = session.execute(comando_sql)
    status = result.scalar()  # Extrai o valor do resultado da consulta

    session.commit()
        
    # Retorna o status como uma resposta JSON
    response_data = {'status': status}
    return JsonResponse(response_data)


@shared_task
def criar_csv(nome_usuario,
        filtro_sexo="filtro_sexo",
        filtro_recurso="filtro_recurso",
        filtro_ltp_adm_escola="filtro_ltp_adm_escola",
        filtro_ano_de_conclusao="filtro_ano_de_conclusao",
        filtro_localizacao_da_escola="filtro_localizacao_da_escola",
        filtro_amostra="filtro_amostra",
        filtro_estado="filtro_estado",
        filtro_cidade = "cidade",
        filtro_questao="filtro_questao",
        filtro_deficiencia="filtro_deficiencia",
        filtro_ano="filtro_ano",
        filtro_cor="filtro_cor",
        filtro_estado_civil="filtro_estado_civil",
        filtro_escola="filtro_escola",
        filtro_nacionalidade="filtro_nacionalidade"):
    
    print('---------------------------------------------------------------------------')
    print("FUNÇÃO DE IMPRIMIR CSV")
    
    
    engine = conect_db.connect()
    # Conectando com o Banco de Dados
    Session = sessionmaker(bind=engine)
    session = Session()
    comando_sql = """UPDATE "csv" SET "status"='andamento' WHERE  "nome"= '"""+ nome_usuario +"';"
    print(comando_sql)

    session.execute(comando_sql)
    session.commit()
        
    Amostra = '*'
    Microdado_Amostra = bd_formulario_1_4.buscar_dataframe_no_banco(
        Amostra,
        filtro_sexo=filtro_sexo,
        filtro_cidade=filtro_cidade, 
        filtro_recurso=filtro_recurso,
        filtro_ltp_adm_escola=filtro_ltp_adm_escola,
        filtro_ano_de_conclusao=filtro_ano_de_conclusao,
        filtro_localizacao_da_escola=filtro_localizacao_da_escola,
        filtro_amostra=filtro_amostra,
        filtro_estado=filtro_estado,
        filtro_questao=filtro_questao,
        filtro_deficiencia=filtro_deficiencia,
        filtro_ano=filtro_ano,
        filtro_cor=filtro_cor,
        filtro_estado_civil=filtro_estado_civil,
        filtro_escola=filtro_escola,
        filtro_nacionalidade=filtro_nacionalidade)

    from pathlib import Path

    # Caminho para o diretório do projeto
    BASE_DIR = Path(__file__).resolve().parents[2]

    # Caminho para a pasta onde deseja salvar o arquivo CSV
    pasta_destino = str(BASE_DIR) + '/static/csv/' + str(nome_usuario)+'/'

    # Nome do arquivo CSV
    nome_arquivo = 'microdados_enem.csv'
        
    # Caminho completo do arquivo CSV
    caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)
    print('---------------------------------------------------------------------------')
    print(caminho_arquivo)
    Microdado_Amostra.to_csv(caminho_arquivo, index=False)

    comando_sql = """
        UPDATE "csv" SET "status"='finalizado' WHERE   "nome"= '"""+ nome_usuario +"';"
    print(comando_sql)
    session.execute(comando_sql)
    session.commit()
    print('---------------------------------------------------------------------------')
    print("FINALIZOU")
    
    # O arquivo CSV foi salvo com sucesso na pasta especificada
    
    from django.shortcuts import redirect, reverse

    # Obtém a URL correspondente à view 'dashboard' com os argumentos corretos
    url = reverse('dashboard')
    
    # Redireciona o usuário para a URL obtida
    return redirect(url)