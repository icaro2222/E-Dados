from email.mime import image
from multiprocessing import context
import os
from unittest.util import _MAX_LENGTH
from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from edados.formularios.forms import MeuFormulario
from edados.settings import BASE_DIR
import numpy as np

caminho = os.path.join(BASE_DIR, 'dados/Microdado_Amostra.csv')

def teste(request):
    form = MeuFormulario()
    context = {
        'form' : form
    }
    return render(request, 'grafico_plot_teste.html', context=context)

def logar(request):
    form = MeuFormulario()
    context = {
        'form' : form
    }
    return render(request, 'index1.html', context=context)

def grafico(request):
    Q = 'TP_SEXO'
    prova = 'NU_NOTA_MT'

    if request.method == 'GET':
        Microdado_Amostra = pd.read_csv(caminho, sep= ';', encoding = "ISO-8859-1")
        Amostra = [prova, Q]
        ChAmostra = Microdado_Amostra.filter(items = Amostra)
        ChAmostra = ChAmostra.sort_values(by=[Q])
        
        NU_NOTA_CNCHAmostra = ChAmostra[prova]
        questao = ChAmostra[Q]
        
        limits = [300, 960]
        plt.switch_backend('AGG')
        plt.figure(figsize = (10,5))
        plt.scatter(NU_NOTA_CNCHAmostra, questao)
        # plt.plot(NU_NOTA_CNCHAmostra, questao)
        plt.xlim(limits)
        plt.title('Ciências da Humanas, Questão Socioeconômica VS Nota da prova ')
        plt.show()

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        graph = base64.b64encode(image_png)
        graph = graph.decode('utf-8')
        buffer.close()
        form = MeuFormulario(request.POST)

        if form.is_valid():
            print(form.changed_data)
        else:
            pass

        context = {
            'form' : form,
            'graph' : graph
        }
        form = MeuFormulario()
        context = {
            'form' : form,
            'graph' : graph
        }
        return render(request, 'index1.html', context=context)
    else:
        form = MeuFormulario(request.POST)
        Q = form.data['questao']
        prova = form.data['nota']
        filtro_sexo = form.data['sexo']
        grafico = form.data['tipo_de_grafico']

        Microdado_Amostra = pd.read_csv(caminho, sep= ';', encoding = "ISO-8859-1")
        
        if Q == 'TP_SEXO':
            Amostra = [prova, Q]
        else:
            Amostra = [prova, Q, 'TP_SEXO']
            
        ChAmostra = Microdado_Amostra.filter(items = Amostra)

        if filtro_sexo == 'ambos':
            pass
        elif filtro_sexo == 'm':
            ChAmostra = ChAmostra[ChAmostra['TP_SEXO']=='M']
            Amostra = [prova, Q]
        else:
            ChAmostra = ChAmostra[ChAmostra['TP_SEXO']=='F']
            Amostra = [prova, Q]

        ChAmostra = ChAmostra.sort_values(by=[Q])
        
        NU_NOTA_CNCHAmostra = ChAmostra[prova]
        questao = ChAmostra[Q]
        
        limits = [0, 1000]
        plt.switch_backend('AGG')
        plt.figure(figsize = (10,5))
        # plt.scatter(questao, NU_NOTA_CNCHAmostra)

        if grafico == 'tabela':
            plt.bar(NU_NOTA_CNCHAmostra, questao)
        elif grafico == 'plot':
            plt.plot(NU_NOTA_CNCHAmostra, questao)
        elif grafico == 'histograma':
            plt.hist(NU_NOTA_CNCHAmostra, questao)
        elif grafico == 'scatter':
            plt.scatter(NU_NOTA_CNCHAmostra, questao)
        else:
            plt.hist2d(NU_NOTA_CNCHAmostra, questao)
        
        plt.xlim(limits)
        plt.title(Q +' , Questão Socioeconômica VS Nota no Exame')
        plt.show()

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        graph = base64.b64encode(image_png)
        graph = graph.decode('utf-8')
        buffer.close()

        if form.is_valid():
            print(form.changed_data)
        else:
            pass

        context = {
            'form' : form,
            'graph' : graph
        }
        return render(request, 'index1.html', context=context)


