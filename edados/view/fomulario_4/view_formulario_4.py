from django.shortcuts import render
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from io import BytesIO
import pandas as pd
from edados.formularios.formulario_4.formulario_4 import Formulario_4
from edados.formularios.filtros.formulario_1_filtros import Formulario_filtros
from edados.formularios.filtros.filtros_ano import Formulario_filtro_ano
import numpy as np
from django.utils.html import format_html_join
from edados.database import bd_formulario_4

def formatar(valor):
    return "{:,.2f}".format(valor)

def formulario_4(request):

    if request.method == 'GET':        
        
        menssagem = ("Mapa de Distribuição de Alunos")
        menssagem_informativa = """O formulário web em questão disponibiliza uma ferramenta de análise da densidade demográfica dos inscritos no ENEM utilizando os microdados. Através dessa plataforma, é possível realizar análises comparativas entre diferentes regiões demográficas e identificar padrões que possam estar relacionados aos dados socioeconômicos dos inscritos.

        Com o objetivo de oferecer uma experiência de usuário intuitiva e acessível, a tela do site apresenta de forma clara e organizada as diferentes opções de análise disponíveis. É possível selecionar diferentes regiões demográficas e        comparar a densidade de inscritos em cada uma delas, além de visualizar gráficos e tabelas com informações detalhadas         sobre os dados socioeconômicos dos inscritos em cada região.

        Além disso, o site oferece opções avançadas de filtragem e segmentação de dados, permitindo que o usuário realize         análises mais específicas e detalhadas de acordo com suas necessidades. Por exemplo, é possível filtrar os dados por         gênero, idade, escolaridade e outras variáveis socioeconômicas para identificar padrões mais específicos em cada         região demográfica.

        A análise da densidade demográfica dos inscritos no ENEM é uma ferramenta valiosa para a compreensão das dinâmicas         socioeconômicas do país. Com base nesses dados, é possível identificar desigualdades regionais e propor políticas     públicas mais efetivas para a melhoria do acesso à educação e para a promoção da igualdade social.         O site web em questão representa uma importante contribuição nesse sentido, oferecendo uma plataforma de análise de dados     demográficos acessível e de fácil utilização para pesquisadores, estudantes e outros interessados em compreender melhor a realidade socioeconômica do Brasil."""
        menssagem_informativa = menssagem_informativa.split('\n')
        menssagem_informativa = format_html_join('\n', '<p>{}</p>', ((line,) for line in menssagem_informativa))


        form = Formulario_filtro_ano()
        form_filtro = Formulario_filtros()

        context = {
            'form' : form,
            'menssagem' : menssagem,
            'menssagem_informativa' : menssagem_informativa,
            'form_filtro' : form_filtro
        }
        return render(request, 'base/formulario_4/quest_formulario_4.html', context=context)
    else:


        # Recebendo fomulario da tela
        form = Formulario_filtro_ano()
        form_filtro = Formulario_filtros()


        # Formulario de Filtro
        menssagem = ("Mapa de Distribuição de Alunos")
        menssagem_informativa = """O tela web em questão disponibiliza uma ferramenta de análise da densidade demográfica 
        dos inscritos no ENEM utilizando os microdados."""

        df = pd.read_csv('/home/icaro/Documentos/e-dados/edados/view/fomulario_4/municipios_brasileiros.csv')

        trace = go.Scattergeo(
            locationmode = 'ISO-3',
            lon = df['longitude'],
            lat = df['latitude'],
            text = df['nome_municipio'] + '- População: ' + df['codigo_ibge'].astype(str),
            marker = dict(
                size = df['codigo_ibge']/20000,
                color = '#e74c3c',
                line = {'width': 0.5, 
                        'color': '#2c3e50'},
                sizemode = 'area')
        )
        data = [trace]
        layout = go.Layout(
            height=700,
            margin=dict(l=0, r=0, b=10, t=50),
            title = '<b>Inscritos do Enem de 2019</b>',
            titlefont = {'family': 'Arial', 'size': 24},
            geo =  {'scope': 'south america',
                    'projection': {'type': 'mercator'},
                    'showland': True,
                    'landcolor': '#2ecc71',
                    'showlakes': True,
                    'lakecolor': '#3498db',
                    'subunitwidth': 1,
                    'subunitcolor': "rgb(255, 255, 255)"
                }
        )
        fig = go.Figure(data=data, layout=layout)

        relatorio = fig.to_html()

        context = {
            'form' : form,
            'form_filtro' : form_filtro,
            'menssagem' : menssagem,
            'menssagem_informativa' : menssagem_informativa,
            'relatorio' : relatorio
        }

    return render(request, 'base/formulario_4/relatorio_formulario_4.html', context=context)
    