import csv
import os
from django.http import HttpResponse
from edados.database import bd_formulario_1_4
from celery import shared_task
from django.contrib import messages

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

    # Sua lógica em segundo plano aqui
    
    # Após a conclusão da função em segundo plano
    menssagem_segundo_plano = "Deu certo, meu chapa!"
    messages.success( menssagem_segundo_plano)
    
    # Retorna uma resposta vazia
    return HttpResponse()
