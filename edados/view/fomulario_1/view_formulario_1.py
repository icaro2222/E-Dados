from django.shortcuts import render
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from io import BytesIO
import plotly.express as px
import base64
from edados.formularios.formulario_1.formulario_1 import Formulario_1
from edados.formularios.filtros.filtros import Formulario_filtros
import numpy as np
from edados.database import bd_formulario_1

def formatar(valor):
    return "{:,.2f}".format(valor)

def formulario_1(request):

    questao= 'Q001'
    demografico = 'TP_SEXO'

    if request.method == 'GET':        
        menssagem = ("Formulário 1.")

        form = Formulario_1()
        form_filtro = Formulario_filtros()
        context = {
            'form' : form,
            'menssagem' : menssagem,
            'form_filtro' : form_filtro
        }
        return render(request, 'base/formulario_1/quest_formulario_1.html', context=context)
    else:


        # Recebendo fomulario da tela
        form = Formulario_1(request.POST)
        form_filtro = Formulario_filtros(request.POST)

        # Variáveis vindas do Formulario
        questao= form.data['questao']
        demografico = form.data['demografico']
        filtro_deficiencia = form.data['deficiencia']

        # Formulario de Filtro
        filtro_sexo = form_filtro.data['sexo']
        filtro_ano = form_filtro.data['ano']

        if(filtro_sexo != 'ambos'):
            Amostra = [demografico, questao, 'TP_SEXO']
            if(filtro_deficiencia != 'todas' and filtro_deficiencia != 'nenhuma'):
                Microdado_Amostra = bd_formulario_1.buscar_dataframe_no_banco(Amostra, filtro_sexo=filtro_sexo, filtro_deficiencia=filtro_deficiencia, filtro_ano=filtro_ano)
            else:
                Microdado_Amostra = bd_formulario_1.buscar_dataframe_no_banco(Amostra, filtro_sexo=filtro_sexo, filtro_ano=filtro_ano)
        else:
            Amostra = [demografico, questao]
            if(filtro_deficiencia != 'todas' and filtro_deficiencia != 'nenhuma'):
                Microdado_Amostra = bd_formulario_1.buscar_dataframe_no_banco(Amostra, filtro_deficiencia=filtro_deficiencia, filtro_ano=filtro_ano)
            else:
                Microdado_Amostra = bd_formulario_1.buscar_dataframe_no_banco(Amostra, filtro_ano=filtro_ano)
        


        menssagem = 'Formulário 1'

        if(demografico == 'TP_SEXO'):
            vetor = demografico_sexo(Microdado_Amostra, demografico, questao)
            imagem_relatorio = vetor[0]
            relatorio_em_linha = vetor[1]
            relatorio_em_tabela_feminino = vetor[2]
            relatorio_em_tabela_masculino = vetor[3]

            context = {
                'form' : form,
                'form_filtro' : form_filtro,
                'menssagem' : menssagem,
                'imagem_relatorio' : imagem_relatorio,
                'relatorio_em_linha' : relatorio_em_linha,
                'relatorio_em_tabela_feminino' : relatorio_em_tabela_feminino,
                'relatorio_em_tabela_masculino' : relatorio_em_tabela_masculino
            }
        else:
            if(demografico == 'TP_ESTADO_CIVIL'):
                vetor = demografico_estado_civil(Microdado_Amostra, demografico, questao)
                relatorio_em_linha = vetor[0]

                context = {
                    'form' : form,
                    'form_filtro' : form_filtro,
                    'menssagem' : menssagem,
                    'relatorio_em_linha' : relatorio_em_linha
                }

    return render(request, 'base/formulario_1/relatorio_formulario_1.html', context=context)
    

