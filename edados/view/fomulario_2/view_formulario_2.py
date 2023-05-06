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

def anotacao(Questao):

    if Questao == 'Q001':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 1 no questionario socioeconômico:
                            <br>A: Nunca estudou.
                            <br>B: Não completou a 4ª série/5º ano do Ensino Fundamental.
                            <br>C: Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.
                            <br>D: Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio.
                            <br>E: Completou o Ensino Médio, mas não completou a Faculdade.
                            <br>F: Completou a Faculdade, mas não completou a Pós-graduação.
                            <br>G: Completou a Pós-graduação.
                            <br>H: Não sei."""
    elif Questao == 'Q002':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 2 no questionario socioeconômico:
                            <br>A: Nunca estudou.
                            <br>B: Não completou a 4ª série/5º ano do Ensino Fundamental.
                            <br>C: Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.
                            <br>D: Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio.
                            <br>E: Completou o Ensino Médio, mas não completou a Faculdade.
                            <br>F: Completou a Faculdade, mas não completou a Pós-graduação.
                            <br>G: Completou a Pós-graduação.
                            <br>H: Não sei."""
    elif Questao == 'Q003':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 3 no questionario socioeconômico:
                            <br>
                            <br>Grupo 1: Lavrador, agricultor sem empregados, bóia fria, criador de animais (gado, porcos, galinhas, ovelhas, cavalos etc.), apicultor,
<br pescador, lenhador, seringueiro, extrativista.
                            <br>Grupo 2: Diarista, empregado doméstico, cuidador de idosos, babá, cozinheiro (em casas particulares), motorista particular, jardineiro, f
<braxineiro de empresas e prédios, vigilante, porteiro, carteiro, office-boy, vendedor, caixa, atendente de loja, auxiliar administrativo, recepcionista, servente de pedreiro, repositor de mercadoria.
                            <br>Grupo 3: Padeiro, cozinheiro industrial ou em restaurantes, sapateiro, costureiro, joalheiro, torneiro mecânico, operador de máquinas, 
<brsoldador, operário de fábrica, trabalhador da mineração, pedreiro, pintor, eletricista, encanador, motorista, caminhoneiro, taxista.
                            <br>Grupo 4: Professor (de ensino fundamental ou médio, idioma, música, artes etc.), técnico (de enfermagem, contabilidade, eletrônica etc.), 
<brpolicial, militar de baixa patente (soldado, cabo, sargento), corretor de imóveis, supervisor, gerente, mestre de obras, pastor, microempresário (proprietário de
<br empresa com menos de 10 empregados), pequeno comerciante, pequeno proprietário de terras, trabalhador autônomo ou por conta própria.
                            <br>Grupo 5: Médico, engenheiro, dentista, psicólogo, economista, advogado, juiz, promotor, defensor, delegado, tenente, capitão, coronel,
<br professor universitário, diretor em empresas públicas ou privadas, político, proprietário de empresas com mais de 10 empregados.
                            <br>Não sei.."""
    elif Questao == 'Q004':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 4 no questionario socioeconômico:
                            <br>
                            <br>Grupo 1: Lavradora, agricultora sem empregados, bóia fria, criadora de animais (gado, porcos, galinhas, ovelhas,
<br cavalos etc.), apicultora, pescadora, lenhadora, seringueira, extrativista.
<br>Grupo 2: Diarista, empregada doméstica, cuidadora de idosos, babá, cozinheira (em casas particulares), motorista particular, jardineira, 
<brfaxineira de empresas e prédios, vigilante, porteira, carteira, office-boy, vendedora, caixa, atendente de loja, auxiliar administrativa, recepcionista, servente de pedreiro, repositora de mercadoria.
<br>Grupo 3: Padeira, cozinheira industrial ou em restaurantes, sapateira, costureira, joalheira, torneira mecânica, operadora de máquinas, 
<brsoldadora, operária de fábrica, trabalhadora da mineração, pedreira, pintora, eletricista, encanadora, motorista, caminhoneira, taxista.
<br>Grupo 4: Professora (de ensino fundamental ou médio, idioma, música, artes etc.), técnica (de enfermagem, contabilidade, eletrônica etc.), 
<brpolicial, militar de baixa patente (soldado, cabo, sargento), corretora de imóveis, supervisora, gerente, mestre de obras, pastora,
<br microempresária (proprietária de empresa com menos de 10 empregados), pequena comerciante, pequena proprietária de terras, trabalhadora autônoma ou por conta própria.
<br>Grupo 5: Médica, engenheira, dentista, psicóloga, economista, advogada, juíza, promotora, defensora, delegada, tenente, capitã, coronel,
<br professora universitária, diretora em empresas públicas ou privadas, política, proprietária de empresas com mais de 10 empregados.
<br>Não sei."""
    elif Questao == 'Q005':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 5 no questionario socioeconômico:
                            <br><br>1: Moro sozinho(a)
