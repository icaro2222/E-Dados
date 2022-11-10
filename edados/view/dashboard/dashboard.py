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
        menssagem = ("Dados Gerais do enem")

        form = DashboardFormulario()
        context = {
            'form' : form,
            'menssagem' : menssagem
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

        context = {
            'form' : form,
            # 'nome_do_relatorio' : nome_do_relatorio,
            'relatorio' : relatorio,
        }

    return render(request, 'dashboard/dashboard.html', context=context)
    