def demografico_sexo(Microdado_Amostra, demografico, questao):

        width = 0.25         # A largura das barras

        DataFrame = Microdado_Amostra.sort_values(by=[questao])
        DataFrame = DataFrame.groupby([demografico, questao])
        DataFrame = DataFrame['TP_SEXO'].count()
        Dataset_F = DataFrame['F']
        Dataset_M = DataFrame['M']
            
        figura = plt.figure(figsize=(12, 8))
        figura.suptitle('Relatório de Compreenssão em formato de gráfico, \n'+
        'realizando o comparativo entre: Questão Socioeconômica e Desempenho no ENEM', size=16)
        figura.add_subplot(1,1,1)

        br1 = np.arange(len(Dataset_F.index))
        br2 = [x + width for x in br1]

        bar_label_feminino = plt.bar(br1, Dataset_F, color='y', width=width, label="feminíno")
        bar_label_masculino = plt.bar(br2, Dataset_M, color='b', width=width, label="masculíno")
        
        plt.bar_label(bar_label_feminino, fmt='%.2f', padding=2)
        plt.bar_label(bar_label_masculino, fmt='%.2f', padding=2)

        labels = np.arange(len(Dataset_F.index.tolist()))
        print(labels)
        plt.xticks(labels, Dataset_F.index.tolist())

        plt.legend(loc='center', bbox_to_anchor=(0.9, 1))
        plt.title(questao)
        plt.ylabel('Quantidade de Inscritos por Questão Demográfica')
        plt.xlabel('Respostas da Questão Socioeconômica')

        buffer = BytesIO()
        plt.savefig(buffer, format='png', facecolor='#e8eeff')
        buffer.seek(0)
        image_png = buffer.getvalue()
        image = base64.b64encode(image_png)
        imagem_relatorio = image.decode('utf-8')
        buffer.close()

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            y=Dataset_M,
            x=Dataset_M.index,
            name = 'masculíno', # Style name/legend entry with html tags
            connectgaps=True # override default to connect the gaps
        ))
        fig.add_trace(go.Scatter(
            y=Dataset_F,
            x=Dataset_F.index,
            name='feminíno',
        ))

        relatorio = fig.to_html()

        # Definindo cores que seram utilizadas na  tabela
        rowEvenColor = 'lightgrey'
        rowOddColor = 'white'


        # Criando a tabela, utilizando a biblioteca "go".
        figura_tabela_feminino = go.Figure(data=[go.Table(
                header=dict(
                    values=['Respostas', 'quantidade'],
                    fill_color='royalblue',
                    height=40,
                    line_color='darkslategray',
                    align=['left','center'],
                    font=dict(color='white', size=12)
                ),
                cells=dict(
                    values=[Dataset_F.index, Dataset_F],
                    line_color='darkslategray',
                    fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
                    align = ['left', 'center'],
                    font = dict(color = 'darkslategray', size = 11)
                    ))
                ])

        figura_tabela_masculino = go.Figure(data=[go.Table(
                header=dict(
                    values=['Respostas', 'quantidade'],
                    fill_color='royalblue',
                    height=40,
                    line_color='darkslategray',
                    align=['left','center'],
                    font=dict(color='white', size=12)
                ),
                cells=dict(
                    values=[Dataset_M.index, Dataset_M],
                    line_color='darkslategray',
                    fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
                    align = ['left', 'center'],
                    font = dict(color = 'darkslategray', size = 11)
                    ))
                ])


        figura_tabela_feminino.add_trace(go.Bar(x=Dataset_M.index, y=Dataset_M))
        figura_tabela_feminino.add_trace(go.Bar(x=Dataset_F.index, y=Dataset_F))

        figura_tabela_feminino.update_layout(
            title_text = 'Tabela demográfica Feminína.',
            height = 500,
            margin = {'t':75, 'l':50},
            yaxis = {'domain': [0, .45]},
            xaxis2 = {'anchor': 'y2'},
            yaxis2 = {'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'}
        )

        figura_tabela_masculino.update_layout(
            title_text = 'Tabela demográfica Masculína.',
            height = 300,
            margin = {'t':75, 'l':50},
            yaxis = {'domain': [0, .45]},
            xaxis2 = {'anchor': 'y2'},
            yaxis2 = {'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'}
        )

        relatorio_em_tabela = figura_tabela_feminino.to_html()
        figura_tabela_masculino = figura_tabela_masculino.to_html()

        return [imagem_relatorio, relatorio, relatorio_em_tabela, figura_tabela_masculino]
def demografico_estado_civil(Microdado_Amostra, demografico, questao):

        width = 0.25         # A largura das barras

        DataFrame = Microdado_Amostra.sort_values(by=[questao])
        DataFrame = DataFrame.groupby([demografico, questao])
        DataFrame = DataFrame[demografico].count()

        # rotacionar 
        DataFrame = DataFrame.unstack()

        print(DataFrame.index[0])


        lista_dos_index = DataFrame.index.to_list()

        # desrotacionar 
        DataFrame = DataFrame.stack()

        fig = go.Figure()

        for index in lista_dos_index:
            
            if index=='0':
                nome = 'Não informou'
            elif index=='1':
                nome = 'Solteiro(a)'
            elif index=='2':
                nome = 'Casado(a)'
            elif index=='3':
                nome = 'Divorciado(a)'
            else:
                nome = 'Viúvo(a)'
            fig.add_trace(go.Scatter(
                y=DataFrame[index],
                x=DataFrame[index].index,
                name = nome,
            ))
            
        relatorio = fig.to_html()

        return [relatorio]