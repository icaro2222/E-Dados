from django.shortcuts import render
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from io import BytesIO
import plotly.express as px
import base64
from edados.formularios.formulario_1.formulario_1 import Formulario_1
from edados.formularios.filtros.formulario_1_filtros import Formulario_filtros
import numpy as np
from edados.database import bd_formulario_1

CONTAGEM = 0
CONTAGEMMicrodado_Amostra = 3702008

def formatar(valor):
    return "{:,.2f}".format(valor)

def formatarContagem(valor):
    valor = CONTAGEM
    return "{:,.2f}".format(valor)

def formatarFrequencia(valor):
    valor =  (valor/CONTAGEM)*100
    return "{:,.4f}%".format(valor)

def formatarFrequenciaSemPorcentagem(valor):
    valor =  (valor/CONTAGEM)*100
    return "{:,.4f}".format(valor)

def formatarFrequenciaAbsoluta(valor):
    valor =  (valor/CONTAGEMMicrodado_Amostra)*100
    return "{:,.6f}%".format(valor)

def formulario_1(request):

    global CONTAGEM
    global CONTAGEMMicrodado_Amostra
    
    questao = 'Q001'
    demografico = 'TP_SEXO'

    if request.method == 'GET':
        menssagem = 'Análise de Dados Socioeconômicos do ENEM'
        menssagem1 = """Este formulário permite realizar uma análise exploratória que correlaciona os microdados socioeconômicos e demográficos do ENEM nos anos de 2016, 2017, 2018 e 2019. 
        É possível obter resultados em porcentagem, o que possibilita a comparação entre os anos estudados."""

        form = Formulario_1()
        form_filtro = Formulario_filtros()
        context = {
            'form': form,
            'menssagem': menssagem,
            'menssagem1': menssagem1,
            'form_filtro': form_filtro
        }
        return render(request, 'base/formulario_1/quest_formulario_1.html', context=context)
    else:

        # Recebendo fomulario da tela
        form = Formulario_1(request.POST)
        form_filtro = Formulario_filtros(request.POST)

        # Variáveis vindas do Formulario
        questao = form.data['questao']
        demografico = form.data['demografico']
        filtro_deficiencia = form.data['deficiencia']

        # Formulario de Filtro
        # Formulario de Filtro
        filtro_deficiencia = form_filtro.data['deficiencia']
        filtro_estado_civil = form_filtro.data['estado_civil']
        filtro_cor = form_filtro.data['cor']
        filtro_sexo = form_filtro.data['sexo']
        filtro_ano = form_filtro.data['ano']
        filtro_escola = form_filtro.data['escola']
        filtro_nacionalidade = form_filtro.data['nacionalidade']
        filtro_estado = form_filtro.data['estado']
        filtro_amostra = form_filtro.data['amostra']
        filtro_recurso = form_filtro.data['recurso']
        filtro_localizacao_da_escola = form_filtro.data['localizacao_da_escola']

        Amostra = [demografico, questao]
        if demografico != 'TP_SEXO' and filtro_sexo != 'todos':
            Amostra.append('TP_SEXO')
            
        Microdado_Amostra = bd_formulario_1.buscar_dataframe_no_banco(
            Amostra, 
            filtro_sexo=filtro_sexo, 
            filtro_amostra=filtro_amostra, 
            filtro_deficiencia=filtro_deficiencia,
            filtro_cor=filtro_cor, 
            filtro_estado=filtro_estado, 
            filtro_recurso=filtro_recurso, 
            filtro_questao=questao, 
            filtro_localizacao_da_escola=filtro_localizacao_da_escola, 
            filtro_estado_civil=filtro_estado_civil, 
            filtro_escola=filtro_escola, 
            filtro_nacionalidade=filtro_nacionalidade,
            filtro_ano=filtro_ano)
            

        CONTAGEM  = Microdado_Amostra[questao].count()
        print('---------------------------------------------')
        print(CONTAGEM)
        menssagem = 'Análise de Dados Socioeconômicos do ENEM'
        relatorio_em_grafico = ''

        if (demografico == 'TP_SEXO'):

            if (filtro_sexo == 'todos'):
                vetor = demografico_sexo(
                    Microdado_Amostra, demografico, questao)
                relatorio = vetor[0]
                relatorio_em_grafico = vetor[1]
            else:
                vetor = demografico_sexo_unilateral(
                    Microdado_Amostra, demografico, questao, filtro_sexo)
                relatorio = vetor[0]

        elif (demografico == 'TP_ESTADO_CIVIL'):
            vetor = demografico_estado_civil(
                Microdado_Amostra, demografico, questao, filtro_ano)
            relatorio = vetor[0]
            relatorio_em_grafico = vetor[1]

        elif (demografico == 'TP_COR_RACA'):
            vetor = demografico_raca(Microdado_Amostra, demografico, questao)
            relatorio = vetor[0]

        elif (demografico == 'TP_NACIONALIDADE'):
            vetor = demografico_nascionalidade(
                Microdado_Amostra, demografico, questao)
            relatorio = vetor[0]

        elif (demografico == 'TP_ESCOLA'):
            vetor = demografico_escolaridade(
                Microdado_Amostra, demografico, questao)
            relatorio = vetor[0]

        elif (demografico == 'TP_ENSINO'):
            vetor = demografico_instituicao_aonde_conclui_ensino_medio(
                Microdado_Amostra, demografico, questao)
            relatorio = vetor[0]

        elif (demografico == 'TP_ANO_CONCLUIU'):
            vetor = demografico_ano_de_conclusao(
                Microdado_Amostra, demografico, questao, filtro_ano=filtro_ano)
            relatorio = vetor[0]

        context = {
            'form': form,
            'form_filtro': form_filtro,
            'menssagem': menssagem,
            'relatorio': relatorio,
            'quantidadeParcial' : CONTAGEM,
            'quantidadeTotal' : CONTAGEMMicrodado_Amostra,
            'relatorio_em_grafico': relatorio_em_grafico
        }

    return render(request, 'base/formulario_1/relatorio_formulario_1.html', context=context)


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
<br>pescador, lenhador, seringueiro, extrativista.
                            <br>Grupo 2: Diarista, empregado doméstico, cuidador de idosos, babá, cozinheiro (em casas particulares), motorista particular, jardineiro, f
