import os
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

def Dashboard(request):

    if request.method == 'GET':        
        menssagem1 = ("Dados Gerais do enem")

        menssagem = """Está é uma plataforma online, visando te possibilitar 
                        uma análise de forma simples e eficiente, 
                        de maneira que você não necessite gastar horas."""
        form = DashboardFormulario()
        context = {
            'form' : form,
            'menssagem' : menssagem,
            'menssagem1' : menssagem1
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

        menssagem = """Está é uma ploataforma online, com o objetivo de te possibilitar 
                        uma análise de forma simples e eficiênte, 
                        de maneira que você não necessite gastar horas."""

        context = {
            'form' : form,
            'menssagem' : menssagem,
            # 'nome_do_relatorio' : nome_do_relatorio,
            'relatorio' : relatorio,
        }

    return render(request, 'dashboard/dashboard.html', context=context)
    
