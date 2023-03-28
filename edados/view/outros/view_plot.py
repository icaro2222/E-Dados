
import os
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from edados.formularios.form import MeuFormulario
from edados.settings import BASE_DIR
import numpy as np

caminho = os.path.join(BASE_DIR, 'dados/Microdado_Amostra.csv')

def logar(request):
    # return render(request, 'indexTest.html')
    
    return HttpResponse("oi, DEUUUUUUU CERTTTTTOOOOOO. AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

def Grafico_Plot(request):

    Q = 'TP_SEXO'
    prova = 'NU_NOTA_MT'

    if request.method == 'GET':
        form = MeuFormulario(request.POST)

        if form.is_valid():
            print(form.changed_data)
        else:
            pass

        context = {
            'form' : form,
            # 'graph' : graph
        }
        form = MeuFormulario()
        context = {
            'form' : form,
            # 'graph' : graph
        }
        return render(request, 'index1.html', context=context)
    else:
        form = MeuFormulario(request.POST)

        Q = form.data['questao']
        prova = form.data['nota']
        filtro_sexo = form.data['sexo']

        Microdado_Amostra = pd.read_csv(caminho, sep= ';', encoding = "ISO-8859-1")
            
        Amostra = [prova, Q, 'TP_SEXO']
            
        ChAmostra = Microdado_Amostra.filter(items = Amostra)

        if filtro_sexo == 'ambos':
            pass
        elif filtro_sexo == 'm':
            Amostra_Feminina = ChAmostra[ChAmostra['TP_SEXO']=='M']
            Amostra = [prova, Q]
        else:
            Amostra_Masculina = ChAmostra[ChAmostra['TP_SEXO']=='F']
            Amostra = [prova, Q]


        ChAmostra = ChAmostra.sort_values(by=[Q])

        Amostra_Feminina = ChAmostra[ChAmostra['TP_SEXO']=='M']
        Amostra_Masculina = ChAmostra[ChAmostra['TP_SEXO']=='F']

        Amostra_Feminina = Amostra_Feminina.groupby(Q)[prova]
        Amostra_Masculina = Amostra_Masculina.groupby(Q)[prova]
        Amostra_Feminina = Amostra_Feminina.describe()
        Amostra_Masculina = Amostra_Masculina.describe()




        dados = ChAmostra.groupby(Q)[prova]
        dados = dados.describe()

        NU_NOTA_CNCHAmostra = ChAmostra[prova]
        questao = ChAmostra[Q]
        
        # limits = [10, 1000]
        plt.switch_backend('AGG')

        width = 0.25         # A largura das barras
        plt.figure(figsize=(13,5))

        r1 = np.arange(len(NU_NOTA_CNCHAmostra))
        r2 = [x + width for x in r1]
        r3 = [x + width for x in r2]


        figura = plt.figure(figsize=(20, 33))
        figura.suptitle('Questão Socioeconômica VS Desempenho no Exame')
        
        figura.add_subplot(621)
        p1 = plt.bar(dados.index, dados['mean'], color='#BA5ACD', width=width, label="questao")
        
        # plt.xlim(limits)
        plt.title(Q +' , Questão Socioeconômica VS Nota Média no Exame')
        plt.ylabel('Nota Média Global no Exame')
        plt.xlabel('Questão Socioeconômica')

        figura.add_subplot(622)
        p1 = plt.plot(dados.index, dados['mean'], color='#BA5ACD', label="questao")
        
        # plt.xlim(limits)
        plt.title(Q +' , Questão Socioeconômica VS Nota Média no Exame')
        plt.ylabel('Nota Média Global no Exame')
        plt.xlabel('Questão Socioeconômica')

        figura.add_subplot(623)
        p2 = plt.bar(dados.index, dados['count'], color='#BA7ACD', width=width, label="questao")
        plt.legend((p1[0], p2[0]), ('boys', 'girls'))
        
        # plt.xlim(limits)
        plt.title(Q +' , Questão Socioeconômica VS Nota Média no Exame')
        plt.ylabel('Quantidade de Respostas')
        plt.xlabel('Questão Socioeconômica')

        figura.add_subplot(624)
        p2 = plt.plot(dados.index, dados['count'], color='#BA7ACD', label="questao")
        plt.legend((p1[0], p2[0]), ('boys', 'girls'))
        
        # plt.xlim(limits)
        plt.title(Q +' , Questão Socioeconômica VS Nota Média no Exame')
        plt.ylabel('Quantidade de Respostas')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(625)
        plt.bar(dados.index, dados['25%'], color='#B15ACD', width=width, label="questao")
        
        # plt.xlim(limits)
        plt.title(Q +' , Questão Socioeconômica VS Nota Média no Exame')
        plt.ylabel('Nota ate 25%/ Global no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(626)
        plt.plot(dados.index, dados['25%'], color='#B15ACD', label="questao")
        
        # plt.xlim(limits)
        plt.title(Q +' , Questão Socioeconômica VS Nota Média no Exame')
        plt.ylabel('Nota ate 25%/ Global no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(627)
        plt.bar(dados.index, dados['50%'], color='#EA5ACD', width=width, label="questao")
        
        # plt.xlim(limits)
        plt.title(Q +' , Questão Socioeconômica VS Nota Média no Exame')
        plt.ylabel('Nota até 50%/ Global no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(628)
        plt.plot(dados.index, dados['50%'], color='#EA5ACD', label="questao")
        
        # plt.xlim(limits)
        plt.title(Q +' , Questão Socioeconômica VS Nota Média no Exame')
        plt.ylabel('Nota até 50%/ Global no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(629)
        plt.bar(dados.index, dados['max'], color='#AA5ACD', width=width, label="questao")
        
        # plt.xlim(limits)
        plt.title(Q +' , Questão Socioeconômica VS Nota Média no Exame')
        plt.ylabel('Nota Máxima no Exame')
        plt.xlabel('Questão Socioeconômica')


        # figura.add_subplot(6210)
        # plt.bar(dados.index, dados['std'], color='#CA5ACD', width=width, label="questao")
        
        # # plt.xlim(limits)
        # plt.title(Q +' , Questão Socioeconômica VS Nota Média no Exame')
        # plt.ylabel('Nota STD no Exame')
        # plt.xlabel('Questão Socioeconômica')



        plt.show(figura)
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        graph_media = base64.b64encode(image_png)
        graph_media = graph_media.decode('utf-8')
        buffer.close()

        if form.is_valid():
            print(form.changed_data)
        else:
            pass

        context = {
            'form' : form,
            'graph_media' : graph_media,
            'image_png' : image_png,
            # 'graph_25' : graph_25,
            # 'graph_50' : graph_50,
            # 'graph_max' : graph_max
        }

    return render(request, 'grafico_scatter.html', context=context)
    
def Grafico_Plot_Teste(request):

    Q = 'TP_SEXO'
    prova = 'NU_NOTA_MT'

    if request.method == 'GET':
        form = MeuFormulario(request.POST)

        if form.is_valid():
            print(form.changed_data)
        else:
            pass

        context = {
            'form' : form,
            # 'graph' : graph
        }
        form = MeuFormulario()
        context = {
            'form' : form,
            # 'graph' : graph
        }
        return render(request, 'index1.html', context=context)
    else:
        form = MeuFormulario(request.POST)

        Q = form.data['questao']
        prova = form.data['nota']
        filtro_sexo = form.data['sexo']

        Microdado_Amostra = pd.read_csv(caminho, sep= ';', encoding = "ISO-8859-1")
            
        Amostra = [prova, Q, 'TP_SEXO']
            
        ChAmostra = Microdado_Amostra.filter(items = Amostra)

        if filtro_sexo == 'ambos':
            pass
        elif filtro_sexo == 'm':
            Amostra_Feminina = ChAmostra[ChAmostra['TP_SEXO']=='M']
            Amostra = [prova, Q]
        else:
            Amostra_Masculina = ChAmostra[ChAmostra['TP_SEXO']=='F']
            Amostra = [prova, Q]


        ChAmostra = ChAmostra.sort_values(by=[Q])

        Amostra_Feminina = ChAmostra[ChAmostra['TP_SEXO']=='M']
        Amostra_Masculina = ChAmostra[ChAmostra['TP_SEXO']=='F']

        Amostra_Feminina = Amostra_Feminina.groupby(Q)[prova]
        Amostra_Masculina = Amostra_Masculina.groupby(Q)[prova]
        Amostra_Feminina = Amostra_Feminina.describe()
        Amostra_Masculina = Amostra_Masculina.describe()




        dados = ChAmostra.groupby(Q)[prova]
        dados = dados.describe()

        NU_NOTA_CNCHAmostra = ChAmostra[prova]
        questao = ChAmostra[Q]
        
        # limits = [10, 1000]
        plt.switch_backend('AGG')

        width = 0.25         # A largura das barras
        plt.figure(figsize=(13,5))

        r1 = np.arange(len(NU_NOTA_CNCHAmostra))
        r2 = [x + width for x in r1]
        r3 = [x + width for x in r2]


        figura = plt.figure(figsize=(17, 13))
        figura.suptitle('Questão Socioeconômica VS Desempenho no Exame')
        
        figura.add_subplot(111)
        plt.rcdefaults()
        fig, ax = plt.subplots()

        error = np.random.rand(len(dados['count']))
        ax.barh(dados.index, dados['mean'], xerr=error, align='center')

        
        # plt.xlim(limits)
        plt.title(Q +' , Questão Socioeconômica VS Nota Média no Exame')
        plt.ylabel('Nota Média Global no Exame')
        plt.xlabel('Questão Socioeconômica')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        graph_media = base64.b64encode(image_png)
        graph_media = graph_media.decode('utf-8')
        buffer.close()

        if form.is_valid():
            print(form.changed_data)
        else:
            pass

        context = {
            'form' : form,
            'graph_media' : graph_media,
            'image_png' : image_png,
            # 'graph_25' : graph_25,
            # 'graph_50' : graph_50,
            # 'graph_max' : graph_max
        }

    return render(request, 'grafico_scatter.html', context=context)
    