<br>2: 2 pessoas
<br>3: 3 pessoas
<br>4: 4 pessoas
<br>5: 5 pessoas
<br>6: 6 pessoas
<br>7: 7 pessoas
<br>8: 8 pessoas
<br>9: 9 pessoas
<br>10: 10 pessoas
<br>11: 11 pessoas
<br>12: 12 pessoas
<br>13: 13 pessoas
<br>14: 14 pessoas
<br>15: 15 pessoas
<br>16: 16 pessoas
<br>17: 17 pessoas
<br>18: 18 pessoas
<br>19: 19 pessoas
<br>20: 20 pessoas"""
    elif Questao == 'Q006':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 6 no questionario socioeconômico:
                            <br>
                            <br>A: Nenhuma renda
<br>B: Até R$ 998,00
<br>C: De R$ 998,01 até R$ 1.497,00
<br>D: De R$ 1.497,01 até R$ 1.996,00
<br>E: De R$ 1.996,01 até R$ 2.495,00
<br>F: De R$ 2.495,01 até R$ 2.994,00
<br>G: De R$ 2.994,01 até R$ 3.992,00
<br>H: De R$ 3.992,01 até R$ 4.990,00
<br>I: De R$ 4.990,01 até R$ 5.988,00
<br>J: De R$ 5.988,01 até R$ 6.986,00
<br>K: De R$ 6.986,01 até R$ 7.984,00
<br>L: De R$ 7.984,01 até R$ 8.982,00
<br>M: De R$ 8.982,01 até R$ 9.980,00
<br>N: De R$ 9.980,01 até R$ 11.976,00
<br>O: De R$ 11.976,01 até R$ 14.970,00
<br>P: De R$ 14.970,01 até R$ 19.960,00
<br>Q: Mais de R$ 19.960,00"""
    elif Questao == 'Q007':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 7 no questionario socioeconômico:
                            <br><br>A: Não.
<br>B: Sim, um ou dois dias por semana.
<br>C: Sim, três ou quatro dias por semana.
<br>D: Sim, pelo menos cinco dias por semana."""
    elif Questao == 'Q008':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 8 no questionario socioeconômico:
                            <br>
                            <br>A: Não.
<br>B: Sim, um.
<br>C: Sim, dois.
<br>D: Sim, três.
<br>E: Sim, quatro ou mais."""
    elif Questao == 'Q009':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 9 no questionario socioeconômico:
                            <br><br>A: Não.
<br>B: Sim, um.
<br>C: Sim, dois.
<br>D: Sim, três.
<br>E: Sim, quatro ou mais."""
    elif Questao == 'Q010':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 10 no questionario socioeconômico:
                            <br><br>A: Não.
<br>B: Sim, um.
<br>C: Sim, dois.
<br>D: Sim, três.
<br>E: Sim, quatro ou mais."""
    elif Questao == 'Q011':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 11 no questionario socioeconômico:
                            <br><br>A: Não.
<br>B: Sim, um.
<br>C: Sim, dois.
<br>D: Sim, três.
<br>E: Sim, quatro ou mais."""
    elif Questao == 'Q012':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 12 no questionario socioeconômico:
                            <br><br>A: Não.
<br>B: Sim, um.
<br>C: Sim, dois.
<br>D: Sim, três.
<br>E: Sim, quatro ou mais."""
    elif Questao == 'Q013':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 13 no questionario socioeconômico:
                            <br><br>A: Não.