def index(request):

    Q = 'TP_SEXO'
    prova = 'NU_NOTA_MT'

    if request.method == 'GET':
        Microdado_Amostra = pd.read_csv(caminho, sep= ';', encoding = "ISO-8859-1")
        Amostra = [prova, Q]
        ChAmostra = Microdado_Amostra.filter(items = Amostra)
        ChAmostra = ChAmostra.sort_values(by=[Q])
        
        NU_NOTA_CNCHAmostra = ChAmostra[prova]
        questao = ChAmostra[Q]
        
        limits = [300, 960]
        plt.switch_backend('AGG')
        plt.figure(figsize = (10,5))
        plt.scatter(NU_NOTA_CNCHAmostra, questao)
        # plt.plot(NU_NOTA_CNCHAmostra, questao)
        plt.xlim(limits)
        plt.title('Ciências da Humanas, Questão Socioeconômica VS Nota da prova ')
        plt.show()

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        graph = base64.b64encode(image_png)
        graph = graph.decode('utf-8')
        buffer.close()
        form = MeuFormulario(request.POST)

        if form.is_valid():
            print(form.changed_data)
        else:
            pass

        context = {
            'form' : form,
            'graph' : graph
        }
        form = MeuFormulario()
        context = {
            'form' : form,
            'graph' : graph
        }
        return render(request, 'index1.html', context=context)
    else:
        form = MeuFormulario(request.POST)

        Q = form.data['questao']
        prova = form.data['nota']
        filtro_sexo = form.data['sexo']
        grafico = form.data['tipo_de_grafico']

        Microdado_Amostra = pd.read_csv(caminho, sep= ';', encoding = "ISO-8859-1")
        
        if Q == 'TP_SEXO':
            Amostra = [prova, Q]
        else:
            Amostra = [prova, Q, 'TP_SEXO']
            
        ChAmostra = Microdado_Amostra.filter(items = Amostra)

        if filtro_sexo == 'ambos':
            pass
        elif filtro_sexo == 'm':
            ChAmostra = ChAmostra[ChAmostra['TP_SEXO']=='M']
            Amostra = [prova, Q]
        else:
            ChAmostra = ChAmostra[ChAmostra['TP_SEXO']=='F']
            Amostra = [prova, Q]

        ChAmostra = ChAmostra.sort_values(by=[Q])
        
        NU_NOTA_CNCHAmostra = ChAmostra[prova]
        questao = ChAmostra[Q]
        
        limits = [0, 1000]
        plt.switch_backend('AGG')
        plt.figure(figsize = (13,5))



        width = 0.25         # A largura das barras
        plt.figure(figsize=(13,5))

        r1 = np.arange(len(NU_NOTA_CNCHAmostra))
        r2 = [x + width for x in r1]
        r3 = [x + width for x in r2]

        # plt.scatter(questao, NU_NOTA_CNCHAmostra)

        if grafico == 'tabela':
            plt.bar(NU_NOTA_CNCHAmostra, questao)
        elif grafico == 'plot':
            plt.plot(NU_NOTA_CNCHAmostra, questao)
        elif grafico == 'histograma':
            plt.hist(NU_NOTA_CNCHAmostra, questao)
        elif grafico == 'scatter':
            plt.scatter(NU_NOTA_CNCHAmostra, questao, color='#BA5ACD', label="questao")
        elif grafico == 'bar':
            plt.bar(r1, questao, color='#BA5ACD', width=width, label="questao")
        else:
            plt.hist2d(NU_NOTA_CNCHAmostra, questao)
        
        plt.xlim(limits)
        plt.title(Q +' , Questão Socioeconômica VS Nota no Exame')
        plt.xlabel('Nota no Exame')
        plt.ylabel('Questão Socioeconômica')


        plt.show()
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        graph = base64.b64encode(image_png)
        graph = graph.decode('utf-8')
        buffer.close()

        if form.is_valid():
            print(form.changed_data)
        else:
            pass

        context = {
            'form' : form,
            'graph' : graph
        }
        return render(request, 'index1.html', context=context)
