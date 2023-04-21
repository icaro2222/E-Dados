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
from edados.formularios.form_filtro import Formulario_filtro
from edados.settings import BASE_DIR
import numpy as np

caminho = os.path.join(BASE_DIR, 'dados/Microdado_Amostra.csv')

def view_regiao_mapa(request):

    Q = 'TP_SEXO'
    prova = 'NU_NOTA_MT'

    if request.method == 'GET':
        form = Formulario_filtro(request.POST)

        if form.is_valid():
            print(form.changed_data)

        menssagem = ("Desempenho por Região")

        form = Formulario_filtro()
        context = {
            'form' : form,
            'menssagem' : menssagem
        }
        return render(request, 'base/quest_socio_notas.html', context=context)
    else:

        form = Formulario_filtro(request.POST)

        # Q = form.data['questao']
        # prova = form.data['nota']
        # filtro_sexo = form.data['sexo']

        # Microdado_Amostra = pd.read_csv(caminho, sep= ';', encoding = "ISO-8859-1")
        # Amostra = [prova, Q, 'TP_SEXO', 'SG_UF_ESC', 'longitude', 'latitude']
        # DataFrame = Microdado_Amostra.filter(items = Amostra)

        # if filtro_sexo == 'ambos':
        #     pass
        # elif filtro_sexo == 'm':
        #     DataFrame = DataFrame[DataFrame['TP_SEXO']=='M']
        #     Amostra = [prova, Q]
        # else:
        #     DataFrame = DataFrame[DataFrame['TP_SEXO']=='F']
        #     Amostra = [prova, Q]

        # DataFrame = DataFrame.sort_values(by=[Q])
        # dados = DataFrame.groupby('SG_UF_ESC')[prova]
        # dados = dados.describe()


        # width = 0.25         # A largura das barras

        # mpl.rcParams['lines.linewidth'] = 2
        # mpl.rcParams['lines.linestyle'] = '--'

        # figura = plt.figure(figsize=(10, 9))
        # figura.suptitle('Relatório de Compreenssão em formato de gráfico, \n'+
        # 'realizando o comparativo entre: Questão Socioeconômica e Desempenho no ENEM', size=26)
        
        # DataFrame.plot.scatter(y='latitude', x='longitude', c=DataFrame[prova], figsize=(10, 8), label="máximo")
        # plt.legend()
        
        # # plt.xlim(limits)
        # plt.title(Q, size=24)
        # plt.ylabel('Nota Máxima no Exame')
        # plt.xlabel('Questão Socioeconômica')

        # # plt.show(figura)
        # buffer = BytesIO()
        # plt.savefig(buffer, format='png', facecolor='#e8eeff')
        # # nome_do_relatorio = 'dados_relatorio/' + str(uuid.uuid4()) + '.pdf'
        # # nome_destino_do_relatorio = str(BASE_DIR) + '/static/' + nome_do_relatorio
        # # plt.savefig(fname=nome_destino_do_relatorio, format='pdf', facecolor='#e8eeff')
        # # plt.savefig(fname='dados/Relatório comparativo entre Questões Socioeconômicas e Desempenho no Enem.pdf' , format='pdf')
        # buffer.seek(0)
        # image_png = buffer.getvalue()
        # image = base64.b64encode(image_png)
        # imagem_relatorio = image.decode('utf-8')
        # buffer.close()

        # # fig = go.Figure(data=dados) 
        # # fig.show() 

        # # plt.show(figura)
        # buffer = BytesIO()
        # savefig = plt.savefig(buffer, format='png', facecolor='#e8eeff')
        # # nome_do_relatorio = 'dados_relatorio/' + str(uuid.uuid4()) + '.pdf'
        # # nome_destino_do_relatorio = str(BASE_DIR) + '/static/' + nome_do_relatorio
        # # plt.savefig(fname=nome_destino_do_relatorio, format='pdf', facecolor='#e8eeff')
        # # plt.savefig(fname='dados/Relatório comparativo entre Questões Socioeconômicas e Desempenho no Enem.pdf' , format='pdf')
        # buffer.seek(0)
        # image_png = buffer.getvalue()
        # image = base64.b64encode(image_png)
        # imagem_relatorio = image.decode('utf-8')
        # buffer.close()

        # fig = px.line(y=DataFrame['longitude'], x=DataFrame['latitude'])
        # # fig = px.scatter_mapbox(dados, lat="centroid_lat", lon="centroid_lon",     color="peak_hour", size="car_hours",
        # #           color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)
        # relatorio = fig.to_html()

        # if form.is_valid():
        #     print(form.changed_data)
        # else:
        #     pass

        context = {
            'form' : form,
            # 'imagem_relatorio' : imagem_relatorio,
            # 'nome_do_relatorio' : nome_do_relatorio,
            # 'relatorio' : relatorio,
            # 'dados' : DataFrame
        }

    return render(request, 'base/relatorio_regiao-mapa.html', context=context)
    
