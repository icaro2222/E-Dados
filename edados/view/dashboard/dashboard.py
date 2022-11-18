import os
from django.contrib.auth.decorators import login_required
from typing import Sized
import plotly.graph_objects as go
from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib as mpl
from edados.formularios.dashboard.formulario_dashboard import DashboardFormulario
import numpy as np
from edados.database import bd_quest_socio_notas_deficiencia, conect_db


def formatar(valor):
    return "{:,.2f}".format(valor)


@login_required
def Dashboard(request):

    if request.method == 'GET':

        menssagem1 = "Dados Gerais do enem"
        menssagem = """Esta é uma plataforma online, que visa te possibilitar, 
        realizar uma análise de forma simples, eficiente, 
        e no menor período possível."""

        form = DashboardFormulario()

        fig = go.Figure(data=[go.Table(
            header=dict(values=['Ano', 'Quantidade de alunos']),
            cells=dict(values=[['2021', '2020', '2019', '2018', '2017', '2016'],
                               [5335345, 2537645, 3433078, 5775045, 6475045, 4098045]
                               ]))
        ])

        figura = go.Figure()

        figura.add_bar(x=['2021', '2020', '2019', '2018', '2017', '2016'],
                    y=[5335345, 2537645, 3433078, 5775045, 6475045, 4098045])
        figura.add_scatter(x=['2021', '2020', '2019', '2018', '2017', '2016'],
                    y=[5335345, 2537645, 3433078, 5775045, 6475045, 4098045])


        figura.update_layout(
            title_text = 'Quantidade de inscrições no Enem, por ano.',
            height = 400,
            xaxis_title="Ano",
            yaxis_title="Quantidade de Inscritos",
            legend_title="Legenda",
            font=dict(
                family="Courier New, monospace",
                size=12,
                color="black"
            )
        )

        fig.update_layout(
            title_text = 'Tabela.',
            height = 400,
            width=500,
            xaxis_title="Ano",
            yaxis_title="Quantidade de Inscritos",
            legend_title="Legenda",
            font=dict(
                family="Courier New, monospace",
                size=12,
                color="black"
            )
        )

        relatorio_em_tabela = fig.to_html()
        relatorio = figura.to_html()

        context = {
            'form': form,
            'menssagem': menssagem,
            'menssagem1': menssagem1,
            'relatorio': relatorio,
            'relatorio_em_tabela': relatorio_em_tabela
        }
        return render(request, 'dashboard/dashboard.html', context=context)
    else:

        # Recebendo fomulario da tela
        form = DashboardFormulario(request.POST)

        # Variáveis vindas do Formulario
        ano = form.data['ano']

        # if(ano != 'todos'):
        #     Microdado_Amostra = bd_quest_socio_notas_deficiencia.buscar_dataframe_no_banco(ano)
        # else:
        #     Microdado_Amostra = bd_quest_socio_notas_deficiencia.buscar_dataframe_no_banco(ano)

        relatorio = 1800

        menssagem1 = "Dados Gerais do enem"
        menssagem = """Esta é uma plataforma online, que visa te possibilitar, 
        realizar uma análise de forma simples, eficiente, 
        e no menor período possível."""

        fig = go.Figure(data=[go.Table(
            header=dict(values=['Ano', 'Quantidade de alunos']),
            cells=dict(values=[['2016', '2017', '2018', '2019'],
                               [5335345, 2537645, 3433078, 5775045]
                               ]))
        ])

        relatorio_em_tabela = fig.to_html()

        context = {
            'form': form,
            'menssagem': menssagem,
            'menssagem1': menssagem1,
            'relatorio_em_tabela': relatorio_em_tabela,
            'relatorio': relatorio,
        }

    return render(request, 'dashboard/dashboard.html', context=context)