<br>B: Sim, um.
<br>C: Sim, dois.
<br>D: Sim, três.
<br>E: Sim, quatro ou mais."""
    elif Questao == 'Q014':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 14 no questionario socioeconômico:
                            <br><br>A: Não.
<br>B: Sim, um.
<br>C: Sim, dois.
<br>D: Sim, três.
<br>E: Sim, quatro ou mais."""
    elif Questao == 'Q015':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 15 no questionario socioeconômico:
                            <br><br>A: Não.
<br>B: Sim, um.
<br>C: Sim, dois.
<br>D: Sim, três.
<br>E: Sim, quatro ou mais."""
    elif Questao == 'Q016':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 16 no questionario socioeconômico:
                            <br><br>A: Não.
<br>B: Sim, um.
<br>C: Sim, dois.
<br>D: Sim, três.
<br>E: Sim, quatro ou mais."""
    elif Questao == 'Q017':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 17 no questionario socioeconômico:
                            <br><br>A: Não.
<br>B: Sim, um.
<br>C: Sim, dois.
<br>D: Sim, três.
<br>E: Sim, quatro ou mais."""
    elif Questao == 'Q018':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 18 no questionario socioeconômico:
                            <br><br>A: Sim.
<br>B Não."""
    elif Questao == 'Q019':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 19 no questionario socioeconômico:
                            <br><br>A: Não.
<br>B: Sim, um.
<br>C: Sim, dois.
<br>D: Sim, três.
<br>E: Sim, quatro ou mais."""
    elif Questao == 'Q020':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 20 no questionario socioeconômico:
                            <br><br>A: Sim.
<br>B Não."""
    elif Questao == 'Q021':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 21 no questionario socioeconômico:
                            <br><br>A: Sim.
<br>B Não."""
    elif Questao == 'Q022':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 22 no questionario socioeconômico:
                            <br><br>A: Não.
<br>B: Sim, um.
<br>C: Sim, dois.
<br>D: Sim, três.
<br>E: Sim, quatro ou mais."""
    elif Questao == 'Q023':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 23 no questionario socioeconômico:
                            <br><br>A: Sim.
<br>B Não."""
    elif Questao == 'Q024':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 24 no questionario socioeconômico:
                            <br><br>A: Não.
<br>B: Sim, um.
<br>C: Sim, dois.
<br>D: Sim, três.
<br>E: Sim, quatro ou mais."""
    elif Questao == 'Q025':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 25 no questionario socioeconômico:
                            <br><br>A: Sim.
<br>B Não."""

    annotations = [
        {
            'x': 0,
            'y': -0.8,
            'xref': "paper",
            'yref': "paper",
            'text': texto,
            'showarrow': False,
            'align': 'left',
            'font': {'family': "Arial", 'size': 13, 'color': "black"}
        }
    ]

    return annotations


def formulario_2(request):

    Q = 'TP_SEXO'
    prova = 'NU_NOTA_MT'

    if request.method == 'GET':    
          
        menssagem = "Análise do Desempenho Acadêmico de Pessoas com Deficiência e seus Dados Socioeconômicos:"          
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

        figura_com_criador_de_tabela = px.bar(Dataframe)
        figura_com_criador_de_tabela = figura_com_criador_de_tabela.to_html()
        
        figura_tabela_da_media = px.bar(Dataframe['mean'])
        figura_tabela_da_media = figura_tabela_da_media.to_html()
       
        # Crie um estilo CSS externo para estilizar a tabela
        # CSS_STYLE = """
        #     .table-header {
        #         background-color: royalblue;
        #         height: 30px;
        #         line-color: darkslategray;
        #         text-align: center;
        #         font-color: white;
        #         font-size: 12px;
        #     }
        #     .table-cell {
        #         line-color: darkslategray;
        #         text-align: center;
        #         height: 30px;
        #         font-color: darkslategray;
        #         font-size: 11px;
        #     }
        # """
        
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
            height=700,
            margin=dict(l=50, r=50, b=300, t=50),
            yaxis = {'domain': [0, .45]},
            xaxis2 = {'anchor': 'y2'},
            xaxis_title="Respota do questionário socioeconômico",
            yaxis_title="Desempenho",
            yaxis2 = {'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'},
            legend_title="Legenda",
            annotations=anotacao(Q),
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

        menssagem1 = """Formulário da análise do Desempenho do inscrito em relação aos dados socioêconomicos :"""
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
    
