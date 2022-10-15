from cProfile import label
import os
import uuid
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from edados.formularios.form_questao_e_notas import MeuFormulario
from edados.settings import BASE_DIR
import numpy as np

caminho = os.path.join(BASE_DIR, 'dados/Microdado_PROVA_CH_N_Amostra.csv')

def logar(request):
    # return render(request, 'indexTest.html')
    
    return HttpResponse("oi, DEUUUUUUU CERTTTTTOOOOOO. AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

def Grafico_Scatter(request):

    Q = 'TP_SEXO'
    prova = 'NU_NOTA_MT'

    if request.method == 'GET':
        form = MeuFormulario(request.POST)

        if form.is_valid():
            print(form.changed_data)

        form = MeuFormulario()
        context = {
            'form' : form,
            # 'graph' : graph
        }
        return render(request, 'base/quest_socio_notas.html', context=context)
    else:
        form = MeuFormulario(request.POST)

        Q = form.data['questao']
        prova = form.data['nota']

        Microdado_Amostra = pd.read_csv(caminho, sep= ';', encoding = "ISO-8859-1")
            
        Amostra = [prova, Q, 'TP_SEXO']
            
        ChAmostra = Microdado_Amostra.filter(items = Amostra)
            
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
        # plt.switch_backend('AGG')

        width = 0.25         # A largura das barras
        plt.figure(figsize=(0,0))

        r1 = np.arange(len(NU_NOTA_CNCHAmostra))
        r2 = [x + width for x in r1]
        r3 = [x + width for x in r2]


        figura = plt.figure(figsize=(17, 29))
        figura.suptitle('Relatório de Compreenssão em formato de gráfico, \n'+
        'realizando o comparativo entre: Questão Socioeconômica e Desempenho no ENEM')
        
        figura.add_subplot(6,2,1)
        bar_label_mean = plt.bar(dados.index, dados['mean'], color='#BA5ACD', width=width, label="média")
        plt.scatter(dados.index, dados['max'], color='#FA1AFD', label="máximo")
        plt.bar_label(bar_label_mean)
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24, y=1)
        plt.ylabel('Nota Média Global no Exame')
        plt.xlabel('Questão Socioeconômica')

        figura.add_subplot(6,2,2)
        plt.scatter(dados.index, dados['mean'],  c='k', label='Média')
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q)
        plt.ylabel('Nota Média Global no Exame')
        plt.xlabel('Questão Socioeconômica')

        figura.add_subplot(6,2,3)
        plt.bar(dados.index, dados['count'], color='r', width=width, label="quantidade")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q)
        plt.ylabel('Quantidade de Respostas')
        plt.xlabel('Questão Socioeconômica')

        figura.add_subplot(6,2,4)
        plt.plot(dados.index, dados['count'], color='#BA7ACD', label="quantidade")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q)
        plt.ylabel('Quantidade de Respostas')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6,2,5)
        plt.bar(dados.index, dados['25%'], color='y', width=width, label="25%")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q)
        plt.ylabel('Nota ate 25%/ Global no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6,2,6)
        plt.plot(dados.index, dados['25%'], color='b', label="25%")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q)
        plt.ylabel('Nota ate 25%/ Global no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6,2,7)
        plt.bar(dados.index, dados['50%'], color='#EA5ACD', width=width, label="50%")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q)
        plt.ylabel('Nota até 50%/ Global no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6,2,8)
        plt.plot(dados.index, dados['50%'], color='#EA5ACD', label="50%")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q)
        plt.ylabel('Nota até 50%/ Global no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6,2,9)
        plt.bar(dados.index, dados['max'], color='#AA5ACD', width=width, label="máximo")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q)
        plt.ylabel('Nota Máxima no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6, 2, 10)
        plt.scatter(dados.index, dados['max'], color='#AA5ACD',  label="máximo")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q)
        plt.ylabel('Nota Máxima no Exame')
        plt.xlabel('Questão Socioeconômica')

        # plt.show(figura)
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        nome_do_relatorio = 'dados_imagens/' + str(uuid.uuid4()) + '.pdf'
        nome_destino_do_relatorio = str(BASE_DIR) + '/static/' + nome_do_relatorio
        plt.savefig(fname=nome_destino_do_relatorio, format='pdf')
        # plt.savefig(fname='dados/Relatório comparativo entre Questões Socioeconômicas e Desempenho no Enem.pdf' , format='pdf')
        buffer.seek(0)
        image_png = buffer.getvalue()
        image = base64.b64encode(image_png)
        imagem_relatorio = image.decode('utf-8')
        buffer.close()

        if form.is_valid():
            print(form.changed_data)
        else:
            pass

        context = {
            'form' : form,
            'imagem_relatorio' : imagem_relatorio,
            'nome_do_relatorio' : nome_do_relatorio
        }

    return render(request, 'base/relatorio_quest_socio_notas.html', context=context)
    
