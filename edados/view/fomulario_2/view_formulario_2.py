from django.shortcuts import render
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from io import BytesIO
import plotly.express as px
import base64
from edados.formularios.formulario_2.formulario_2 import Formulario_2
from edados.formularios.filtros.formulario_1_filtros import Formulario_filtros
import numpy as np
from django.utils.html import format_html_join
from edados.database import bd_quest_socio_notas_deficiencia

def formatar(valor):
    return "{:,.2f}".format(valor)

def formulario_2(request):

    Q = 'TP_SEXO'
    prova = 'NU_NOTA_MT'

    if request.method == 'GET':    
          
        menssagem = "Formulário:"          
        menssagem1 = ("Correlação entre as questões socioeconômicas e desempenho no exame, somados a filtros.")
        menssagem_informativa = """
        A análise de dados é uma ferramenta poderosa para compreender e tirar conclusões a partir de grandes quantidades de informações. Uma aplicação interessante da análise de dados é na área da educação, mais especificamente na análise do desempenho dos alunos em exames, como o Enem.
        Ao analisar o desempenho dos alunos no Enem, é possível identificar padrões e correlações entre o desempenho e fatores socioeconômicos, como renda familiar, escolaridade dos pais e acesso à internet. Essas informações podem ser obtidas por meio de questionários aplicados aos alunos ou de dados do IBGE.
        Uma plataforma online que ofereça filtros pode ser de grande ajuda nessa análise. Por exemplo, é possível filtrar os dados por região, tipo de escola e nível socioeconômico dos alunos. Isso permite que sejam identificadas correlações específicas para cada grupo de alunos, o que pode ser de grande ajuda para a elaboração de políticas públicas mais eficazes.
        Além disso, a plataforma pode oferecer um indicador de acertos por questão, permitindo que sejam identificadas as questões em que os alunos têm mais dificuldade e que exigem maior atenção por parte dos professores e gestores escolares.
        Portanto, a análise de dados combinada com uma plataforma online que ofereça filtros pode ser uma ferramenta poderosa para compreender as correlações entre fatores socioeconômicos e desempenho no Enem, além de fornecer informações valiosas para a elaboração de políticas públicas e para a gestão escolar."""
        
        menssagem_informativa = menssagem_informativa.split('\n')
        menssagem_informativa = format_html_join('\n', '<p>{}</p>', ((line,) for line in menssagem_informativa))
        
        
        
        form = Formulario_2()
        form_filtro = Formulario_filtros()
        context = {
            'form' : form,
            'menssagem' : menssagem,
            'menssagem1' : menssagem_informativa,
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
        filtro_ano = form_filtro.data['ano']

        if(filtro_sexo != 'todos'):
            Amostra = [prova, Q, 'TP_SEXO']
            if(filtro_deficiencia != 'todas' and filtro_deficiencia != 'nenhuma'):
                Microdado_Amostra = bd_quest_socio_notas_deficiencia.buscar_dataframe_no_banco(Amostra, filtro_sexo=filtro_sexo, filtro_deficiencia=filtro_deficiencia, filtro_ano=filtro_ano)
            else:
                Microdado_Amostra = bd_quest_socio_notas_deficiencia.buscar_dataframe_no_banco(Amostra, filtro_sexo=filtro_sexo, filtro_ano=filtro_ano)
        else:
            Amostra = [prova, Q]
            if(filtro_deficiencia != 'todas' and filtro_deficiencia != 'nenhuma'):
                Microdado_Amostra = bd_quest_socio_notas_deficiencia.buscar_dataframe_no_banco(Amostra, filtro_deficiencia=filtro_deficiencia, filtro_ano=filtro_ano)
            else:
                Microdado_Amostra = bd_quest_socio_notas_deficiencia.buscar_dataframe_no_banco(Amostra, filtro_ano=filtro_ano)
            
        print(filtro_ano)
        width = 0.25         # A largura das barras

        Dataframe = Microdado_Amostra.filter(items = Amostra)
        Dataframe = Dataframe.sort_values(by=[Q])
        Dataframe = Dataframe.groupby(Q)[prova]
        Dataframe = Dataframe.describe()     

        # Seleção conforme a escolha do usuário na tela do formulario
        # if filtro_deficiencia == 'ambos':
            # br1 = np.arange(len(Dataframe.index))
            # br2 = [x + width for x in br1]

            # figura = plt.figure(figsize=(12, 8))
            # figura.suptitle('Relatório de correlação entre: Questão socioeconômica e Desempenho no Enem', size=16)
            # figura.add_subplot(1,1,1)

            # bar_label_mean = plt.bar(br2, Dataframe['mean'], color='r', width=width, label="Média")
            # plt.bar_label(bar_label_mean, fmt='%.2f', padding=2)

        # else:
            # caminho_a_deficiencia = caminho2 + filtro_deficiencia + '.csv'
            # Microdado_Amostra = pd.read_csv(caminho_a_deficiencia, sep= ';', encoding = "ISO-8859-1")
            # DataFrame = Microdado_Amostra.filter(items = Amostra)
            # DataFrame = DataFrame.sort_values(by=[Q])
            # DataFrame_dificiente = DataFrame[DataFrame[filtro_deficiencia]==1]

            # DataFrame_dificiente = DataFrame_dificiente.sort_values(by=[Q])
            # dados = DataFrame_dificiente.groupby(Q)[prova]
            # dataset = dados.describe()
            # dataset = Dataframe
            # figura = plt.figure(figsize=(12, 8))
            # figura.suptitle('Relatório de Compreenssão em formato de gráfico, \n'+
            # 'realizando o comparativo entre: Questão Socioeconômica e Desempenho no ENEM', size=16)
            # figura.add_subplot(1,1,1)

            # br1 = np.arange(len(dataset.index))
            # br2 = [x + width for x in br1]
            # br3 = [x + width for x in br2]

            # bar_label_min = plt.bar(br1, dataset['min'], color='y', width=width, label="Mínimo")
            # bar_label_mean = plt.bar(br2, dataset['mean'], color='b', width=width, label="Média")
            # bar_label_max = plt.bar(br3, dataset['max'], color='r', width=width, label="Máximno")
            
            # plt.bar_label(bar_label_max, fmt='%.2f', padding=2)
            # plt.bar_label(bar_label_mean, fmt='%.2f', padding=2)
            # plt.bar_label(bar_label_min, fmt='%.2f', padding=2)

            # labels = np.arange(len(dataset.index.tolist()))
            # print(labels)
            # plt.xticks(labels, dataset.index.tolist())
            # plt.xticks()


        # plt.legend(loc='center', bbox_to_anchor=(0.9, 1))
        # plt.title(Q)
        # plt.ylabel('Desempenho dos Inscritos no Enem')
        # plt.xlabel('Respostas da Questão Socioeconômica: "'+Q+'"')

        # buffer = BytesIO()
        # plt.savefig(buffer, format='png', facecolor='#e8eeff')
        # buffer.seek(0)
        # image_png = buffer.getvalue()
        # image = base64.b64encode(image_png)
        # imagem_relatorio = image.decode('utf-8')
        # buffer.close()

        figura_com_criador_de_tabela = px.bar(Dataframe)
        figura_com_criador_de_tabela = figura_com_criador_de_tabela.to_html()
        
        figura_tabela_da_media = px.bar(Dataframe['mean'])
        figura_tabela_da_media = figura_tabela_da_media.to_html()

        rowEvenColor = 'lightgrey'
        rowOddColor = 'white'

        figura_tabela = go.Figure(data=[go.Table(
                header=dict(
                    values=['Respostas', 'média', 'máximo', 'quant alunos', '25%', '50%', '75%'],
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

        figura_tabela.add_trace(go.Bar(
            text=Dataframe['min'].apply(formatar),
            x=Dataframe.index, 
            y=Dataframe['min'],
            name='mínimo'))
        figura_tabela.add_trace(go.Bar(
            text=Dataframe['mean'].apply(formatar),
            x=Dataframe.index, 
            y=Dataframe['mean'],
            name='média'))
        figura_tabela.add_trace(go.Bar(
            text=Dataframe['max'].apply(formatar),
            x=Dataframe.index, 
            y=Dataframe['max'],
            name='máximo'),
            )

        figura_tabela.update_layout(
            title_text = """Quadro de correlação entre o desempenho e a resposta da questão socioeconômica.""",
            height = 600,
            margin = {'t':75, 'l':50},
            yaxis = {'domain': [0, .45]},
            xaxis2 = {'anchor': 'y2'},
            xaxis_title="Respota do questionário socioeconômico",
            yaxis_title="Desempenho",
            yaxis2 = {'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'},
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )

        relatorio_em_tabela = figura_tabela.to_html()

        if form.is_valid():
            print(form.changed_data)
        else:
            pass

        menssagem1 = """Formulário 2:"""
        menssagem = """Correlação entre as respostas do questionário socioeconômico e
        o desempenho no exame."""

        context = {
            'form' : form,
            'menssagem' : menssagem,
            'menssagem1' : menssagem1,
            # 'imagem_relatorio' : imagem_relatorio,
            'form_filtro' : form_filtro,
            'figura_com_criador_de_tabela' : figura_com_criador_de_tabela,
            'relatorio_em_tabela' : relatorio_em_tabela
        }

    return render(request, 'base/formulario_2/relatorio_formulario_2.html', context=context)
    
