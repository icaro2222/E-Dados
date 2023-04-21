from django.shortcuts import render
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from io import BytesIO
import plotly.express as px
import base64
from edados.formularios.formulario_1.formulario_1 import Formulario_1
from edados.formularios.filtros.formulario_1_filtros import Formulario_filtros
import numpy as np
from edados.database import bd_formulario_1

def formatar(valor):
    return "{:,.2f}".format(valor)

def formulario_1(request):

    questao= 'Q001'
    demografico = 'TP_SEXO'

    if request.method == 'GET':        
        menssagem = ("Formulário 1.")
        menssagem1 = """Este formulário permite realizar uma análise exploratória que correlaciona os microdados socioeconômicos e demográficos do ENEM nos anos de 2016, 2017, 2018 e 2019. 
        É possível obter resultados em porcentagem, o que possibilita a comparação entre os anos estudados."""

        form = Formulario_1()
        form_filtro = Formulario_filtros()
        context = {
            'form' : form,
            'menssagem' : menssagem,
            'menssagem1' : menssagem1,
            'form_filtro' : form_filtro
        }
        return render(request, 'base/formulario_1/quest_formulario_1.html', context=context)
    else:


        # Recebendo fomulario da tela
        form = Formulario_1(request.POST)
        form_filtro = Formulario_filtros(request.POST)

        # Variáveis vindas do Formulario
        questao= form.data['questao']
        demografico = form.data['demografico']
        filtro_deficiencia = form.data['deficiencia']

        # Formulario de Filtro
        filtro_sexo = form_filtro.data['sexo']
        filtro_ano = form_filtro.data['ano']

        Amostra = [demografico, questao]
        if demografico != 'TP_SEXO' and filtro_sexo != 'todos':
            Amostra.append('TP_SEXO')
            Microdado_Amostra = bd_formulario_1.buscar_dataframe_no_banco(Amostra, filtro_sexo=filtro_sexo, filtro_deficiencia=filtro_deficiencia, filtro_ano=filtro_ano)
        else:
            Microdado_Amostra = bd_formulario_1.buscar_dataframe_no_banco(Amostra, filtro_deficiencia=filtro_deficiencia, filtro_ano=filtro_ano)

        menssagem = 'Formulário 1'
        relatorio_em_grafico = ''

        if(demografico == 'TP_SEXO'):

            if(filtro_sexo == 'todos'):
                vetor = demografico_sexo(Microdado_Amostra, demografico, questao)
                relatorio = vetor[0]
                relatorio_em_grafico = vetor[1]
            else:
                vetor = demografico_sexo_unilateral(Microdado_Amostra, demografico, questao, filtro_sexo)
                relatorio = vetor[0]

        elif(demografico == 'TP_ESTADO_CIVIL'):
            vetor = demografico_estado_civil(Microdado_Amostra, demografico, questao, filtro_ano)
            relatorio = vetor[0]
            relatorio_em_grafico = vetor[1]

        elif(demografico == 'TP_COR_RACA'):
            vetor = demografico_raca(Microdado_Amostra, demografico, questao)
            relatorio = vetor[0]

        elif(demografico == 'TP_NACIONALIDADE'):
            vetor = demografico_nascionalidade(Microdado_Amostra, demografico, questao)
            relatorio = vetor[0]

        elif(demografico == 'TP_ESCOLA'):
            vetor = demografico_escolaridade(Microdado_Amostra, demografico, questao)
            relatorio = vetor[0]

        elif(demografico == 'TP_ENSINO'):
            vetor = demografico_instituicao_aonde_conclui_ensino_medio(Microdado_Amostra, demografico, questao)
            relatorio = vetor[0]

        elif(demografico == 'TP_ANO_CONCLUIU'):
            vetor = demografico_ano_de_conclusao(Microdado_Amostra, demografico, questao, filtro_ano=filtro_ano)
            relatorio = vetor[0]

        context = {
            'form' : form,
            'form_filtro' : form_filtro,
            'menssagem' : menssagem,
            'relatorio' : relatorio,
            'relatorio_em_grafico' : relatorio_em_grafico
        }

    return render(request, 'base/formulario_1/relatorio_formulario_1.html', context=context)
    
