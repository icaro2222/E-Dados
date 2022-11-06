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
from edados.settings import BASE_DIR
import numpy as np
from edados.database import bd_quest_socio_notas

caminho = os.path.join(BASE_DIR, 'dados/Microdado_Amostra.csv')

def logar(request):
    # return render(request, 'indexTest.html')
    
    return HttpResponse("oi, DEUUUUUUU CERTTTTTOOOOOO. AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

def formatar(valor):
    return "{:,.2f}".format(valor)

def contrast_quest_socio_notas(request):

    Q = 'TP_SEXO'
    prova = 'NU_NOTA_MT'

    if request.method == 'GET':
        form_com_deficiencia = MeuFormulario(request.POST)
        form_sem_deficiencia = MeuFormulario(request.POST)

        if form_com_deficiencia.is_valid():
            print(form_com_deficiencia.changed_data)

        menssagem = ("""Introdução:\nNesta tela você irá poder realizar uma análise 
        comparativa entre inscritos com e sem deficiência, no quesito 
        questões socioeconômicas e o desempenho nas provas, 
        realizadas durante o exame.\n
        Sendo possivel fazer uma filtragem por gêreno.\n
        Objetivo:\nPossibilitar a análise e visualisação do resultado em formato de tabelas e gráficos\n
        , e permitindo com que os usuários entrem com metricas e fatores a serem analisador.\n
        O que se espera?\n Ao termino da análise terá se resultados que tentam entregar ao usuário informações que 
        "são facies e simples de se compreender.""")

        context = {
            'form_com_deficiencia' : form_com_deficiencia,
            'form_sem_deficiencia' : form_sem_deficiencia,
            'menssagem' : menssagem
        }
        return render(request, 'base/contraste/quest_contraste_socio_notas.html', context=context)
    else:
        form_sem_deficiencia = MeuFormulario(request.POST)
        form_com_deficiencia = MeuFormulario(request.POST)
        
        Q = form_sem_deficiencia.data['Questao_Socioeconomica']
        prova = form_sem_deficiencia.data['Nota_da_prova']
        
        questao_socioe_de_deficientes = form_com_deficiencia.data['Questao_Socioeconomica']
        nota_da_prova_de_deficientes = form_com_deficiencia.data['Nota_da_prova']

        # Processo de pegar os dados para a realização da análise
        Amostra = [prova, Q, 'TP_SEXO']
        Microdado_Amostra = bd_quest_socio_notas.buscar_dataframe_no_banco(Amostra)

        # realizando um agrupamento, para criar uam estrutura para a análise
        ChAmostra = Microdado_Amostra.filter(items = Amostra)
        ChAmostra = ChAmostra.sort_values(by=[Q])
        dados = ChAmostra.groupby(Q)[prova]
        dados = dados.describe()

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
        relatorio_em_tabela1 = fig.to_html()

        fig = px.line(dados)
        relatorio_linha = fig.to_html()
        relatorio_linha1 = fig.to_html()

        context = {
            'form_com_deficiencia' : form_com_deficiencia,
            'form_sem_deficiencia' : form_sem_deficiencia,
            # 'imagem_relatorio' : imagem_relatorio,
            # 'nome_do_relatorio' : nome_do_relatorio,
            'relatorio_em_tabela' : relatorio_em_tabela,
            'relatorio' : relatorio_linha,
            'relatorio_em_tabela1' : relatorio_em_tabela1,
            'relatorio1' : relatorio_linha1,
            'dados' : dados
        }

    return render(request, 'base/contraste/relatorio_contrast_quest_socio_notas.html', context=context)
    
