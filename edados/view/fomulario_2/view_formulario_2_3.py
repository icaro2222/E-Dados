from django.shortcuts import render
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from io import BytesIO
import pandas as pd
import plotly.express as px
import base64
from edados.formularios.formulario_2.formulario_2_1 import Formulario
from edados.formularios.filtros.formulario_1_filtros import Formulario_filtros
import numpy as np
from edados.database import bd_formulario_1_3

def formatar(valor):
    return "{:,.2f}".format(valor)

def formulario_3(request):

    questao= 'Q001'
    demografico = 'TP_SEXO'

    if request.method == 'GET':        
        menssagem = ("Formulário 1.3")
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
        return render(request, 'base/formulario_2/quest_formulario_3.html', context=context)
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
        Microdado_Amostra = bd_formulario_1_3.buscar_dataframe_no_banco(
            Amostra, 
            filtro_sexo=filtro_sexo, 
            filtro_questao=filtro_questao, 
            filtro_deficiencia=filtro_deficiencia, 
            filtro_ano=filtro_ano, 
            filtro_cor=filtro_cor, 
            filtro_estado_civil=filtro_estado_civil, 
            filtro_escola=filtro_escola, 
            filtro_nacionalidade=filtro_nacionalidade)


        menssagem = 'Formulário 1.3'
        relatorio_em_grafico = ''

        Dataframe = Microdado_Amostra.sort_values(by=[filtro_questao])
        # Dataframe.reset_index()
        # pd.set_option("max_colwidth", 2)
        pd.set_eng_float_format(accuracy=2, use_eng_prefix=True)

        Dataframe = Dataframe.groupby([filtro_questao, "TP_SEXO", "TP_COR_RACA"]).agg({
            "TP_SEXO":("count"),
            "TP_COR_RACA":("count"),
            "NU_IDADE":("count", "min", "mean", "max"),
            "NU_NOTA_CN":("count", "min", "mean", "max"), 
            "NU_NOTA_CH":("count", "min", "mean", "max"),
            "NU_NOTA_LC":("count", "min", "mean", "max"),
            "NU_NOTA_MT":("count", "min", "mean", "max")
        }).T
        # DataFrame = DataFrame.groupby([filtro_questao])
        # Dataframe = Dataframe.describe().T
        # Dataframe = Dataframe['NU_IDADE']

        # rotacionar 
        # Dataframe = Dataframe.unstack()

        # lista_dos_index = Dataframe['A']
        # print(lista_dos_index)

        # desrotacionar 
        # Dataframe = Dataframe.stack()


        # pd.set_option('display.max_colwidth',4)
        # teste = Dataframe['A'].apply(formatar)
        
        print(Dataframe) 
        
        Dataframe = Dataframe.to_html()   

        relatorio = Microdado_Amostra.to_html(
            max_rows=10, justify='center', 
            classes="""table table-striped table-bordered table-sm
            text-dark"""
            )

        context = {
            'form' : form,
            'form_filtro' : form_filtro,
            'menssagem' : menssagem,
            'relatorio' : Dataframe,
            'relatorio_em_grafico' : relatorio_em_grafico
        }

    return render(request, 'base/formulario_2/relatorio_formulario_3.html', context=context)
    