
from edados.formularios.filtros.formulario_1_filtros import Formulario_filtros
from edados.formularios.formulario_1.formulario_1_4 import Formulario
from sqlalchemy.orm import sessionmaker
from django.http import JsonResponse
from edados.database import bd_formulario_1_4
from celery import shared_task
from edados.database import conect_db
import csv
import os

def verificar_csv(request):
    # Aqui você pode executar a consulta SQL para obter o status atual do CSV
    
    engine = conect_db.connect()
    # Conectando com o Banco de Dados
    Session = sessionmaker(bind=engine)
    session = Session()
    comando_sql = """
        SELECT "status" FROM "csv" WHERE  "id"=1;
    """

    result = session.execute(comando_sql)
    status = result.scalar()  # Extrai o valor do resultado da consulta

    session.commit()
        
    # Retorna o status como uma resposta JSON
    response_data = {'status': status}
    return JsonResponse(response_data)


@shared_task
def criar_csv(
        filtro_sexo="filtro_sexo",
        filtro_recurso="filtro_recurso",
        filtro_ltp_adm_escola="filtro_ltp_adm_escola",
        filtro_ano_de_conclusao="filtro_ano_de_conclusao",
        filtro_localizacao_da_escola="filtro_localizacao_da_escola",
        filtro_amostra="filtro_amostra",
        filtro_estado="filtro_estado",
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
    comando_sql = """
        UPDATE "csv" SET "status"='andamento' WHERE  "id"=1;
            """

    session.execute(comando_sql)
    session.commit()
        
    Amostra = '*'
    Microdado_Amostra = bd_formulario_1_4.buscar_dataframe_no_banco(
        Amostra,
        filtro_sexo=filtro_sexo,
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


    # Caminho para a pasta onde deseja salvar o arquivo CSV
    pasta_destino = '/var/www/edados/static/csv/'

    # Nome do arquivo CSV
    nome_arquivo = 'microdados_enem.csv'

    # Caminho completo do arquivo CSV
    caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

    # Modifique esta linha
    with open(caminho_arquivo, 'w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(Microdado_Amostra.values.tolist())

    comando_sql = """
        UPDATE "csv" SET "status"='finalizado' WHERE  "id"=1;
            """

    session.execute(comando_sql)
    session.commit()
    print('---------------------------------------------------------------------------')
    print("FINALIZOU")
    # Modifique esta linha
    # Microdado_Amostra = Microdado_Amostra.to_csv(index=False)


    # O arquivo CSV foi salvo com sucesso na pasta especificada

    # # Cria o objeto response com o cabeçalho CSV
    # response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="microdados_enem.csv"'

    # # Cria o escritor CSV e escreve as linhas no objeto response
    # writer = csv.writer(response)

    # # Escreve as linhas do CSV
    # for row in csv.reader(Microdado_Amostra.splitlines()):
    #     writer.writerow(row)
    
    from django.shortcuts import render
    import json
    from django.shortcuts import redirect, reverse

    # Obtém a URL correspondente à view 'dashboard' com os argumentos corretos
    url = reverse('dashboard')
    
    # Redireciona o usuário para a URL obtida
    return redirect(url)


    # Sua lógica em segundo plano aqui
    menssagem_segundo_planos="CSV pronto para baixa!"
    form = Formulario()
    form_filtro = Formulario_filtros()
    menssagem = ("Análise de Dados Socioeconômicos do ENEM")
    menssagem1 = """Esta é uma tela web que permite realizar o somatório dos alunos que responderam ao ENEM. Esta tela também possui filtros que permitem reduzir o somatório para fins de análise dos microdados. O resultado desse somatório é obtido após a aplicação desses filtros."""
    context = {
        'form' : form,
        'menssagem' : menssagem,
        'menssagem1' : menssagem1,
        'form_filtro' : form_filtro
    }
    return redirect('dashboard', context=context)
