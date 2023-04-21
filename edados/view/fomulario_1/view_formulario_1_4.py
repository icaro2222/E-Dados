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
import numpy as np

CONTAGEM = 0
CONTAGEMMicrodado_Amostra = 5096019

def formatar(valor):
    return "{:,.2f}".format(valor)

def formatarContagem(valor):
    valor = CONTAGEM
    return "{:,.2f}".format(valor)

def formatarFrequencia(valor):
    valor =  (valor/CONTAGEM)*100
    return "{:,.4f}%".format(valor)

def formatarFrequenciaSemPorcentagem(valor):
    valor =  (valor/CONTAGEM)*100
    return "{:,.4f}".format(valor)

def formatarFrequenciaAbsoluta(valor):
    valor =  (valor/CONTAGEMMicrodado_Amostra)*100
    return "{:,.6f}%".format(valor)
    
def formulario_4(request):

    global CONTAGEM
    global CONTAGEMMicrodado_Amostra

    questao= 'Q001'
    demografico = 'TP_SEXO'

    if request.method == 'GET':        
        menssagem = ("Formulário 1.4")
        menssagem1 = """Esta é uma tela web que permite realizar o somatório dos alunos que responderam ao ENEM. Esta tela também possui filtros que permitem reduzir o somatório para fins de análise dos microdados. O resultado desse somatório é obtido após a aplicação desses filtros."""

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
        
        if filtro_questao == 'nenhum':
            Dataframe = Microdado_Amostra
            print('--------------------------------------------------------------------')
            print(Dataframe) 
            print('--------------------------------------------------------------------')
            Dataframe = Dataframe.describe().T
        else:
            Dataframe = Microdado_Amostra.groupby(filtro_questao)['NU_IDADE']       
            Dataframe = Dataframe.describe()    

        # print(Dataframe.count().count)

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

        rowEvenColor = 'lightgrey'
        rowOddColor = 'white'

        # print("contage = " + str(CONTAGEM))
        # print("contage = " + str(CONTAGEMMicrodado_Amostra))
        

        if filtro_questao == 'nenhum':
            CONTAGEM  = Dataframe['count']['NU_IDADE']
            figura_tabela = go.Figure(data=[go.Table(
                    header=dict(
                        values=['Quantidade de inscritos', 'Porcentagem parcial', 'Porcentagem absoluta'],
                        fill_color='royalblue',
                        height=40,
                        line_color='darkslategray',
                        align=['left','center'],
                        font=dict(color='white', size=12)
                    ),
                    cells=dict(
                        values=[Dataframe['count'][0:1], 
                                Dataframe['count'].apply(formatarFrequencia)[0:1],
                                Dataframe['count'].apply(formatarFrequenciaAbsoluta)[0:1]],
                        line_color='darkslategray',
                        fill_color = [[rowOddColor,rowEvenColor,rowOddColor]],
                        align = ['left', 'center'],
                        font = dict(color = 'darkslategray', size = 11)
                        ))
                    ])

        else:
            CONTAGEM = Dataframe['count'].sum()
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
        
        if filtro_questao == 'nenhum':
            figura_tabela.update_layout(
                title_text = """Quadro de contagem das respostas das questões socioeconômicas.""",
                height = 500,
                margin = {'t':75, 'l':50},
                yaxis = {'domain': [0, .45]},
                xaxis2 = {'anchor': 'y2'},
                xaxis_title="Respota do questionário socioeconômico",
                yaxis_title="Porcentagem",
                yaxis2 = {'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'},
                legend_title="Legenda",
                annotations=[
                    {
                        'x': 0,
                        'y': 0.7,
                        'xref': "paper",
                        'yref': "paper",
                        'text': """INFORMATIVO:
                                <br>Nesta tela, é possível realizar tanto o somatório dos dados, com a visualização dos percentuais parcial e absoluto, 
                                <br>quanto a análise comparativa entre a filtragem de dados e as respostas do questionário socioeconômico; 
                                <br><br>O percentual parcial: se refere à porcentagem de inscritos que se enquadram nas diferentes respostas do questionário socioeconômico. 
                                <br>Essa análise é feita após a realização da filtragem e o somatório desses percentuais resulta em 100%, 
                                <br>considerando todos os inscritos que passaram pelos filtros selecionados na tela de análise de dados; 
                                <br>Percentual absoluto: é o percentual de inscritos no Enem que foram filtrados em comparação com o total de todos os alunos inscritos, sem qualquer filtro aplicado; 
                                <br><br>Somatório dos inscritos que responderam: Corresponde ao somatório de todos inscritos após a filtragem nos filtros acima; 
                                """,
                        'showarrow': False,
                        'align': 'left',
                        'font': {'family': "Arial", 'size': 13, 'color': "black"}
                    }
                ],
                font=dict(
                    family="Arial",
                    size=12,
                    color="black"
                )
            )
        else:
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
                annotations=[
                    {
                        'x': 0,
                        'y': -0.3,
                        'xref': "paper",
                        'yref': "paper",
                        'text': """INFORMATIVO:
                                <br>Nesta tela, é possível realizar tanto o somatório dos dados, com a visualização dos percentuais parcial e absoluto, 
                                <br>quanto a análise comparativa entre a filtragem de dados e as respostas do questionário socioeconômico; 
                                <br><br>O percentual parcial: se refere à porcentagem de inscritos que se enquadram nas diferentes respostas do questionário socioeconômico. 
                                <br>Essa análise é feita após a realização da filtragem e o somatório desses percentuais resulta em 100%, 
                                <br>considerando todos os inscritos que passaram pelos filtros selecionados na tela de análise de dados; 
                                <br>Percentual absoluto: é o percentual de inscritos no Enem que foram filtrados em comparação com o total de todos os alunos inscritos, sem qualquer filtro aplicado; 
                                <br><br>Somatório dos inscritos que responderam: Corresponde ao somatório de todos inscritos após a filtragem nos filtros acima; 
                                
                                <br><br>A LEGENDA: "A, B, C, D, ..." se referem às opções de resposta do questionário socioeconômico:
                                <br>A: Não informado
                                <br>B: Nenhuma escolaridade
                                <br>C: Ensino fundamental incompleto
                                <br>D: Ensino fundamental completo
                                <br>E: Ensino médio incompleto
                                <br>F: Ensino médio completo
                                <br>G: Ensino superior incompleto
                                <br>H: Ensino superior completo
                                <br>I: Pós-graduação""",
                        'showarrow': False,
                        'align': 'left',
                        'font': {'family': "Arial", 'size': 13, 'color': "black"}
                    }
                ],
                font=dict(
                    family="Arial",
                    size=12,
                    color="black"
                )
            )

        relatorio_em_tabela = figura_tabela.to_html()

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
    