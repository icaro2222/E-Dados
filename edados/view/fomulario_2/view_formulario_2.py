from django.shortcuts import render
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from io import BytesIO
import plotly.express as px
import base64
from edados.formularios.formulario_2.formulario_2 import Formulario_2
from edados.formularios.filtros.filtros import Formulario_filtros
import numpy as np
from edados.database import bd_quest_socio_notas_deficiencia

def formatar(valor):
    return "{:,.2f}".format(valor)

def formulario_2(request):

    Q = 'TP_SEXO'
    prova = 'NU_NOTA_MT'

    if request.method == 'GET':        
        menssagem = ("Correlação entre as questões socioeconômicas e desempenho no exame, somados a filtros.")

        form = Formulario_2()
        form_filtro = Formulario_filtros()
        context = {
            'form' : form,
            'menssagem' : menssagem,
            'form_filtro' : form_filtro
        }
        return render(request, 'base/formulario_2/quest_formulario_2.html', context=context)
    else:


        # Recebendo fomulario da tela
        form = Formulario_2(request.POST)
        form_filtro = Formulario_filtros(request.POST)

        # Variáveis vindas do Formulario
        Q = form.data['questao']
        prova = form.data['nota']
        filtro_deficiencia = form.data['deficiencia']

        # Formulario de Filtro
        filtro_sexo = form_filtro.data['sexo']

        if(filtro_sexo != 'ambos'):
            Amostra = [prova, Q, 'TP_SEXO']
            if(filtro_deficiencia != 'todas' and filtro_deficiencia != 'nenhuma'):
                Microdado_Amostra = bd_quest_socio_notas_deficiencia.buscar_dataframe_no_banco(Amostra, filtro_sexo=filtro_sexo, filtro_deficiencia=filtro_deficiencia)
            else:
                Microdado_Amostra = bd_quest_socio_notas_deficiencia.buscar_dataframe_no_banco(Amostra, filtro_sexo=filtro_sexo)
        else:
            Amostra = [prova, Q]
            if(filtro_deficiencia != 'todas' and filtro_deficiencia != 'nenhuma'):
                Microdado_Amostra = bd_quest_socio_notas_deficiencia.buscar_dataframe_no_banco(Amostra, filtro_deficiencia=filtro_deficiencia)
            else:
                Microdado_Amostra = bd_quest_socio_notas_deficiencia.buscar_dataframe_no_banco(Amostra)

        width = 0.25         # A largura das barras

        Dataframe = Microdado_Amostra.filter(items = Amostra)
        Dataframe = Dataframe.sort_values(by=[Q])
        Dataframe = Dataframe.groupby(Q)[prova]
        Dataframe = Dataframe.describe()     

        # Seleção conforme a escolha do usuário na tela do formulario
        if filtro_deficiencia == 'ambos':
            br1 = np.arange(len(Dataframe.index))
            br2 = [x + width for x in br1]

            figura = plt.figure(figsize=(12, 8))
            figura.suptitle('Relatório de correlação entre: Questão socioeconômica e Desempenho no Enem', size=16)
            figura.add_subplot(1,1,1)

            bar_label_mean = plt.bar(br2, Dataframe['mean'], color='r', width=width, label="Média")
            plt.bar_label(bar_label_mean, fmt='%.2f', padding=2)

        else:
            # caminho_a_deficiencia = caminho2 + filtro_deficiencia + '.csv'
            # Microdado_Amostra = pd.read_csv(caminho_a_deficiencia, sep= ';', encoding = "ISO-8859-1")
            # DataFrame = Microdado_Amostra.filter(items = Amostra)
            # DataFrame = DataFrame.sort_values(by=[Q])
            # DataFrame_dificiente = DataFrame[DataFrame[filtro_deficiencia]==1]

            # DataFrame_dificiente = DataFrame_dificiente.sort_values(by=[Q])
            # dados = DataFrame_dificiente.groupby(Q)[prova]
            # dataset = dados.describe()
            dataset = Dataframe
            figura = plt.figure(figsize=(12, 8))
            figura.suptitle('Relatório de Compreenssão em formato de gráfico, \n'+
            'realizando o comparativo entre: Questão Socioeconômica e Desempenho no ENEM', size=16)
            figura.add_subplot(1,1,1)

            br1 = np.arange(len(dataset.index))
            br2 = [x + width for x in br1]
            br3 = [x + width for x in br2]
            bar_label_max = plt.bar(br2, dataset['max'], color='r', width=width, label="Máximno")
            bar_label_mean = plt.bar(br1, dataset['mean'], color='b', width=width, label="Média")
            bar_label_min = plt.bar(br3, dataset['min'], color='y', width=width, label="Mínimo")
            
            plt.bar_label(bar_label_max, fmt='%.2f', padding=2)
            plt.bar_label(bar_label_mean, fmt='%.2f', padding=2)
            plt.bar_label(bar_label_min, fmt='%.2f', padding=2)

        plt.legend(loc='center', bbox_to_anchor=(0.9, 1))
        plt.title(Q)
        plt.ylabel('Nota Média dos Inscritos')
        plt.xlabel('Questão Socioeconômica')

        buffer = BytesIO()
        plt.savefig(buffer, format='png', facecolor='#e8eeff')
        buffer.seek(0)
        image_png = buffer.getvalue()
        image = base64.b64encode(image_png)
        imagem_relatorio = image.decode('utf-8')
        buffer.close()

        fig = px.line(Dataframe)
        relatorio = fig.to_html()

        figura_com_criador_de_tabela = px.bar(Dataframe)
        figura_com_criador_de_tabela = figura_com_criador_de_tabela.to_html()

        figura_tabela_da_media = px.bar(Dataframe['mean'])
        figura_tabela_da_media = figura_tabela_da_media.to_html()

        headerColor = 'grey'
        rowEvenColor = 'lightgrey'
        rowOddColor = 'white'

        figura_tabela = go.Figure(data=[go.Table(
                header=dict(
                    values=['Respostas', 'medias', 'máximo', 'quant alunos', '25%', '50%', '75%'],
                    fill_color='royalblue',
                    height=40,
                    line_color='darkslategray',
                    align=['left','center'],
                    font=dict(color='white', size=12)
                ),
                cells=dict(
                    values=[Dataframe.index,
                    Dataframe['mean'].apply(formatar), Dataframe['max'], 
                    Dataframe['count'], Dataframe['25%'].apply(formatar), 
                    Dataframe['50%'].apply(formatar), Dataframe['75%'].apply(formatar)],
                    line_color='darkslategray',
                    fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
                    align = ['left', 'center'],
                    font = dict(color = 'darkslategray', size = 11)
                    ))
                ])

        figura_tabela.add_trace(go.Bar(x=Dataframe.index, y=Dataframe['max']))
        figura_tabela.add_trace(go.Bar(x=Dataframe.index, y=Dataframe['mean']))

        figura_tabela.update_layout(
            title_text = 'Pessoas Com Deficiência X Pessoas Sem Deficiência',
            height = 800,
            margin = {'t':75, 'l':50},
            yaxis = {'domain': [0, .45]},
            xaxis2 = {'anchor': 'y2'},
            yaxis2 = {'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'}
        )

        relatorio_em_tabela = figura_tabela.to_html()

        if form.is_valid():
            print(form.changed_data)
        else:
            pass

        context = {
            'form' : form,
            'imagem_relatorio' : imagem_relatorio,
            'relatorio' : relatorio,
            'form_filtro' : form_filtro,
            'figura_com_criador_de_tabela' : figura_com_criador_de_tabela,
            'figura_tabela_da_media' : figura_tabela_da_media,
            'relatorio_em_tabela' : relatorio_em_tabela
        }

    return render(request, 'base/formulario_2/relatorio_formulario_2.html', context=context)
    
