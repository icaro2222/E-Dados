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
        filtro_deficiencia = form.data['deficiencia']
        acerto_erro = form.data['acerto_erro']

        # Formulario de Filtro
        filtro_sexo = form_filtro.data['sexo']
        filtro_ano = form_filtro.data['ano']

        if(filtro_cor_da_prova == '503' or 
            filtro_cor_da_prova == '504' or
            filtro_cor_da_prova == '505' or
            filtro_cor_da_prova == '506' or
            filtro_cor_da_prova == '519' or
            filtro_cor_da_prova == '523' or
            filtro_cor_da_prova == '543' or
            filtro_cor_da_prova == '544' or
            filtro_cor_da_prova == '545' or
            filtro_cor_da_prova == '546'):
            prova = 'CO_PROVA_CN'
        elif(filtro_cor_da_prova == '507' or 
            filtro_cor_da_prova == '508' or
            filtro_cor_da_prova == '509' or
            filtro_cor_da_prova == '510' or
            filtro_cor_da_prova == '520' or
            filtro_cor_da_prova == '524' or
            filtro_cor_da_prova == '547' or
            filtro_cor_da_prova == '548' or
            filtro_cor_da_prova == '549' or
            filtro_cor_da_prova == '550' or
            filtro_cor_da_prova == '564'):
            prova = 'CO_PROVA_CH'
        elif(filtro_cor_da_prova == '511' or 
            filtro_cor_da_prova == '512' or
            filtro_cor_da_prova == '513' or
            filtro_cor_da_prova == '514' or
            filtro_cor_da_prova == '521' or
            filtro_cor_da_prova == '525' or
            filtro_cor_da_prova == '551' or
            filtro_cor_da_prova == '552' or
            filtro_cor_da_prova == '553' or
            filtro_cor_da_prova == '554' or
            filtro_cor_da_prova == '565'):
            prova = 'CO_PROVA_LC'
        elif(filtro_cor_da_prova == '515' or
            filtro_cor_da_prova == '516' or
            filtro_cor_da_prova == '517' or
            filtro_cor_da_prova == '518' or
            filtro_cor_da_prova == '522' or
            filtro_cor_da_prova == '526' or
            filtro_cor_da_prova == '555' or
            filtro_cor_da_prova == '556' or
            filtro_cor_da_prova == '557' or
            filtro_cor_da_prova == '558'):
            prova = 'CO_PROVA_MT'

        # Formulario de Filtro
        if prova == 'CO_PROVA_LC':
            respostas = "TX_RESPOSTAS_LC"
            gabarito = "TX_GABARITO_LC"
        elif prova == 'CO_PROVA_CN':
            respostas = "TX_RESPOSTAS_CN"
            gabarito = "TX_GABARITO_CN"
        elif prova == 'CO_PROVA_MT':
            respostas = "TX_RESPOSTAS_MT"
            gabarito = "TX_GABARITO_MT"
        elif prova == 'CO_PROVA_CH':
            respostas = "TX_RESPOSTAS_CH"
            gabarito = "TX_GABARITO_CH"

        if(filtro_sexo != 'ambos'):
            Amostra = [prova, 'TP_SEXO', respostas, gabarito]
            Microdado_Amostra = bd_formulario_3.buscar_dataframe_no_banco(Amostra, filtro_sexo=filtro_sexo, filtro_cor_da_prova=filtro_cor_da_prova, filtro_deficiencia=filtro_deficiencia, filtro_ano=filtro_ano)
        else:
            Amostra = [prova, respostas, gabarito]
            Microdado_Amostra = bd_formulario_3.buscar_dataframe_no_banco(Amostra, filtro_cor_da_prova=filtro_cor_da_prova, filtro_deficiencia=filtro_deficiencia, filtro_ano=filtro_ano)


        menssagem = 'Formulário 3'

        Microdado_Amostra.reset_index(inplace=True)
        resposta = Microdado_Amostra[respostas]
        quantidade_de_respostas = (Microdado_Amostra[respostas].count()-1)
        gabarito = Microdado_Amostra[gabarito]

        acertos = [0]*46
        acertos_porcentagem = [0]*46
        if(quantidade_de_respostas >= 0):
            linha_do_gabarito = gabarito[quantidade_de_respostas]

        for j in range(0, 45):
            for i in range(0, quantidade_de_respostas):
                # print(i)
                # print(quantidade_de_respostas)
                # print('resposta[i]:'+resposta[i])
                # print("linha_da_resposta[j] :" +linha_da_resposta[j] )
                if(resposta[i] == ''):
                    resposta[i] = "............................................."
                linha_da_resposta = resposta[i]

                resposta_gabarito = linha_do_gabarito[j]
                resposta_candidato = linha_da_resposta[j]
                
                if acerto_erro == 'acertos':
                    if resposta_candidato == resposta_gabarito:
                        acertos[j] = acertos[j] + 1
                        resposta_candidato = ''
                else:
                    if resposta_candidato != resposta_gabarito:
                        acertos[j] = acertos[j] + 1
                        resposta_candidato = ''

            acertos_porcentagem[j+1] = (acertos[j] / quantidade_de_respostas)*100
        
        # print(acertos_porcentagem)
        acertos_pd = pd.DataFrame(acertos_porcentagem)
        
        # Colocando nome no DataFrame
        acertos_pd.columns = ['porcentagem_de_acertos']
        texto = acertos_pd.porcentagem_de_acertos
        
        print(texto)


        fig = px.bar(acertos_pd,
        x= acertos_pd.index,
        y= acertos_pd['porcentagem_de_acertos'],
        # text= acertos_pd.porcentagem_de_acertos,
        text_auto=True,
        error_y= (acertos_pd.porcentagem_de_acertos / quantidade_de_respostas),
        # text_auto='.2s',
        title="Percentual Conforme os critérios estabelecidos",
        labels={'index':'Questão de número', 'porcentagem_de_acertos':'Porcentagem de acerto/erros'})

        fig.update_traces(
            # texttemplate='%{'+acertos_pd.porcentagem_de_acertos.to_list()+':.2s}', 
            # textposition='outside', 
            textfont_size=12, 
            # extangle=0, 
            # cliponaxis=False
            )

        fig.update_layout(
            xaxis=dict(
                # tickvals=acertos_pd.index,
                tickvals =acertos_pd.index,
                tickmode="array",
                titlefont=dict(size=10),
            ),
            title="Percentual Conforme os critérios estabelecidos",
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
            height = 500,
            font=dict(
                family="Courier New, monospace",
                size=12,
                color="black"
            )
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
            height = 500,
            font=dict(
                family="Courier New, monospace",
                size=12,
                color="black"
            )
        )

        relatorio = fig.to_html()

        return [relatorio]