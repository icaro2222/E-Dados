from django.shortcuts import render
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from io import BytesIO
import pandas as pd
import plotly.express as px
import base64
from edados.formularios.formulario_1.formulario_1_4 import Formulario
from edados.formularios.filtros.formulario_1_filtros import Formulario_filtros
import numpy as np
from edados.database import bd_formulario_1_4

CONTAGEM = 0
CONTAGEMMicrodado_Amostra = 5096019

def formatar(valor):
    return "{:,.2f}".format(valor)

def formatarContagem(valor):
    valor = CONTAGEM
    return "{:,.2f}".format(valor)

def formatarFrequencia(valor):
    print("contage = " + str(CONTAGEM))
    valor =  (valor/CONTAGEM)*100
    return "{:,.4f}%".format(valor)

def formatarFrequenciaSemPorcentagem(valor):
    print("contage = " + str(CONTAGEM))
    valor =  (valor/CONTAGEM)*100
    return "{:,.4f}".format(valor)

def formatarFrequenciaAbsoluta(valor):
    print("contage = " + str(CONTAGEMMicrodado_Amostra))
    valor =  (valor/CONTAGEMMicrodado_Amostra)*100
    return "{:,.6f}%".format(valor)
    
def formulario_4(request):

    global CONTAGEM
    global CONTAGEMMicrodado_Amostra

    questao= 'Q001'
    demografico = 'TP_SEXO'

    if request.method == 'GET':        
        menssagem = ("Formulário 1.4")
        menssagem1 = """Este é um formulário que possibilitar a realização
         de uma análise exploratória do ENEM nos períodos de 2018 e 2019."""

        form = Formulario()
        form_filtro = Formulario_filtros()
        context = {
            'form' : form,
            'menssagem' : menssagem,
            'menssagem1' : menssagem1,
            'form_filtro' : form_filtro
        }
        return render(request, 'base/formulario_1/quest_formulario_4.html', context=context)
    else:


        # Recebendo fomulario da tela
        form = Formulario(request.POST)
        form_filtro = Formulario_filtros(request.POST)

        # Variáveis vindas do Formulario
        filtro_questao = form.data['questao']

        # Formulario de Filtro
        filtro_deficiencia = form_filtro.data['deficiencia']
        filtro_estado_civil = form_filtro.data['estado_civil']
        filtro_cor = form_filtro.data['cor']
        filtro_sexo = form_filtro.data['sexo']
        filtro_ano = form_filtro.data['ano']
        filtro_escola = form_filtro.data['escola']
        filtro_nacionalidade = form_filtro.data['nacionalidade']

        print("teste: "+filtro_escola)

        Amostra = [demografico, questao]
        Microdado_Amostra = bd_formulario_1_4.buscar_dataframe_no_banco(
            Amostra, 
            filtro_sexo=filtro_sexo, 
            filtro_questao=filtro_questao, 
            filtro_deficiencia=filtro_deficiencia, 
            filtro_ano=filtro_ano, 
            filtro_cor=filtro_cor, 
            filtro_estado_civil=filtro_estado_civil, 
            filtro_escola=filtro_escola, 
            filtro_nacionalidade=filtro_nacionalidade)

        Dataframe = Microdado_Amostra.groupby(filtro_questao)['NU_IDADE']
        Dataframe = Dataframe.describe()     
        print(Dataframe.count().count)
        if Dataframe.empty:

            CONTAGEM = 0
            menssagem = """Nenhum dos inscritos com essas características!"""
            context = {
                'form' : form,
                'form_filtro' : form_filtro,
                'menssagem' : menssagem,
                'quantidadeParcial' : CONTAGEM,
                'quantidadeTotal' : CONTAGEMMicrodado_Amostra,
            }
            return render(request, 'base/formulario_1/relatorio_formulario_4.html', context=context)

        figura_com_criador_de_tabela = px.bar(Dataframe)
        figura_com_criador_de_tabela = figura_com_criador_de_tabela.to_html()

        figura_tabela_da_media = px.bar(Dataframe['mean'])
        figura_tabela_da_media = figura_tabela_da_media.to_html()

        rowEvenColor = 'lightgrey'
        rowOddColor = 'white'

        CONTAGEM = Dataframe['count'].sum()

        print("contage = " + str(CONTAGEM))
        print("contage = " + str(CONTAGEMMicrodado_Amostra))

        figura_tabela = go.Figure(data=[go.Table(
                header=dict(
                    values=['Respostas', 'quant alunos', 'porcentagem parcial', 'porcentagem absoluta'],
                    fill_color='royalblue',
                    height=40,
                    line_color='darkslategray',
                    align=['left','center'],
                    font=dict(color='white', size=12)
                ),
                cells=dict(
                    values=[Dataframe.index,
                    Dataframe['count'],
                    Dataframe['count'].apply(formatarFrequencia),
                    Dataframe['count'].apply(formatarFrequenciaAbsoluta)],
                    line_color='darkslategray',
                    fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
                    align = ['left', 'center'],
                    font = dict(color = 'darkslategray', size = 11)
                    ))
                ])
        
        figura_tabela.update_layout(
            title_text = """Quadro de contagem das respostas das questões socioeconômicas.""",
            height = 600,
            margin = {'t':75, 'l':50},
            yaxis = {'domain': [0, .45]},
            xaxis2 = {'anchor': 'y2'},
            xaxis_title="Respota do questionário socioeconômico",
            yaxis_title="Porcentagem",
            yaxis2 = {'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'},
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )

        relatorio_em_tabela = figura_tabela.to_html()
        
        Dataframe1 = Microdado_Amostra.groupby(filtro_questao)['NU_IDADE']
        Dataframe1 = Dataframe1.describe().T
        print(Dataframe1)
        relatorio = Dataframe1.to_html()


        menssagem = 'Formulário 1.4'

        context = {
            'form' : form,
            'form_filtro' : form_filtro,
            'menssagem' : menssagem,
            'quantidadeParcial' : CONTAGEM,
            'quantidadeTotal' : CONTAGEMMicrodado_Amostra,
            'relatorio_em_tabela' : relatorio_em_tabela
        }

    return render(request, 'base/formulario_1/relatorio_formulario_4.html', context=context)
    