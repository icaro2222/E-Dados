import os
from typing import Sized
import uuid
from django.shortcuts import render
import plotly.graph_objects as go 
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import matplotlib as mpl
import plotly.express as px
import base64
import pyodbc
from edados.formularios.form_questao_e_notas_deficiencia import MeuFormulario
from edados.formularios.form_filtro import MeuFormulario as Formulario_filtro
from edados.settings import BASE_DIR
import numpy as np
from edados.database import conect_db, engine

caminho = os.path.join(BASE_DIR, 'dados/Microdado_Amostra.csv')
caminho2 = os.path.join(BASE_DIR, 'dados/')

def formatar(valor):
    return "{:,.2f}".format(valor)

def Quest_Soc_Notas_Deficiencia(request):

    Q = 'TP_SEXO'
    prova = 'NU_NOTA_MT'

    if request.method == 'GET':        
        menssagem = ("Correlação entre pessoas com e sem deficiência, no quesito socioeconômico e desempenho no exame.")

        form = MeuFormulario()
        form_filtro = Formulario_filtro()
        context = {
            'form' : form,
            'menssagem' : menssagem,
            'form_filtro' : form_filtro
        }
        return render(request, 'base/quest_socio_notas_deficiencia.html', context=context)
    else:


        # Recebendo fomulario da tela
        form = MeuFormulario(request.POST)
        form_filtro = Formulario_filtro(request.POST)

        # Variáveis vindas do Formulario
        Q = form.data['questao']
        prova = form.data['nota']
        filtro_deficiencia = form.data['deficiencia']

        # Formulario de Filtro
        filtro_sexo = form_filtro.data['sexo']

        # Microdado_Amostra = pd.read_csv(caminho, sep= ';', encoding = "ISO-8859-1", nrows= 20000 )
        
        if(filtro_sexo != 'ambos'):
            Amostra = [prova, Q, 'TP_SEXO']
            if(filtro_deficiencia != 'ambos'):
                Microdado_Amostra = engine.buscar_dataframe_no_banco(Amostra, filtro_sexo=filtro_sexo, filtro_deficiencia=filtro_deficiencia)
            else:
                Microdado_Amostra = engine.buscar_dataframe_no_banco(Amostra, filtro_sexo=filtro_sexo)
        else:
            Amostra = [prova, Q]
            if(filtro_deficiencia != 'ambos'):
                Microdado_Amostra = engine.buscar_dataframe_no_banco(Amostra, filtro_deficiencia=filtro_deficiencia)
            else:
                Microdado_Amostra = engine.buscar_dataframe_no_banco(Amostra)

        width = 0.25         # A largura das barras

        DataFrame_sem_deficiencia = Microdado_Amostra.filter(items = Amostra)
        DataFrame_sem_deficiencia = DataFrame_sem_deficiencia.sort_values(by=[Q])
        DataFrame_sem_deficiencia = DataFrame_sem_deficiencia.groupby(Q)[prova]
        DataFrame_sem_deficiencia = DataFrame_sem_deficiencia.describe()     

        # Seleção conforme a escolha do usuário na tela do formulario
        if filtro_deficiencia == 'ambos':
            br1 = np.arange(len(DataFrame_sem_deficiencia.index))
            br2 = [x + width for x in br1]

            figura = plt.figure(figsize=(12, 8))
            figura.suptitle('Relatório de Compreenssão em formato de gráfico, \n'+
            'realizando o comparativo entre: Questão Socioeconômica e Desempenho no ENEM', size=16)
            figura.add_subplot(1,1,1)

            bar_label_mean = plt.bar(br2, DataFrame_sem_deficiencia['mean'], color='r', width=width, label="Média")
            plt.bar_label(bar_label_mean, fmt='%.2f', padding=2)

        else:
            # caminho_a_deficiencia = caminho2 + filtro_deficiencia + '.csv'
            # Microdado_Amostra = pd.read_csv(caminho_a_deficiencia, sep= ';', encoding = "ISO-8859-1")
            # DataFrame = Microdado_Amostra.filter(items = Amostra)
            # DataFrame = DataFrame.sort_values(by=[Q])
            # DataFrame_dificiente = DataFrame[DataFrame[filtro_deficiencia]==1]

            # DataFrame_dificiente = DataFrame_dificiente.sort_values(by=[Q])
            # dados = DataFrame_dificiente.groupby(Q)[prova]
            # dados_deficiente = dados.describe()
            dados_deficiente = DataFrame_sem_deficiencia
      # A largura das barras
            figura = plt.figure(figsize=(12, 8))
            figura.suptitle('Relatório de Compreenssão em formato de gráfico, \n'+
            'realizando o comparativo entre: Questão Socioeconômica e Desempenho no ENEM', size=16)
            figura.add_subplot(1,1,1)

            br1 = np.arange(len(dados_deficiente.index))
            br2 = [x + width for x in br1]
            br3 = [x + width for x in br2]
            bar_label_mean_com_deficiencia = plt.bar(br1, dados_deficiente['mean'], color='b', width=width, label="Deficiênte")
            
            br1 = np.arange(len(DataFrame_sem_deficiencia.index))
            br2 = [x + width for x in br1]
            br3 = [x + width for x in br2]
            bar_label_mean_sem_deficiencia = plt.bar(br2, DataFrame_sem_deficiencia['mean'], color='r', width=width, label="Não Deficiênte")
            # plt.scatter(dados.index, dados['max'], color='#FA1AFD', label="máximo")
        
            # bar_label_mean = plt.bar({dados['max'], dados['mean']}, index=dados.index, color='b', width=width, label="média")
            
            plt.bar_label(bar_label_mean_sem_deficiencia, fmt='%.2f', padding=2)
            plt.bar_label(bar_label_mean_com_deficiencia, fmt='%.2f', padding=2)

        plt.legend(loc='center left', bbox_to_anchor=(0.9, 1))
        plt.title(Q)
        plt.ylabel('Nota Média dos Inscritos')
        plt.xlabel('Questão Socioeconômica')

        buffer = BytesIO()
        savefig = plt.savefig(buffer, format='png', facecolor='#e8eeff')
        nome_do_relatorio = 'dados_relatorio/' + str(uuid.uuid4()) + '.pdf'
        nome_destino_do_relatorio = str(BASE_DIR) + '/static/' + nome_do_relatorio
        plt.savefig(fname=nome_destino_do_relatorio, format='pdf', facecolor='#e8eeff')
        buffer.seek(0)
        image_png = buffer.getvalue()
        image = base64.b64encode(image_png)
        imagem_relatorio = image.decode('utf-8')
        buffer.close()

        fig = px.line(DataFrame_sem_deficiencia)
        relatorio = fig.to_html()

        figura_com_criador_de_tabela = px.bar(DataFrame_sem_deficiencia)
        figura_com_criador_de_tabela = figura_com_criador_de_tabela.to_html()

        figura_tabela_da_media = px.bar(DataFrame_sem_deficiencia['mean'])
        figura_tabela_da_media = figura_tabela_da_media.to_html()

        headerColor = 'grey'
        rowEvenColor = 'lightgrey'
        rowOddColor = 'white'

        figura_tabela = go.Figure(data=[go.Table(
                header=dict(
                    values=['Respostas', 'medias', 'máximo', 'quant alunos', '25%', '50%', '75%'],
                    fill_color='royalblue',
                    height=40,
                    line_color='darkslategray',
                    align=['left','center'],
                    font=dict(color='white', size=12)
                ),
                cells=dict(
                    values=[DataFrame_sem_deficiencia.index,
                    DataFrame_sem_deficiencia['mean'].apply(formatar), DataFrame_sem_deficiencia['max'], 
                    DataFrame_sem_deficiencia['count'], DataFrame_sem_deficiencia['25%'].apply(formatar), 
                    DataFrame_sem_deficiencia['50%'].apply(formatar), DataFrame_sem_deficiencia['75%'].apply(formatar)],
                    line_color='darkslategray',
                    # 2-D list of colors for alternating rows
                    fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
                    align = ['left', 'center'],
                    font = dict(color = 'darkslategray', size = 11)
                    ))
                ])

        
        # Adicionando Gráfico ao Datarame
        # teams = ['Montréal Canadiens', 'Dallas Stars', 'NY Rangers',
        #         'Boston Bruins', 'Chicago Blackhawks', 'Ottawa Senators']
        # GFPG = [3.54, 3.48, 3.0, 3.27, 2.83, 3.18]
        # GAPG = [2.17, 2.57, 2.0, 2.91, 2.57, 2.77]

        # figura_tabela.add_trace(go.Bar(x=teams, y=GFPG, xaxis='x2', yaxis='y2',
        #                 marker=dict(color='#0099ff'),
        #                 name='Goals For<br>Per Game'))

        # figura_tabela.add_trace(go.Bar(x=DataFrame_sem_deficiencia['mean'], y=DataFrame_sem_deficiencia.index))
        figura_tabela.add_trace(go.Bar(x=DataFrame_sem_deficiencia.index, y=DataFrame_sem_deficiencia['max']))
        figura_tabela.add_trace(go.Bar(x=DataFrame_sem_deficiencia.index, y=DataFrame_sem_deficiencia['mean']))

        figura_tabela.update_layout(
            title_text = 'Pessoas Com Deficiência X Pessoas Sem Deficiência',
            height = 800,
            margin = {'t':75, 'l':50},
            yaxis = {'domain': [0, .45]},
            xaxis2 = {'anchor': 'y2'},
            yaxis2 = {'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'}
        )

        relatorio_em_tabela = figura_tabela.to_html()

        if form.is_valid():
            print(form.changed_data)
        else:
            pass

        context = {
            'form' : form,
            'imagem_relatorio' : imagem_relatorio,
            'nome_do_relatorio' : nome_do_relatorio,
            'relatorio' : relatorio,
            'form_filtro' : form_filtro,
            'figura_com_criador_de_tabela' : figura_com_criador_de_tabela,
            'figura_tabela_da_media' : figura_tabela_da_media,
            'relatorio_em_tabela' : relatorio_em_tabela
        }

    return render(request, 'base/relatorio_quest_socio_notas_deficiencia.html', context=context)
    
