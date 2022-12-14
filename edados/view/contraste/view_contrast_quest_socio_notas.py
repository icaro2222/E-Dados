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
from edados.formularios.contraste.form_contrast_questao_e_notas import MeuFormulario
from edados.formularios.vazio.formulario_vazio import VazioFormulario
from edados.formularios.form_filtro import Formulario_filtro
from edados.settings import BASE_DIR
import numpy as np
from edados.database import bd_quest_socio_notas

caminho = os.path.join(BASE_DIR, 'dados/Microdado_Amostra.csv')

def logar(request):
    # return render(request, 'indexTest.html')
    
    return HttpResponse("Hum, DEU CERTO.")

def formatar(valor):
    return "{:,.2f}".format(valor)

def contrast_quest_socio_notas(request):

    Q = 'TP_SEXO'
    prova = 'NU_NOTA_MT'

    if request.method == 'GET':
        form = MeuFormulario()

        if form.is_valid():
            print(form.changed_data)

        menssagem = ("""Introdução:\nNesta tela você irá poder realizar uma análise 
        comparativa entre inscritos com e sem deficiência, no quesito 
        questões socioeconômicas e o desempenho nas provas, 
        realizadas durante o exame.\n""")

        menssagem_2= ("""Sendo possivel fazer uma filtragem por gêreno.\n
        Objetivo:\nPossibilitar a análise e visualisação do resultado em formato de tabelas e gráficos\n
        , e permitindo com que os usuários entrem com metricas e fatores a serem analisador.\n
        O que se espera?\n Ao termino da análise terá se resultados que tentam entregar ao usuário informações que 
        "são facies e simples de se compreender.""")

        context = {
            'form' : form,
            'menssagem' : menssagem,
            'menssagem_2' : menssagem_2
        }
        return render(request, 'base/contraste/quest_contraste_socio_notas.html', context=context)
    else:
        form = MeuFormulario(request.POST)
        form_vazio = VazioFormulario()
        form_ano = Formulario_filtro()

        Q = form.data['Questao_Socioeconomica_Com_Deficiencia']
        prova = form.data['Nota_da_prova_Com_Deficiencia']
        
        # Processo de pegar os dados para a realização da análise
        Amostra = [prova, Q, 'TP_SEXO']
        Microdado_Amostra = bd_quest_socio_notas.buscar_dataframe_no_banco(Amostra)

        # realizando um agrupamento, para criar uam estrutura para a análise
        ChAmostra = Microdado_Amostra.filter(items = Amostra)
        ChAmostra = ChAmostra.sort_values(by=[Q])
        dados = ChAmostra.groupby(Q)[prova]
        dados = dados.describe()

        NU_NOTA_CNCHAmostra = ChAmostra[prova]
        
        width = 0.25         # A largura das barras
        plt.figure(figsize=(0,0))

        r1 = np.arange(len(NU_NOTA_CNCHAmostra))
        r2 = [x + width for x in r1]


        mpl.rcParams['lines.linewidth'] = 2
        mpl.rcParams['lines.linestyle'] = '--'

        figura = plt.figure(figsize=(17, 29))
        figura.suptitle('Relatório de Compreenssão em formato de gráfico, \n'+
        'realizando o comparativo entre: Questão Socioeconômica e Desempenho no ENEM', size=26)
        
        figura.add_subplot(6,2,1)
        bar_label_mean = plt.bar(dados.index, dados['mean'], color='#BA5ACD', width=width, label="média")
        plt.scatter(dados.index, dados['max'], color='#FA1AFD', label="máximo")
        plt.bar_label(bar_label_mean)
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24, y=1)
        plt.ylabel('Nota Média Global no Exame')
        plt.xlabel('Questão Socioeconômica')

        figura.add_subplot(6,2,2)
        plt.scatter(dados.index, dados['mean'],  c='k', label='Média')
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Nota Média Global no Exame')
        plt.xlabel('Questão Socioeconômica')

        figura.add_subplot(6,2,3)
        plt.bar(dados.index, dados['count'], color='r', width=width, label="quantidade")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Quantidade de Respostas')
        plt.xlabel('Questão Socioeconômica')

        figura.add_subplot(6,2,4)
        plt.plot(dados.index, dados['count'], color='#BA7ACD', label="quantidade")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Quantidade de Respostas')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6,2,5)
        plt.bar(dados.index, dados['25%'], color='y', width=width, label="25%")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Nota ate 25%/ Global no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6,2,6)
        plt.plot(dados.index, dados['25%'], color='b', label="25%")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Nota ate 25%/ Global no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6,2,7)
        plt.bar(dados.index, dados['50%'], color='#EA5ACD', width=width, label="50%")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Nota até 50%/ Global no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6,2,8)
        plt.plot(dados.index, dados['50%'], color='#EA5ACD', label="50%")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Nota até 50%/ Global no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6,2,9)
        plt.bar(dados.index, dados['max'], color='#AA5ACD', width=width, label="máximo")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Nota Máxima no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6, 2, 10)
        plt.scatter(dados.index, dados['max'], color='#AA5ACD',  label="máximo")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Nota Máxima no Exame')
        plt.xlabel('Questão Socioeconômica')
        
        # plt.show(figura)
        buffer = BytesIO()
        savefig = plt.savefig(buffer, format='png', facecolor='#e8eeff')
        # nome_do_relatorio = 'dados_relatorio/' + str(uuid.uuid4()) + '.pdf'
        # nome_destino_do_relatorio = str(BASE_DIR) + '/static/' + nome_do_relatorio
        # plt.savefig(fname=nome_destino_do_relatorio, format='pdf', facecolor='#e8eeff')
        # plt.savefig(fname='dados/Relatório comparativo entre Questões Socioeconômicas e Desempenho no Enem.pdf' , format='pdf')
        buffer.seek(0)
        image_png = buffer.getvalue()
        image = base64.b64encode(image_png)
        imagem_relatorio = image.decode('utf-8')
        buffer.close()

        rowEvenColor = 'lightgrey'
        rowOddColor = 'white'

        fig = go.Figure(data=[go.Table(
                header=dict(
                    values=['Respostas', 'medias', 'máximo', 'quant alunos', '25%', '50%', '75%'],
                    fill_color='royalblue',
                    height=40,
                    line_color='darkslategray',
                    align=['left','center'],
                    font=dict(color='white', size=12)
                ),
                cells=dict(
                    values=[dados.index,
                    dados['mean'].apply(formatar), dados['max'], dados['count'], dados['25%'].apply(formatar), dados['50%'].apply(formatar), dados['75%'].apply(formatar)],
                    line_color='darkslategray',
                    # 2-D list of colors for alternating rows
                    fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
                    align = ['left', 'center'],
                    font = dict(color = 'darkslategray', size = 11)
                    ))
                ])

        relatorio_em_tabela = fig.to_html()
        fig = px.line(dados)
        relatorio_linha = fig.to_html()

        Q = form.data['Questao_Socioeconomica_Sem_Deficiencia']
        prova = form.data['Nota_da_prova_Sem_Deficiencia']

        # Processo de pegar os dados para a realização da análise
        Amostra = [prova, Q, 'TP_SEXO']
        Microdado_Amostra = bd_quest_socio_notas.buscar_dataframe_no_banco(Amostra)

        # realizando um agrupamento, para criar uam estrutura para a análise
        ChAmostra = Microdado_Amostra.filter(items = Amostra)
        ChAmostra = ChAmostra.sort_values(by=[Q])
        dados = ChAmostra.groupby(Q)[prova]
        dados = dados.describe()

        NU_NOTA_CNCHAmostra = ChAmostra[prova]
        
        width = 0.25         # A largura das barras
        plt.figure(figsize=(0,0))

        r1 = np.arange(len(NU_NOTA_CNCHAmostra))
        r2 = [x + width for x in r1]


        mpl.rcParams['lines.linewidth'] = 2
        mpl.rcParams['lines.linestyle'] = '--'

        figura = plt.figure(figsize=(17, 29))
        figura.suptitle('Relatório de Compreenssão em formato de gráfico, \n'+
        'realizando o comparativo entre: Questão Socioeconômica e Desempenho no ENEM', size=26)
        
        figura.add_subplot(6,2,1)
        bar_label_mean = plt.bar(dados.index, dados['mean'], color='#BA5ACD', width=width, label="média")
        plt.scatter(dados.index, dados['max'], color='#FA1AFD', label="máximo")
        plt.bar_label(bar_label_mean)
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24, y=1)
        plt.ylabel('Nota Média Global no Exame')
        plt.xlabel('Questão Socioeconômica')

        figura.add_subplot(6,2,2)
        plt.scatter(dados.index, dados['mean'],  c='k', label='Média')
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Nota Média Global no Exame')
        plt.xlabel('Questão Socioeconômica')

        figura.add_subplot(6,2,3)
        plt.bar(dados.index, dados['count'], color='r', width=width, label="quantidade")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Quantidade de Respostas')
        plt.xlabel('Questão Socioeconômica')

        figura.add_subplot(6,2,4)
        plt.plot(dados.index, dados['count'], color='#BA7ACD', label="quantidade")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Quantidade de Respostas')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6,2,5)
        plt.bar(dados.index, dados['25%'], color='y', width=width, label="25%")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Nota ate 25%/ Global no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6,2,6)
        plt.plot(dados.index, dados['25%'], color='b', label="25%")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Nota ate 25%/ Global no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6,2,7)
        plt.bar(dados.index, dados['50%'], color='#EA5ACD', width=width, label="50%")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Nota até 50%/ Global no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6,2,8)
        plt.plot(dados.index, dados['50%'], color='#EA5ACD', label="50%")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Nota até 50%/ Global no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6,2,9)
        plt.bar(dados.index, dados['max'], color='#AA5ACD', width=width, label="máximo")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Nota Máxima no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6, 2, 10)
        plt.scatter(dados.index, dados['max'], color='#AA5ACD',  label="máximo")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Nota Máxima no Exame')
        plt.xlabel('Questão Socioeconômica')
        
        # plt.show(figura)
        buffer = BytesIO()
        savefig = plt.savefig(buffer, format='png', facecolor='#e8eeff')
        # nome_do_relatorio = 'dados_relatorio/' + str(uuid.uuid4()) + '.pdf'
        # nome_destino_do_relatorio = str(BASE_DIR) + '/static/' + nome_do_relatorio
        # plt.savefig(fname=nome_destino_do_relatorio, format='pdf', facecolor='#e8eeff')
        # plt.savefig(fname='dados/Relatório comparativo entre Questões Socioeconômicas e Desempenho no Enem.pdf' , format='pdf')
        buffer.seek(0)
        image_png = buffer.getvalue()
        image = base64.b64encode(image_png)
        imagem_relatorio1 = image.decode('utf-8')
        buffer.close()

        rowEvenColor = 'lightgrey'
        rowOddColor = 'white'

        fig = go.Figure(data=[go.Table(
                header=dict(
                    values=['Respostas', 'medias', 'máximo', 'quant alunos', '25%', '50%', '75%'],
                    fill_color='royalblue',
                    height=40,
                    line_color='darkslategray',
                    align=['left','center'],
                    font=dict(color='white', size=12)
                ),
                cells=dict(
                    values=[dados.index,
                    dados['mean'].apply(formatar), dados['max'], dados['count'], dados['25%'].apply(formatar), dados['50%'].apply(formatar), dados['75%'].apply(formatar)],
                    line_color='darkslategray',
                    # 2-D list of colors for alternating rows
                    fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
                    align = ['left', 'center'],
                    font = dict(color = 'darkslategray', size = 11)
                    ))
                ])

        relatorio_em_tabela1 = fig.to_html()

        fig = px.line(dados)
        relatorio_linha1 = fig.to_html()

        context = {
            'form_ano' : form_ano,
            'form' : form,
            'form_vazio' : form_vazio,
            'imagem_relatorio' : imagem_relatorio,
            'imagem_relatorio1' : imagem_relatorio1,
            # 'nome_do_relatorio' : nome_do_relatorio,
            'relatorio_em_tabela' : relatorio_em_tabela,
            'relatorio' : relatorio_linha,
            'relatorio_em_tabela1' : relatorio_em_tabela1,
            'relatorio1' : relatorio_linha1,
            'dados' : dados
        }

    return render(request, 'base/contraste/relatorio_contrast_quest_socio_notas.html', context=context)
    
