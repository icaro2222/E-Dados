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
from edados.formularios.form_questao_demografica_e_socioeonomica import MeuFormulario
from edados.settings import BASE_DIR
import numpy as np
from edados.database import bd_quest_socio_notas

caminho = os.path.join(BASE_DIR, 'dados/Microdado_Amostra.csv')

def logar(request):
    # return render(request, 'indexTest.html')
    
    return HttpResponse("oi, DEUUUUUUU CERTTTTTOOOOOO. AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

def formatar(valor):
    return "{:,.2f}".format(valor)

def view_quest_demo_socioe(request):

    Q = 'TP_SEXO'
    prova = 'NU_NOTA_MT'

    if request.method == 'GET':
        form = MeuFormulario(request.POST)

        if form.is_valid():
            print(form.changed_data)

        form = MeuFormulario()
        menssagem = ("A demografia baseia-se em dados estatísticos, para analisar, organizar e fornecer informações sobre a população de um território.")
        context = {
            'form' : form,
            'menssagem' : menssagem
        }
        return render(request, 'base/quest_socio_notas.html', context=context)
    else:
        form = MeuFormulario(request.POST)
        
        Q = form.data['questionario_socioeconomico']
        prova = form.data['questionario_demografico']

        # Processo de pegar os dados para a realização da análise
        # Microdado_Amostra = pd.read_csv(caminho, sep= ';', encoding = "ISO-8859-1")

        Amostra = [prova, Q]
        Microdado_Amostra = bd_quest_socio_notas.buscar_dataframe_no_banco(Amostra)

        # realizando um agrupamento, para criar uam estrutura para a análise
        ChAmostra = Microdado_Amostra.filter(items = Amostra)
        ChAmostra = ChAmostra.sort_values(by=[Q])
        dados = ChAmostra.groupby(Q)[prova]
        dados = dados.describe()

        NU_NOTA_CNCHAmostra = ChAmostra[prova]
        
        width = 0.25         # A largura das barras
        plt.figure(figsize=(0,0))

        r1 = np.arange(len(NU_NOTA_CNCHAmostra))
        r2 = [x + width for x in r1]


        mpl.rcParams['lines.linewidth'] = 2
        mpl.rcParams['lines.linestyle'] = '--'

        figura = plt.figure(figsize=(17, 12))
        figura.suptitle('Relatório de Compreenssão em formato de gráfico, \n'+
        'realizando o comparativo entre: Questão Demográfica Vs Socioeconômica', size=16)
        
        figura.add_subplot(1,1,1)
        bar_label_mean = plt.bar(dados.index, dados['freq'], color='#BA5ACD', width=width, label="Frequência")
        plt.scatter(dados.index, dados['count'], color='#FA1AFD', label="Quantidade")
        plt.bar_label(bar_label_mean)
        plt.legend()
        
        plt.title(Q, size=14, y=1)
        plt.ylabel('Socioeconomico')
        plt.xlabel('Questão Demográficos')

        buffer = BytesIO()
        savefig = plt.savefig(buffer, format='png', facecolor='#e8eeff')
        nome_do_relatorio = 'dados_relatorio/' + str(uuid.uuid4()) + '.pdf'
        nome_destino_do_relatorio = str(BASE_DIR) + '/static/' + nome_do_relatorio
        plt.savefig(fname=nome_destino_do_relatorio, format='pdf', facecolor='#e8eeff')
        
        buffer.seek(0)
        image_png = buffer.getvalue()
        image = base64.b64encode(image_png)
        imagem_relatorio = image.decode('utf-8')
        buffer.close()

        buffer = BytesIO()
        savefig = plt.savefig(buffer, format='png', facecolor='#e8eeff')
        nome_do_relatorio = 'dados_relatorio/' + str(uuid.uuid4()) + '.pdf'
        nome_destino_do_relatorio = str(BASE_DIR) + '/static/' + nome_do_relatorio
        plt.savefig(fname=nome_destino_do_relatorio, format='pdf', facecolor='#e8eeff')
        buffer.seek(0)
        image_png = buffer.getvalue()
        image = base64.b64encode(image_png)
        imagem_relatorio = image.decode('utf-8')
        buffer.close()

        # Cores para criar as tabelas e gráficos
        rowEvenColor = 'lightgrey'
        rowOddColor = 'white'

        # Criando Tabela de corelação entre as questões demográficas e notas 'medias', 'máximo','mínimo'
        fig = go.Figure(data=[go.Table(
                header=dict(
                    values=['Respostas', 'quantidade', 'frequência', 'unico', 'top'],
                    fill_color='royalblue',
                    height=40,
                    line_color='darkslategray',
                    align=['left','center'],
                    font=dict(color='white', size=12) 
                ),
                cells=dict(
                    values=[dados.index,
                    dados['count'], dados['freq'], dados['unique'], dados['top']],
                    line_color='darkslategray',
                    # 2-D list of colors for alternating rows
                    fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
                    align = ['left', 'center'],
                    font = dict(color = 'darkslategray', size = 11)
                    ))
                ])

        relatorio_em_tabela = fig.to_html()

        fig = px.line(dados)
        relatorio_linha = fig.to_html()

        context = {
            'form' : form,
            'imagem_relatorio' : imagem_relatorio,
            'nome_do_relatorio' : nome_do_relatorio,
            'relatorio_em_tabela' : relatorio_em_tabela,
            'relatorio' : relatorio_linha,
        }

    return render(request, 'base/relatorio_quest_socio_notas.html', context=context)
    
