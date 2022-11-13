from django.shortcuts import render
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from io import BytesIO
import pandas as pd
import plotly.express as px
import base64
from edados.formularios.formulario_3.formulario_3 import Formulario_3
from edados.formularios.filtros.filtros import Formulario_filtros
import numpy as np
from edados.database import bd_formulario_3

def formatar(valor):
    return "{:,.2f}".format(valor)

def formulario_3(request):

    filtro_cor_da_prova = '503'
    prova = 'TP_SEXO'

    if request.method == 'GET':        
        menssagem = ("Formulário 3.")

        form = Formulario_3()
        form_filtro = Formulario_filtros()
        context = {
            'form' : form,
            'menssagem' : menssagem,
            'form_filtro' : form_filtro
        }
        return render(request, 'base/formulario_3/quest_formulario_3.html', context=context)
    else:


        # Recebendo fomulario da tela
        form = Formulario_3(request.POST)
        form_filtro = Formulario_filtros(request.POST)

        # Variáveis vindas do Formulario
        filtro_cor_da_prova = form.data['cor_da_prova']
        prova = form.data['prova']
        filtro_deficiencia = form.data['deficiencia']

        # Formulario de Filtro
        filtro_sexo = form_filtro.data['sexo']
        filtro_ano = form_filtro.data['ano']

        if(filtro_sexo != 'ambos'):
            Amostra = [prova, 'TP_SEXO', "TX_RESPOSTAS_CN", "TX_GABARITO_CN"]
            Microdado_Amostra = bd_formulario_3.buscar_dataframe_no_banco(Amostra, filtro_sexo=filtro_sexo, filtro_cor_da_prova=filtro_cor_da_prova, filtro_deficiencia=filtro_deficiencia, filtro_ano=filtro_ano)
        else:
            Amostra = [prova, "TX_RESPOSTAS_CN", "TX_GABARITO_CN"]
            Microdado_Amostra = bd_formulario_3.buscar_dataframe_no_banco(Amostra, filtro_cor_da_prova=filtro_cor_da_prova, filtro_deficiencia=filtro_deficiencia, filtro_ano=filtro_ano)


        menssagem = 'Formulário 3'

        Microdado_Amostra.reset_index(inplace=True)
        resposta = Microdado_Amostra['TX_RESPOSTAS_CN']
        quantidade_de_respostas = (Microdado_Amostra['TX_RESPOSTAS_CN'].count()-1)
        gabarito = Microdado_Amostra['TX_GABARITO_CN']

        acertos = [0]*46
        linha_do_gabarito = gabarito[1]

        for j in range(0, 45):
            for i in range(0, quantidade_de_respostas):
                print(i)
                print(quantidade_de_respostas)
                print('resposta[i]:'+resposta[i])
                if(resposta[i] == ''):
                    resposta[i] = "............................................."
                linha_da_resposta = resposta[i]
                print("linha_da_resposta[j] :" +linha_da_resposta[j] )

                resposta_gabarito = linha_do_gabarito[j]
                resposta_candidato = linha_da_resposta[j]

                if resposta_candidato == resposta_gabarito:
                    x = (j+1)
                    acertos[x] = acertos[x] + 1
                    resposta_candidato = ''

        acertos_pd = pd.DataFrame(acertos)

        fig = px.bar(acertos_pd)

        fig.update_layout(
            title_text = 'Tabela de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
            height = 500
        )

        relatorio = fig.to_html()

        context = {
            'form' : form,
            'form_filtro' : form_filtro,
            'menssagem' : menssagem,
            'relatorio' : relatorio
        }

    return render(request, 'base/formulario_3/relatorio_formulario_3.html', context=context)
    

def acertos_quantidade(Microdado_Amostra, prova, cor_da_prova):

        width = 0.25         # A largura das barras

        DataFrame = Microdado_Amostra.sort_values(by=[cor_da_prova])
        DataFrame = DataFrame.groupby([prova, cor_da_prova])
        DataFrame = DataFrame[prova].count()
        Dataset_F = DataFrame['F']
        Dataset_M = DataFrame['M']
            
        figura = plt.figure(figsize=(12, 8))
        figura.suptitle('Relatório de Compreenssão em formato de gráfico, \n'+
        'realizando o comparativo entre: Questão Socioeconômica e Desempenho no ENEM', size=16)
        figura.add_subplot(1,1,1)

        br1 = np.arange(len(Dataset_F.index))
        br2 = [x + width for x in br1]

        bar_label_feminino = plt.bar(br1, Dataset_F, color='y', width=width, label="feminíno")
        bar_label_masculino = plt.bar(br2, Dataset_M, color='b', width=width, label="masculíno")
        
        plt.bar_label(bar_label_feminino, fmt='%.2f', padding=2)
        plt.bar_label(bar_label_masculino, fmt='%.2f', padding=2)

        labels = np.arange(len(Dataset_F.index.tolist()))
        print(labels)
        plt.xticks(labels, Dataset_F.index.tolist())

        plt.legend(loc='center', bbox_to_anchor=(0.9, 1))
        plt.title(cor_da_prova)
        plt.ylabel('Quantidade de Inscritos por Questão Demográfica')
        plt.xlabel('Respostas da Questão Socioeconômica')

        buffer = BytesIO()
        plt.savefig(buffer, format='png', facecolor='#e8eeff')
        buffer.seek(0)
        image_png = buffer.getvalue()
        image = base64.b64encode(image_png)
        imagem_relatorio = image.decode('utf-8')
        buffer.close()

        # rotacionar 
        DataFrame = DataFrame.unstack()

        lista_dos_index = DataFrame.index.to_list()
        print(lista_dos_index)

        # desrotacionar 
        DataFrame = DataFrame.stack()

        fig = go.Figure()

        for index in lista_dos_index:
            print(index)
            if index=='M':
                nome = 'masculíno'
            else:
                nome = 'feminíno'
            fig.add_bar(
                y=DataFrame[index],
                x=DataFrame[index].index,
                name = nome,

            )
            
        fig.update_layout(
            title_text = 'Tabela de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
            height = 500
        )

        relatorio = fig.to_html()


        relatorio_em_tabela = relatorio
        figura_tabela_masculino = relatorio

        return [imagem_relatorio, relatorio, relatorio_em_tabela, figura_tabela_masculino]

def prova_instituicao_aonde_conclui_ensino_medio(Microdado_Amostra, prova, cor_da_prova):

        width = 0.25         # A largura das barras

        DataFrame = Microdado_Amostra.sort_values(by=[cor_da_prova])
        DataFrame = DataFrame.groupby([prova, cor_da_prova])
        DataFrame = DataFrame[prova].count()

        # rotacionar 
        DataFrame = DataFrame.unstack()

        lista_dos_index = DataFrame.index.to_list()
        print(lista_dos_index)

        # desrotacionar 
        DataFrame = DataFrame.stack()

        fig = go.Figure()

        for index in lista_dos_index:
            print(index)
            if index=='0':
                nome = 'Não informou'
            elif index=='1':
                nome = 'Pública'
            elif index=='2':
                nome = 'Privada'
            else:
                nome = 'Exterior'
            fig.add_bar(
                y=DataFrame[index],
                x=DataFrame[index].index,
                name = nome,

            )
            
        fig.update_layout(
            title_text = 'Tabela de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
            height = 500
        )

        relatorio = fig.to_html()

        return [relatorio]