def demografico_sexo(Microdado_Amostra, demografico, questao):

        DataFrame = Microdado_Amostra.sort_values(by=[questao])
        DataFrame = DataFrame.groupby([demografico, questao])
        DataFrame = DataFrame[demografico].count()
            
        # rotacionar 
        DataFrame = DataFrame.unstack()
        DataFrame_para_criar_a_grafico = DataFrame

        lista_dos_index = DataFrame.index.to_list()

        # desrotacionar 
        DataFrame = DataFrame.stack()

        fig = go.Figure()

        for index in lista_dos_index:
            if index=='M':
                nome = 'masculíno'
            else:
                nome = 'feminíno'
            fig.add_bar(
                y=DataFrame[index],
                x=DataFrame[index].index,
                text=DataFrame[index],
                name = nome,
            )
            
        fig.update_layout(
            title_text = 'Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
            height = 700,
            margin=dict(l=50, r=50, b=300, t=50),
            xaxis_title="Resposta do questionário socioeconômico",
            yaxis_title="Quantidade",
            legend_title="Legenda",
            annotations=[
                {
                    'x': 0,
                    'y': -0.8,
                    'xref': "paper",
                    'yref': "paper",
                    'text': """A legenda: "A, B, C, D, ..." se referem às opções de resposta do questionário socioeconômico:
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

        relatorio_em_grafico = px.bar(
            DataFrame_para_criar_a_grafico, 
            barmode='group',
            text_auto=True)

        relatorio_em_grafico.update_layout(
            title_text='Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
            height=700,
            margin=dict(l=50, r=50, b=300, t=50),
            xaxis_title="Resposta do questionário socioeconômico por sexo.",
            yaxis_title="Quantidade",
            legend_title="Legenda",
            annotations=[
                {
                    'x': 0,
                    'y': -0.8,
                    'xref': "paper",
                    'yref': "paper",
                    'text': """A Legenda: "F e M" se referem ao sexo do inscrito: <br>F: Significa que se refere aos inscritos que se declararam do sexo feminino.
                            <br>M: Significa que se refere aos inscritos que se declararam do sexo masculino.
                            <br>--
                            <br>A legenda: "A, B, C, D, ..." se referem às opções de resposta do questionário socioeconômico:
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
            font={'family': "Arial", 'size': 12, 'color': "black"}
        )

        relatorio_em_grafico = relatorio_em_grafico.to_html()

        relatorio = fig.to_html()

        return [ relatorio, relatorio_em_grafico]

def demografico_sexo_unilateral(Microdado_Amostra, demografico, questao, filtro_sexo):

        DataFrame = Microdado_Amostra.sort_values(by=[questao])
        DataFrame = DataFrame.groupby([demografico, questao])
        DataFrame = DataFrame[demografico].count()
            
        # rotacionar 
        DataFrame = DataFrame.unstack()

        lista_dos_index = DataFrame.index.to_list()

        # desrotacionar 
        DataFrame = DataFrame.stack()

        fig = go.Figure()
        
        if(DataFrame.count() > 0):
            if filtro_sexo=='M':
                nome = 'masculíno'
                fig.add_bar(
                    y=DataFrame[filtro_sexo],
                    x=DataFrame[filtro_sexo].index,
                    text=DataFrame[filtro_sexo],
                    name = nome,
                )
            else:
                nome = 'feminíno'
                fig.add_bar(
                    y=DataFrame[filtro_sexo],
                    x=DataFrame[filtro_sexo].index,
                    text=DataFrame[filtro_sexo],
                    name = nome,
                )
            
        fig.update_layout(
            title_text = 'Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
            height=700,
            margin=dict(l=50, r=50, b=300, t=50),
            xaxis_title="Resposta do questionário socioeconômico.",
            yaxis_title="Quantidade",
            legend_title="Legenda",
            annotations=[
                {
                    'x': 0,
                    'y': -0.7,
                    'xref': "paper",
                    'yref': "paper",
                    'text': """A legenda: "A, B, C, D, ..." se referem às opções de resposta do questionário socioeconômico:
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
        relatorio = fig.to_html()

        return [relatorio]
 
def demografico_estado_civil(Microdado_Amostra, demografico, questao, filtro_ano):

        DataFrame = Microdado_Amostra.sort_values(by=[questao])
        DataFrame = DataFrame.groupby([demografico, questao])
        DataFrame = DataFrame[demografico].count()

        # rotacionar 
        DataFrame = DataFrame.unstack()
        DataFrame_para_criar_a_grafico = DataFrame

        lista_dos_index = DataFrame.index.to_list()

        # desrotacionar 
        DataFrame = DataFrame.stack()

        fig = go.Figure()

        for index in lista_dos_index:
            print(filtro_ano)
            if filtro_ano=='2019':
                if (index=='0' or index==0):
                    nome = 'Não informou'
                elif (index=='1' or index==1):
                    nome = 'Solteiro(a)'
                elif (index=='2' or index==2):
                    nome = 'Casado(a)'
                elif (index=='3' or index==3):
                    nome = 'Divorciado(a)'
                else:
                    nome = 'Viúvo(a)'
            else:
                if (index=='0' or index==0):
                    nome = 'Solteiro(a)'
                elif (index=='1' or index==1):
                    nome = 'Casado(a)'
                elif (index=='2' or index==2):
                    nome = 'Divorciado(a)'
                elif (index=='3' or index==3):
                    nome = 'Viúvo(a)'
                else:
                    nome = 'Não informou'

            fig.add_bar(
                y=DataFrame[index],
                x=DataFrame[index].index,
                text=DataFrame[index],
                name = nome,
            )
              
        fig.update_layout(
            title_text = 'Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
            height = 700,
            margin=dict(l=50, r=50, b=300, t=50),
            xaxis_title="Resposta do questionário socioeconômico",
            yaxis_title="Quantidade",
            legend_title="Legenda",
            annotations=[
                {
                    'x': 0,
                    'y': -0.7,
                    'xref': "paper",
                    'yref': "paper",
                    'text': """A legenda: "A, B, C, D, ..." se referem às opções de resposta do questionário socioeconômico:
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
        relatorio_em_grafico = px.bar(DataFrame_para_criar_a_grafico, barmode='group')

        relatorio_em_grafico.update_layout(
            title_text = 'Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
            height = 700,
            margin=dict(l=50, r=50, b=300, t=50),
            xaxis_title="Resposta do questionário socioeconômico",
            yaxis_title="Quantidade",
            legend_title="Legenda",
            annotations=[
                {
                    'x': 0,
                    'y': -0.7,
                    'xref': "paper",
                    'yref': "paper",
                    'text': """A legenda: "A, B, C, D, ..." se referem às opções de resposta do questionário socioeconômico:
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
        relatorio_em_grafico = relatorio_em_grafico.to_html()
        
        relatorio = fig.to_html()

        return [relatorio, relatorio_em_grafico]

def demografico_raca(Microdado_Amostra, demografico, questao):

        DataFrame = Microdado_Amostra.sort_values(by=[questao])
        DataFrame = DataFrame.groupby([demografico, questao])
        DataFrame = DataFrame[demografico].count()

        # DataFrame = Microdado_Amostra.sort_values(by=questao)
        # DataFrame = DataFrame.groupby([demografico, questao])[demografico].count()

        # rotacionar 
        DataFrame = DataFrame.unstack()

        # Pegando lista de index pra usá-los posteriomente.
        lista_dos_index = DataFrame.index.to_list()

        # desrotacionar 
        DataFrame = DataFrame.stack()

        fig = go.Figure()

        for index in lista_dos_index:
            
            if (index=='0' or index==0):
                nome = 'Não informou'
            elif (index=='1' or index==1):
                nome = 'Branca'
            elif (index=='2' or index==2):
                nome = 'Preta'
            elif (index=='3' or index==3):
                nome = 'Parda'
            elif (index=='4' or index==4):
                nome = 'Amarela'
            else:
                nome = 'Indígena'
            fig.add_bar(
                y=DataFrame[index],
                x=DataFrame[index].index,
                text=DataFrame[index],
                name = nome,
            )
              
        fig.update_layout(
            title_text = 'Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
            height = 700,
            margin=dict(l=50, r=50, b=300, t=50),
            xaxis_title="Resposta do questionário socioeconômico",
            yaxis_title="Quantidade",
            legend_title="Legenda",
            annotations=[
                {
                    'x': 0,
                    'y': -0.7,
                    'xref': "paper",
                    'yref': "paper",
                    'text': """A legenda: "A, B, C, D, ..." se referem às opções de resposta do questionário socioeconômico:
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

        relatorio = fig.to_html()

        return [relatorio]

def demografico_nascionalidade(Microdado_Amostra, demografico, questao):

        DataFrame = Microdado_Amostra.sort_values(by=[questao])
        DataFrame = DataFrame.groupby([demografico, questao])
        DataFrame = DataFrame[demografico].count()

        # rotacionar 
        DataFrame = DataFrame.unstack()

        lista_dos_index = DataFrame.index.to_list()
        print(lista_dos_index)

        # desrotacionar 
        DataFrame = DataFrame.stack()

        fig = go.Figure()

        for index in lista_dos_index:
            print(index)
            if (index=='0' or index==0):
                nome = 'Não informou'
            elif (index=='1' or index==1):
                nome = 'Brasileiro(a)'
            elif (index=='2' or index==2):
                nome = 'Naturalizado(a)'
            elif (index=='3' or index==3):
                nome = 'Estrangeiro(a)'
            else:
                nome = 'Brasileiro(a) Nato(a), nascido(a) no exterior'
            fig.add_bar(
                y=DataFrame[index],
                x=DataFrame[index].index,
                text=DataFrame[index],
                name = nome,
            )
            
        fig.update_layout(
            title_text = 'Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
            height = 700,
            margin=dict(l=50, r=50, b=300, t=50),
            xaxis_title="Resposta do questionário socioeconômico",
            yaxis_title="Quantidade",
            legend_title="Legenda",
            annotations=[
                {
                    'x': 0,
                    'y': -0.7,
                    'xref': "paper",
                    'yref': "paper",
                    'text': """A legenda: "A, B, C, D, ..." se referem às opções de resposta do questionário socioeconômico:
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
            ),
            # margin = {'t':75, 'l':50},
            # yaxis = {'domain': [0, .45]},
            # xaxis2 = {'anchor': 'y2'},
            # yaxis2 = {'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'}
        )

        relatorio = fig.to_html()

        return [relatorio]

def demografico_escolaridade(Microdado_Amostra, demografico, questao):

        DataFrame = Microdado_Amostra.sort_values(by=[questao])
        DataFrame = DataFrame.groupby([demografico, questao])
        DataFrame = DataFrame[demografico].count()

        # rotacionar 
        DataFrame = DataFrame.unstack()

        lista_dos_index = DataFrame.index.to_list()
        print(lista_dos_index)

        # desrotacionar 
        DataFrame = DataFrame.stack()

        fig = go.Figure()

        for index in lista_dos_index:
            print(index)
            if (index=='0' or index==0):
                nome = 'Não informou'
            elif (index=='1' or index==1):
                nome = 'Pública'
            elif (index=='2' or index==2):
                nome = 'Privada'
            else:
                nome = 'Exterior'
            fig.add_bar(
                y=DataFrame[index],
                x=DataFrame[index].index,
                text=DataFrame[index],
                name = nome,
            )
            
        fig.update_layout(
            title_text = 'Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
            height = 700,
            margin=dict(l=50, r=50, b=300, t=50),
            xaxis_title="Resposta do questionário socioeconômico",
            yaxis_title="Quantidade",
            legend_title="Legenda",
            annotations=[
                {
                    'x': 0,
                    'y': -0.7,
                    'xref': "paper",
                    'yref': "paper",
                    'text': """A legenda: "A, B, C, D, ..." se referem às opções de resposta do questionário socioeconômico:
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

        relatorio = fig.to_html()

        return [relatorio]

def demografico_conclusao_ensino_medio(Microdado_Amostra, demografico, questao):

        DataFrame = Microdado_Amostra.sort_values(by=[questao])
        DataFrame = DataFrame.groupby([demografico, questao])
        DataFrame = DataFrame[demografico].count()

        # rotacionar 
        DataFrame = DataFrame.unstack()

        lista_dos_index = DataFrame.index.to_list()
        print(lista_dos_index)

        # desrotacionar 
        DataFrame = DataFrame.stack()

        fig = go.Figure()

        for index in lista_dos_index:
            print('INDEX= '+index)
            if (index=='0' or index==0):
                nome = 'Não informou'
            elif (index=='1' or index==1):
                nome = 'Pública'
            elif (index=='2' or index==2):
                nome = 'Privada'
            else:
                nome = 'Exterior'
            fig.add_bar(
                y=DataFrame[index],
                x=DataFrame[index].index,
                text=DataFrame[index],
                name = nome,
            )
            
        fig.update_layout(
            title_text = 'Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
            height = 700,
            margin=dict(l=50, r=50, b=300, t=50),
            xaxis_title="Resposta do questionário socioeconômico",
            yaxis_title="Quantidade",
            legend_title="Legenda",
            annotations=[
                {
                    'x': 0,
                    'y': -0.7,
                    'xref': "paper",
                    'yref': "paper",
                    'text': """A legenda: "A, B, C, D, ..." se referem às opções de resposta do questionário socioeconômico:
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

        relatorio = fig.to_html()

        return [relatorio]

def demografico_ano_de_conclusao(Microdado_Amostra, demografico, questao, filtro_ano):

        DataFrame = Microdado_Amostra.sort_values(by=[questao])
        DataFrame = DataFrame.groupby([demografico, questao])
        DataFrame = DataFrame[demografico].count()

        # rotacionar 
        DataFrame = DataFrame.unstack()

        lista_dos_index = DataFrame.index.to_list()
        print(lista_dos_index)

        # desrotacionar 
        DataFrame = DataFrame.stack()

        fig = go.Figure()

        for index in lista_dos_index:
            
            if filtro_ano=='2019':
                print(2019)
                if (index=='0' or index==0):
                    nome = 'Não informou'
                elif (index=='1' or index==1):
                    nome = '2018'
                elif (index=='2' or index==2):
                    nome = '2017'
                elif (index=='3' or index==3):
                    nome = '2016'
                elif (index=='4' or index==4):
                    nome = '2015'
                elif (index=='5' or index==5):
                    nome = '2014'
                elif (index=='6' or index==6):
                    nome = '2013'
                elif (index=='7' or index==7):
                    nome = '2012'
                elif (index=='8' or index==8):
                    nome = '2011'
                elif (index=='9' or index==9):
                    nome = '2010'
                elif (index=='10' or index==10):
                    nome = '2009'
                elif (index=='11' or index==11):
                    nome = '2008'
                elif (index=='12' or index==12):
                    nome = '2007'
                else:
                    nome = 'Antes de 2007'
            elif filtro_ano=='2018':
                print(2018)
                if (index=='0' or index==0):
                    nome = 'Não informou'
                elif (index=='1' or index==1):
                    nome = '2017'
                elif (index=='2' or index==2):
                    nome = '2016'
                elif (index=='3' or index==3):
                    nome = '2015'
                elif (index=='4' or index==4):
                    nome = '2014'
                elif (index=='5' or index==5):
                    nome = '2013'
                elif (index=='6' or index==6):
                    nome = '2012'
                elif (index=='7' or index==7):
                    nome = '2011'
                elif (index=='8' or index==8):
                    nome = '2010'
                elif (index=='9' or index==9):
                    nome = '2009'
                elif (index=='10' or index==10):
                    nome = '2008'
                elif (index=='11' or index==11):
                    nome = '2007'
                else:
                    nome = 'Antes de 2007'

            fig.add_bar(
                y=DataFrame[index],
                x=DataFrame[index].index,
                text=DataFrame[index],
                name = nome,

            )
            
        fig.update_layout(
            title_text = 'Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
            height = 700,
            margin=dict(l=50, r=50, b=300, t=50),
            xaxis_title="Resposta do questionário socioeconômico",
            yaxis_title="Quantidade",
            legend_title="Legenda",
            annotations=[
                {
                    'x': 0,
                    'y': -0.7,
                    'xref': "paper",
                    'yref': "paper",
                    'text': """A legenda: "A, B, C, D, ..." se referem às opções de resposta do questionário socioeconômico:
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

        relatorio = fig.to_html()

        return [relatorio]

def demografico_instituicao_aonde_conclui_ensino_medio(Microdado_Amostra, demografico, questao):

        DataFrame = Microdado_Amostra.sort_values(by=[questao])
        DataFrame = DataFrame.groupby([demografico, questao])
        DataFrame = DataFrame[demografico].count()

        # rotacionar 
        DataFrame = DataFrame.unstack()

        lista_dos_index = DataFrame.index.to_list()
        print(lista_dos_index)

        # desrotacionar 
        DataFrame = DataFrame.stack()

        fig = go.Figure()

        for index in lista_dos_index:
            print(index)
            if (index=='0' or index==0):
                nome = 'Não informou'
            elif (index=='1' or index==1):
                nome = 'Pública'
            elif (index=='2' or index==2):
                nome = 'Privada'
            else:
                nome = 'Exterior'
            fig.add_bar(
                y=DataFrame[index],
                x=DataFrame[index].index,
                text=DataFrame[index],
                name = nome,

            )
            
        fig.update_layout(
            title_text = 'Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
            height = 700,
            margin=dict(l=50, r=50, b=300, t=50),
            xaxis_title="Resposta do questionário socioeconômico",
            yaxis_title="Desempenho",
            legend_title="Legenda",
            annotations=[
                {
                    'x': 0,
                    'y': -0.7,
                    'xref': "paper",
                    'yref': "paper",
                    'text': """A legenda: "A, B, C, D, ..." se referem às opções de resposta do questionário socioeconômico:
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

        relatorio = fig.to_html()

        return [relatorio]