import os
from typing import Sized
import uuid
from django.shortcuts import render
import plotly.graph_objects as go 
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import matplotlib as mpl
import plotly.express as px
import base64
from edados.formularios.form import MeuFormulario
from edados.settings import BASE_DIR
import numpy as np
from edados.database import bd_quest_socio_notas

caminho = os.path.join(BASE_DIR, 'dados/Microdado_Amostra.csv')

def formatar(valor):
    return "{:,.2f}".format(valor)
    
def Quest_Soc_Notas_Sexo(request):

    Q = 'TP_SEXO'
    prova = 'NU_NOTA_MT'

    if request.method == 'GET':
        form = MeuFormulario(request.POST)

        if form.is_valid():
            print(form.changed_data)

        menssagem = ("Nesta tela você irá poder realizar uma análise comparativa entre as " +
        "questões socioeconômicas e o desempenho nas provas, " +
        "realizadas durante o exame.\n" +
        "Sendo possivel fazer uma filtragem por gêreno.")

        form = MeuFormulario()
        context = {
            'form' : form,
            'menssagem' : menssagem
        }
        return render(request, 'base/quest_socio_notas.html', context=context)
    else:

        form = MeuFormulario(request.POST)

        Q = form.data['questao']
        prova = form.data['nota']
        filtro_sexo = form.data['sexo']

        # Microdado_Amostra = pd.read_csv(caminho, sep= ';', encoding = "ISO-8859-1")
       
        
        Amostra = [prova, Q, 'TP_SEXO']
        Microdado_Amostra = bd_quest_socio_notas.buscar_dataframe_no_banco(Amostra)

        DataFrame = Microdado_Amostra.filter(items = Amostra)

        if filtro_sexo == 'ambos':
            pass
        elif filtro_sexo == 'm':
            DataFrame = DataFrame[DataFrame['TP_SEXO']=='M']
            Amostra = [prova, Q]
        else:
            DataFrame = DataFrame[DataFrame['TP_SEXO']=='F']
            Amostra = [prova, Q]

        DataFrame = DataFrame.sort_values(by=[Q])
        dados = DataFrame.groupby(Q)[prova]
        dados = dados.describe()


        width = 0.25         # A largura das barras

        mpl.rcParams['lines.linewidth'] = 2
        mpl.rcParams['lines.linestyle'] = '--'

        figura = plt.figure(figsize=(17, 29))
        figura.suptitle('Relatório de Compreenssão em formato de gráfico, \n'+
        'realizando o comparativo entre: Questão Socioeconômica e Desempenho no ENEM', size=26)
        
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
        plt.title(Q, size=24)
        plt.ylabel('Nota Média Global no Exame')
        plt.xlabel('Questão Socioeconômica')

        figura.add_subplot(6,2,3)
        plt.bar(dados.index, dados['count'], color='r', width=width, label="quantidade")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Quantidade de Respostas')
        plt.xlabel('Questão Socioeconômica')

        figura.add_subplot(6,2,4)
        plt.plot(dados.index, dados['count'], color='#BA7ACD', label="quantidade")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Quantidade de Respostas')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6,2,5)
        plt.bar(dados.index, dados['25%'], color='y', width=width, label="25%")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Nota ate 25%/ Global no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6,2,6)
        plt.plot(dados.index, dados['25%'], color='b', label="25%")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Nota ate 25%/ Global no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6,2,7)
        plt.bar(dados.index, dados['50%'], color='#EA5ACD', width=width, label="50%")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Nota até 50%/ Global no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6,2,8)
        plt.plot(dados.index, dados['50%'], color='#EA5ACD', label="50%")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Nota até 50%/ Global no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6,2,9)
        plt.bar(dados.index, dados['max'], color='#AA5ACD', width=width, label="máximo")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Nota Máxima no Exame')
        plt.xlabel('Questão Socioeconômica')


        figura.add_subplot(6, 2, 10)
        plt.scatter(dados.index, dados['max'], color='#AA5ACD',  label="máximo")
        plt.legend()
        
        # plt.xlim(limits)
        plt.title(Q, size=24)
        plt.ylabel('Nota Máxima no Exame')
        plt.xlabel('Questão Socioeconômica')

        # plt.show(figura)
        buffer = BytesIO()
        savefig = plt.savefig(buffer, format='png', facecolor='#e8eeff')
        # nome_do_relatorio = 'dados_relatorio/' + str(uuid.uuid4()) + '.pdf'
        # nome_destino_do_relatorio = str(BASE_DIR) + '/static/' + nome_do_relatorio
        # plt.savefig(fname=nome_destino_do_relatorio, format='pdf', facecolor='#e8eeff')
        # plt.savefig(fname='dados/Relatório comparativo entre Questões Socioeconômicas e Desempenho no Enem.pdf' , format='pdf')
        buffer.seek(0)
        image_png = buffer.getvalue()
        image = base64.b64encode(image_png)
        imagem_relatorio = image.decode('utf-8')
        buffer.close()

        # fig = go.Figure(data=dados) 
        # fig.show() 

        # plt.show(figura)
        buffer = BytesIO()
        savefig = plt.savefig(buffer, format='png', facecolor='#e8eeff')
        # nome_do_relatorio = 'dados_relatorio/' + str(uuid.uuid4()) + '.pdf'
        # nome_destino_do_relatorio = str(BASE_DIR) + '/static/' + nome_do_relatorio
        # plt.savefig(fname=nome_destino_do_relatorio, format='pdf', facecolor='#e8eeff')
        # plt.savefig(fname='dados/Relatório comparativo entre Questões Socioeconômicas e Desempenho no Enem.pdf' , format='pdf')
        buffer.seek(0)
        image_png = buffer.getvalue()
        image = base64.b64encode(image_png)
        imagem_relatorio = image.decode('utf-8')
        buffer.close()

        fig = px.line(dados)
        rowEvenColor = 'lightgrey'
        rowOddColor = 'white'

        relatorio = fig.to_html()

        fig = go.Figure(data=[go.Table(
                header=dict(
                    values=['Respostas', 'medias', 'máximo', 'quant alunos', '25%', '50%', '75%'],
                    fill_color='royalblue',
                    height=40,
                    line_color='darkslategray',
                    align=['left','center'],
                    font=dict(color='white', size=12)
                ),
                cells=dict(
                    values=[dados.index,
                    dados['mean'].apply(formatar), dados['max'], dados['count'], dados['25%'].apply(formatar), dados['50%'].apply(formatar), dados['75%'].apply(formatar)],
                    line_color='darkslategray',
                    # 2-D list of colors for alternating rows
                    fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
                    align = ['left', 'center'],
                    font = dict(color = 'darkslategray', size = 11)
                    ))
                ])

        relatorio_em_tabela = fig.to_html()

        if form.is_valid():
            print(form.changed_data)
        else:
            pass

        context = {
            'form' : form,
            'imagem_relatorio' : imagem_relatorio,
            'relatorio_em_tabela' : relatorio_em_tabela,
            'relatorio' : relatorio,
            'dados' : dados
        }

    return render(request, 'base/relatorio_quest_socio_notas_sexo.html', context=context)
    