<br>axineiro de empresas e prédios, vigilante, porteiro, carteiro, office-boy, vendedor, caixa, atendente de loja, auxiliar administrativo, recepcionista, servente de pedreiro, repositor de mercadoria.
                            <br>Grupo 3: Padeiro, cozinheiro industrial ou em restaurantes, sapateiro, costureiro, joalheiro, torneiro mecânico, operador de máquinas, 
<br>soldador, operário de fábrica, trabalhador da mineração, pedreiro, pintor, eletricista, encanador, motorista, caminhoneiro, taxista.
                            <br>Grupo 4: Professor (de ensino fundamental ou médio, idioma, música, artes etc.), técnico (de enfermagem, contabilidade, eletrônica etc.), 
<br>policial, militar de baixa patente (soldado, cabo, sargento), corretor de imóveis, supervisor, gerente, mestre de obras, pastor, microempresário (proprietário de
<br>empresa com menos de 10 empregados), pequeno comerciante, pequeno proprietário de terras, trabalhador autônomo ou por conta própria.
                            <br>Grupo 5: Médico, engenheiro, dentista, psicólogo, economista, advogado, juiz, promotor, defensor, delegado, tenente, capitão, coronel,
<br>professor universitário, diretor em empresas públicas ou privadas, político, proprietário de empresas com mais de 10 empregados.
                            <br>Não sei.."""
    elif Questao == 'Q004':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 4 no questionario socioeconômico:
                            <br>
                            <br>Grupo 1: Lavradora, agricultora sem empregados, bóia fria, criadora de animais (gado, porcos, galinhas, ovelhas,
<br>cavalos etc.), apicultora, pescadora, lenhadora, seringueira, extrativista.
<br>Grupo 2: Diarista, empregada doméstica, cuidadora de idosos, babá, cozinheira (em casas particulares), motorista particular, jardineira, 
<br>faxineira de empresas e prédios, vigilante, porteira, carteira, office-boy, vendedora, caixa, atendente de loja, auxiliar administrativa, recepcionista, servente de pedreiro, repositora de mercadoria.
<br>Grupo 3: Padeira, cozinheira industrial ou em restaurantes, sapateira, costureira, joalheira, torneira mecânica, operadora de máquinas, 
<br>soldadora, operária de fábrica, trabalhadora da mineração, pedreira, pintora, eletricista, encanadora, motorista, caminhoneira, taxista.
<br>Grupo 4: Professora (de ensino fundamental ou médio, idioma, música, artes etc.), técnica (de enfermagem, contabilidade, eletrônica etc.), 
<br>policial, militar de baixa patente (soldado, cabo, sargento), corretora de imóveis, supervisora, gerente, mestre de obras, pastora,
<br>microempresária (proprietária de empresa com menos de 10 empregados), pequena comerciante, pequena proprietária de terras, trabalhadora autônoma ou por conta própria.
<br>Grupo 5: Médica, engenheira, dentista, psicóloga, economista, advogada, juíza, promotora, defensora, delegada, tenente, capitã, coronel,
<br>professora universitária, diretora em empresas públicas ou privadas, política, proprietária de empresas com mais de 10 empregados.
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

def demografico_sexo(Microdado_Amostra, demografico, questao):

    DataFrame = Microdado_Amostra.sort_values(by=[questao])
    DataFrame = DataFrame.groupby([demografico, questao])
    DataFrame = DataFrame[demografico].count()

    # rotacionar
    DataFrame = DataFrame.unstack()
    DataFrame_para_criar_a_grafico = DataFrame

    lista_dos_index = DataFrame.index.to_list()

    # desrotacionar
    DataFrame = DataFrame.stack()

    QUNATIDADE_TOTAL = 1000
    fig = go.Figure()
    texttemplate = '%{text:.1f}%',
    textposition = 'auto'
    print(CONTAGEM)
    print('++++++++++++++++++++++++++++++++++++++')

    for index in lista_dos_index:
        if index == 'F':
            nome = 'feminino'
        else:
            nome = 'masculino'
        fig.add_bar(
            y=((DataFrame[index]/CONTAGEM)*100),
            x=DataFrame[index].index,
            text=((DataFrame[index]/CONTAGEM)*100),
            texttemplate='%{text:.2f}%',
            textposition='auto',
            name=nome
        )
    print('----------------------------------------------')
    print(DataFrame.index.names[1])

    fig.update_layout(
        title_text='Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
        height=700,
        margin=dict(l=50, r=50, b=300, t=50),
        xaxis_title="Resposta do questionário socioeconômico",
        yaxis_title="Quantidade",
        legend_title="Legenda",
        annotations=anotacao(DataFrame.index.names[1]),
        font=dict(
            family="Arial",
            size=12,
            color="black"
        )
    )

    relatorio_em_grafico = px.bar(
        DataFrame_para_criar_a_grafico,
        barmode='group',
        text_auto=True)

    relatorio_em_grafico.update_layout(
        title_text='Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
        height=700,
        margin=dict(l=50, r=50, b=300, t=50),
        xaxis_title="Resposta do questionário socioeconômico por sexo.",
        yaxis_title="Quantidade",
        legend_title="Legenda",
        annotations=anotacao(DataFrame.index.names[1]),
        font={'family': "Arial", 'size': 12, 'color': "black"}
    )

    relatorio_em_grafico = relatorio_em_grafico.to_html()

    relatorio = fig.to_html()

    return [relatorio, relatorio_em_grafico]

def demografico_sexo_unilateral(Microdado_Amostra, demografico, questao, filtro_sexo):

    DataFrame = Microdado_Amostra.sort_values(by=[questao])
    DataFrame = DataFrame.groupby([demografico, questao])
    DataFrame = DataFrame[demografico].count()

    # rotacionar
    DataFrame = DataFrame.unstack()

    lista_dos_index = DataFrame.index.to_list()

    # desrotacionar
    DataFrame = DataFrame.stack()

    fig = go.Figure()

    if (DataFrame.count() > 0):
        if filtro_sexo == 'M':
            nome = 'masculino'
            fig.add_bar(
            y=((DataFrame[filtro_sexo]/CONTAGEM)*100),
            x=DataFrame[filtro_sexo].index,
            text=((DataFrame[filtro_sexo]/CONTAGEM)*100),
                texttemplate='%{text:.2f}%',
                textposition='auto',
                name=nome
            )
        else:
            nome = 'feminino'
            fig.add_bar(
            y=((DataFrame[filtro_sexo]/CONTAGEM)*100),
            x=DataFrame[filtro_sexo].index,
            text=((DataFrame[filtro_sexo]/CONTAGEM)*100),
                texttemplate='%{text:.2f}%',
                textposition='auto',
                name=nome
            )

    fig.update_layout(
        title_text='Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
        height=700,
        margin=dict(l=50, r=50, b=300, t=50),
        xaxis_title="Resposta do questionário socioeconômico.",
        yaxis_title="Quantidade",
        legend_title="Legenda",
        annotations=anotacao(DataFrame.index.names[1]),
        font=dict(
            family="Arial",
            size=12,
            color="black"
        )
    )
    relatorio = fig.to_html()

    return [relatorio]

def demografico_estado_civil(Microdado_Amostra, demografico, questao, filtro_ano):

    DataFrame = Microdado_Amostra.sort_values(by=[questao])
    DataFrame = DataFrame.groupby([demografico, questao])
    DataFrame = DataFrame[demografico].count()

    # rotacionar
    DataFrame = DataFrame.unstack()
    DataFrame_para_criar_a_grafico = DataFrame

    lista_dos_index = DataFrame.index.to_list()

    # desrotacionar
    DataFrame = DataFrame.stack()

    fig = go.Figure()

    for index in lista_dos_index:
        print(filtro_ano)
        if filtro_ano == '2019':
            if (index == '0' or index == 0):
                nome = 'Não informou'
            elif (index == '1' or index == 1):
                nome = 'Solteiro(a)'
            elif (index == '2' or index == 2):
                nome = 'Casado(a)'
            elif (index == '3' or index == 3):
                nome = 'Divorciado(a)'
            else:
                nome = 'Viúvo(a)'
        else:
            if (index == '0' or index == 0):
                nome = 'Solteiro(a)'
            elif (index == '1' or index == 1):
                nome = 'Casado(a)'
            elif (index == '2' or index == 2):
                nome = 'Divorciado(a)'
            elif (index == '3' or index == 3):
                nome = 'Viúvo(a)'
            else:
                nome = 'Não informou'

        fig.add_bar(
            y=((DataFrame[index]/CONTAGEM)*100),
            x=DataFrame[index].index,
            text=((DataFrame[index]/CONTAGEM)*100),
                texttemplate='%{text:.2f}%',
                textposition='auto',
                name=nome
            )


    fig.update_layout(
        title_text='Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
        height=700,
        margin=dict(l=50, r=50, b=300, t=50),
        xaxis_title="Resposta do questionário socioeconômico",
        yaxis_title="Quantidade",
        legend_title="Legenda",
        annotations=anotacao(DataFrame.index.names[1]),
        font=dict(
            family="Arial",
            size=12,
            color="black"
        )
    )
    relatorio_em_grafico = px.bar(
        DataFrame_para_criar_a_grafico, barmode='group')

    relatorio_em_grafico.update_layout(
        title_text='Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
        height=700,
        margin=dict(l=50, r=50, b=300, t=50),
        xaxis_title="Resposta do questionário socioeconômico",
        yaxis_title="Quantidade",
        legend_title="Legenda",
        annotations=anotacao(DataFrame.index.names[1]),
        font=dict(
            family="Arial",
            size=12,
            color="black"
        )
    )
    relatorio_em_grafico = relatorio_em_grafico.to_html()

    relatorio = fig.to_html()

    return [relatorio, relatorio_em_grafico]

def demografico_raca(Microdado_Amostra, demografico, questao):

    DataFrame = Microdado_Amostra.sort_values(by=[questao])
    DataFrame = DataFrame.groupby([demografico, questao])
    DataFrame = DataFrame[demografico].count()

    # DataFrame = Microdado_Amostra.sort_values(by=questao)
    # DataFrame = DataFrame.groupby([demografico, questao])[demografico].count()

    # rotacionar
    DataFrame = DataFrame.unstack()

    # Pegando lista de index pra usá-los posteriomente.
    lista_dos_index = DataFrame.index.to_list()

    # desrotacionar
    DataFrame = DataFrame.stack()

    fig = go.Figure()

    for index in lista_dos_index:

        if (index == '0' or index == 0):
            nome = 'Não informou'
        elif (index == '1' or index == 1):
            nome = 'Branca'
        elif (index == '2' or index == 2):
            nome = 'Preta'
        elif (index == '3' or index == 3):
            nome = 'Parda'
        elif (index == '4' or index == 4):
            nome = 'Amarela'
        else:
            nome = 'Indígena'

        fig.add_bar(
            y=((DataFrame[index]/CONTAGEM)*100),
            x=DataFrame[index].index,
            text=((DataFrame[index]/CONTAGEM)*100),
                texttemplate='%{text:.2f}%',
                textposition='auto',
                name=nome
            )

    fig.update_layout(
        title_text='Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
        height=700,
        margin=dict(l=50, r=50, b=300, t=50),
        xaxis_title="Resposta do questionário socioeconômico",
        yaxis_title="Quantidade",
        legend_title="Legenda",
        annotations=anotacao(DataFrame.index.names[1]),
        font=dict(
            family="Arial",
            size=12,
            color="black"
        )
    )

    relatorio = fig.to_html()

    return [relatorio]

def demografico_nascionalidade(Microdado_Amostra, demografico, questao):

    DataFrame = Microdado_Amostra.sort_values(by=[questao])
    DataFrame = DataFrame.groupby([demografico, questao])
    DataFrame = DataFrame[demografico].count()

    # rotacionar
    DataFrame = DataFrame.unstack()

    lista_dos_index = DataFrame.index.to_list()
    print(lista_dos_index)

    # desrotacionar
    DataFrame = DataFrame.stack()

    fig = go.Figure()

    for index in lista_dos_index:
        print(index)
        if (index == '0' or index == 0):
            nome = 'Não informou'
        elif (index == '1' or index == 1):
            nome = 'Brasileiro(a)'
        elif (index == '2' or index == 2):
            nome = 'Naturalizado(a)'
        elif (index == '3' or index == 3):
            nome = 'Estrangeiro(a)'
        else:
            nome = 'Brasileiro(a) Nato(a), nascido(a) no exterior'

        fig.add_bar(
            y=((DataFrame[index]/CONTAGEM)*100),
            x=DataFrame[index].index,
            text=((DataFrame[index]/CONTAGEM)*100),
                texttemplate='%{text:.2f}%',
                textposition='auto',
                name=nome
            )

    fig.update_layout(
        title_text='Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
        height=700,
        margin=dict(l=50, r=50, b=300, t=50),
        xaxis_title="Resposta do questionário socioeconômico",
        yaxis_title="Quantidade",
        legend_title="Legenda",
        annotations=anotacao(DataFrame.index.names[1]),
        font=dict(
            family="Arial",
            size=12,
            color="black"
        ),
        # margin = {'t':75, 'l':50},
        # yaxis = {'domain': [0, .45]},
        # xaxis2 = {'anchor': 'y2'},
        # yaxis2 = {'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'}
    )

    relatorio = fig.to_html()

    return [relatorio]

def demografico_escolaridade(Microdado_Amostra, demografico, questao):

    DataFrame = Microdado_Amostra.sort_values(by=[questao])
    DataFrame = DataFrame.groupby([demografico, questao])
    DataFrame = DataFrame[demografico].count()

    # rotacionar
    DataFrame = DataFrame.unstack()

    lista_dos_index = DataFrame.index.to_list()
    print(lista_dos_index)

    # desrotacionar
    DataFrame = DataFrame.stack()

    fig = go.Figure()

    for index in lista_dos_index:
        print(index)
        if (index == '0' or index == 0):
            nome = 'Não informou'
        elif (index == '1' or index == 1):
            nome = 'Pública'
        elif (index == '2' or index == 2):
            nome = 'Privada'
        else:
            nome = 'Exterior'

        fig.add_bar(
            y=((DataFrame[index]/CONTAGEM)*100),
            x=DataFrame[index].index,
            text=((DataFrame[index]/CONTAGEM)*100),
                texttemplate='%{text:.2f}%',
                textposition='auto',
                name=nome
            )

    fig.update_layout(
        title_text='Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
        height=700,
        margin=dict(l=50, r=50, b=300, t=50),
        xaxis_title="Resposta do questionário socioeconômico",
        yaxis_title="Quantidade",
        legend_title="Legenda",
        annotations=anotacao(DataFrame.index.names[1]),
        font=dict(
            family="Arial",
            size=12,
            color="black"
        )
    )

    relatorio = fig.to_html()

    return [relatorio]

def demografico_conclusao_ensino_medio(Microdado_Amostra, demografico, questao):

    DataFrame = Microdado_Amostra.sort_values(by=[questao])
    DataFrame = DataFrame.groupby([demografico, questao])
    DataFrame = DataFrame[demografico].count()

    # rotacionar
    DataFrame = DataFrame.unstack()

    lista_dos_index = DataFrame.index.to_list()
    print(lista_dos_index)

    # desrotacionar
    DataFrame = DataFrame.stack()

    fig = go.Figure()

    for index in lista_dos_index:
        print('INDEX= '+index)
        if (index == '0' or index == 0):
            nome = 'Não informou'
        elif (index == '1' or index == 1):
            nome = 'Pública'
        elif (index == '2' or index == 2):
            nome = 'Privada'
        else:
            nome = 'Exterior'

        fig.add_bar(
            y=((DataFrame[index]/CONTAGEM)*100),
            x=DataFrame[index].index,
            text=((DataFrame[index]/CONTAGEM)*100),
                texttemplate='%{text:.2f}%',
                textposition='auto',
                name=nome
            )

    fig.update_layout(
        title_text='Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
        height=700,
        margin=dict(l=50, r=50, b=300, t=50),
        xaxis_title="Resposta do questionário socioeconômico",
        yaxis_title="Quantidade",
        legend_title="Legenda",
        annotations=anotacao(DataFrame.index.names[1]),
        font=dict(
            family="Arial",
            size=12,
            color="black"
        )
    )

    relatorio = fig.to_html()

    return [relatorio]

def demografico_ano_de_conclusao(Microdado_Amostra, demografico, questao, filtro_ano):

    DataFrame = Microdado_Amostra.sort_values(by=[questao])
    DataFrame = DataFrame.groupby([demografico, questao])
    DataFrame = DataFrame[demografico].count()

    # rotacionar
    DataFrame = DataFrame.unstack()

    lista_dos_index = DataFrame.index.to_list()
    print(lista_dos_index)

    # desrotacionar
    DataFrame = DataFrame.stack()

    fig = go.Figure()

    for index in lista_dos_index:

        if filtro_ano == '2019':
            print(2019)
            if (index == '0' or index == 0):
                nome = 'Não informou'
            elif (index == '1' or index == 1):
                nome = '2018'
            elif (index == '2' or index == 2):
                nome = '2017'
            elif (index == '3' or index == 3):
                nome = '2016'
            elif (index == '4' or index == 4):
                nome = '2015'
            elif (index == '5' or index == 5):
                nome = '2014'
            elif (index == '6' or index == 6):
                nome = '2013'
            elif (index == '7' or index == 7):
                nome = '2012'
            elif (index == '8' or index == 8):
                nome = '2011'
            elif (index == '9' or index == 9):
                nome = '2010'
            elif (index == '10' or index == 10):
                nome = '2009'
            elif (index == '11' or index == 11):
                nome = '2008'
            elif (index == '12' or index == 12):
                nome = '2007'
            else:
                nome = 'Antes de 2007'
        elif filtro_ano == '2018':
            print(2018)
            if (index == '0' or index == 0):
                nome = 'Não informou'
            elif (index == '1' or index == 1):
                nome = '2017'
            elif (index == '2' or index == 2):
                nome = '2016'
            elif (index == '3' or index == 3):
                nome = '2015'
            elif (index == '4' or index == 4):
                nome = '2014'
            elif (index == '5' or index == 5):
                nome = '2013'
            elif (index == '6' or index == 6):
                nome = '2012'
            elif (index == '7' or index == 7):
                nome = '2011'
            elif (index == '8' or index == 8):
                nome = '2010'
            elif (index == '9' or index == 9):
                nome = '2009'
            elif (index == '10' or index == 10):
                nome = '2008'
            elif (index == '11' or index == 11):
                nome = '2007'
            else:
                nome = 'Antes de 2007'

        fig.add_bar(
            y=((DataFrame[index]/CONTAGEM)*100),
            x=DataFrame[index].index,
            text=((DataFrame[index]/CONTAGEM)*100),
                texttemplate='%{text:.2f}%',
                textposition='auto',
                name=nome
            )

    fig.update_layout(
        title_text='Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
        height=700,
        margin=dict(l=50, r=50, b=300, t=50),
        xaxis_title="Resposta do questionário socioeconômico",
        yaxis_title="Quantidade",
        legend_title="Legenda",
        annotations=anotacao(DataFrame.index.names[1]),
        font=dict(
            family="Arial",
            size=12,
            color="black"
        )
    )

    relatorio = fig.to_html()

    return [relatorio]

def demografico_instituicao_aonde_conclui_ensino_medio(Microdado_Amostra, demografico, questao):

    DataFrame = Microdado_Amostra.sort_values(by=[questao])
    DataFrame = DataFrame.groupby([demografico, questao])
    DataFrame = DataFrame[demografico].count()

    # rotacionar
    DataFrame = DataFrame.unstack()

    lista_dos_index = DataFrame.index.to_list()
    print(lista_dos_index)

    # desrotacionar
    DataFrame = DataFrame.stack()

    fig = go.Figure()

    for index in lista_dos_index:
        print(index)
        if (index == '0' or index == 0):
            nome = 'Não informou'
        elif (index == '1' or index == 1):
            nome = 'Pública'
        elif (index == '2' or index == 2):
            nome = 'Privada'
        else:
            nome = 'Exterior'

        fig.add_bar(
            y=((DataFrame[index]/CONTAGEM)*100),
            x=DataFrame[index].index,
            text=((DataFrame[index]/CONTAGEM)*100),
                texttemplate='%{text:.2f}%',
                textposition='auto',
                name=nome
            )

    fig.update_layout(
        title_text='Gráfico de correlação entre a resposta da questão socioeconômica e a questão demográfica.',
        height=700,
        margin=dict(l=50, r=50, b=300, t=50),
        xaxis_title="Resposta do questionário socioeconômico",
        yaxis_title="Desempenho",
        legend_title="Legenda",
        annotations=anotacao(DataFrame.index.names[1]),
        font=dict(
            family="Arial",
            size=12,
            color="black"
        )
    )

    relatorio = fig.to_html()

    return [relatorio]
