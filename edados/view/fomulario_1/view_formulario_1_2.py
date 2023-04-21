from django.shortcuts import render
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from io import BytesIO
import plotly.express as px
import base64
from edados.formularios.formulario_1.formulario_1_2 import Formulario_1
from edados.formularios.filtros.formulario_1_filtros import Formulario_filtros
import numpy as np
from edados.database import bd_formulario_1_2

def formatar(valor):
    return "{:,.2f}".format(valor)

def formulario_2(request):

    questao= 'Q001'
    demografico = 'TP_SEXO'

    if request.method == 'GET':        
        menssagem = ("Formulário 1.")
        menssagem1 = """Este é um formulário que possibilitar a realização
         de uma análise exploratória do ENEM nos períodos de 2018 e 2019."""

        form = Formulario_1()
        form_filtro = Formulario_filtros()
        context = {
            'form' : form,
            'menssagem' : menssagem,
            'menssagem1' : menssagem1,
            'form_filtro' : form_filtro
        }
        return render(request, 'base/formulario_1/quest_formulario_2.html', context=context)
    else:


        # Recebendo fomulario da tela
        form = Formulario_1(request.POST)
        form_filtro = Formulario_filtros(request.POST)

        # Variáveis vindas do Formulario
        filtro_questao = form.data['questao']

        # Formulario de Filtro
        filtro_deficiencia = form_filtro.data['deficiencia']
        filtro_estado_civil = form_filtro.data['estado_civil']
        filtro_cor = form_filtro.data['cor']
        filtro_sexo = form_filtro.data['sexo']
        filtro_ano = form.data['ano']

        Amostra = [demografico, questao]
        Microdado_Amostra = bd_formulario_1_2.buscar_dataframe_no_banco_1_2(
            Amostra, 
            filtro_sexo=filtro_sexo, 
            filtro_questao=filtro_questao, 
            filtro_deficiencia=filtro_deficiencia, 
            filtro_ano=filtro_ano, 
            filtro_cor=filtro_cor, 
            filtro_estado_civil=filtro_estado_civil)


        menssagem = 'Formulário 1'
        relatorio_em_grafico = ''

        relatorio = Microdado_Amostra.to_html(
            max_rows=10, justify='center', 
            classes="""table table-striped table-bordered table-sm
            text-dark"""
            )

        context = {
            'form' : form,
            'form_filtro' : form_filtro,
            'menssagem' : menssagem,
            'relatorio' : relatorio,
            'relatorio_em_grafico' : relatorio_em_grafico
        }

    return render(request, 'base/formulario_1/relatorio_formulario_2.html', context=context)
    