from django.shortcuts import render
import plotly.graph_objects as go
from edados.formularios.formulario_1.formulario_1_4 import Formulario
from edados.formularios.filtros.formulario_1_filtros import Formulario_filtros
from edados.database import bd_formulario_1_4
import numpy as np 
import pandas as pd
import time
import csv
from django.http import HttpResponse

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
<br> pescador, lenhador, seringueiro, extrativista.
                            <br>Grupo 2: Diarista, empregado doméstico, cuidador de idosos, babá, cozinheiro (em casas particulares), motorista particular, jardineiro, f
<br>axineiro de empresas e prédios, vigilante, porteiro, carteiro, office-boy, vendedor, caixa, atendente de loja, auxiliar administrativo, recepcionista, servente de pedreiro, repositor de mercadoria.
                            <br>Grupo 3: Padeiro, cozinheiro industrial ou em restaurantes, sapateiro, costureiro, joalheiro, torneiro mecânico, operador de máquinas, 
<br>soldador, operário de fábrica, trabalhador da mineração, pedreiro, pintor, eletricista, encanador, motorista, caminhoneiro, taxista.
                            <br>Grupo 4: Professor (de ensino fundamental ou médio, idioma, música, artes etc.), técnico (de enfermagem, contabilidade, eletrônica etc.), 
<br>policial, militar de baixa patente (soldado, cabo, sargento), corretor de imóveis, supervisor, gerente, mestre de obras, pastor, microempresário (proprietário de
<br> empresa com menos de 10 empregados), pequeno comerciante, pequeno proprietário de terras, trabalhador autônomo ou por conta própria.
                            <br>Grupo 5: Médico, engenheiro, dentista, psicólogo, economista, advogado, juiz, promotor, defensor, delegado, tenente, capitão, coronel,
<br> professor universitário, diretor em empresas públicas ou privadas, político, proprietário de empresas com mais de 10 empregados.
                            <br>Não sei.."""
    elif Questao == 'Q004':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 4 no questionario socioeconômico:
                            <br>
                            <br>Grupo 1: Lavradora, agricultora sem empregados, bóia fria, criadora de animais (gado, porcos, galinhas, ovelhas,
<br> cavalos etc.), apicultora, pescadora, lenhadora, seringueira, extrativista.
<br>Grupo 2: Diarista, empregada doméstica, cuidadora de idosos, babá, cozinheira (em casas particulares), motorista particular, jardineira, 
<br>faxineira de empresas e prédios, vigilante, porteira, carteira, office-boy, vendedora, caixa, atendente de loja, auxiliar administrativa, recepcionista, servente de pedreiro, repositora de mercadoria.
<br>Grupo 3: Padeira, cozinheira industrial ou em restaurantes, sapateira, costureira, joalheira, torneira mecânica, operadora de máquinas, 
<br>soldadora, operária de fábrica, trabalhadora da mineração, pedreira, pintora, eletricista, encanadora, motorista, caminhoneira, taxista.
<br>Grupo 4: Professora (de ensino fundamental ou médio, idioma, música, artes etc.), técnica (de enfermagem, contabilidade, eletrônica etc.), 
<br>policial, militar de baixa patente (soldado, cabo, sargento), corretora de imóveis, supervisora, gerente, mestre de obras, pastora,
<br> microempresária (proprietária de empresa com menos de 10 empregados), pequena comerciante, pequena proprietária de terras, trabalhadora autônoma ou por conta própria.
<br>Grupo 5: Médica, engenheira, dentista, psicóloga, economista, advogada, juíza, promotora, defensora, delegada, tenente, capitã, coronel,
<br> professora universitária, diretora em empresas públicas ou privadas, política, proprietária de empresas com mais de 10 empregados.
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


    texto = """INFORMATIVO:
                                <br>Nesta tela, é possível realizar tanto o somatório dos dados, com a visualização dos percentuais parcial e absoluto, 
                                <br>quanto a análise comparativa entre a filtragem de dados e as respostas do questionário socioeconômico; 
                                <br><br>O percentual parcial: se refere à porcentagem de inscritos que se enquadram nas diferentes respostas do questionário socioeconômico. 
                                <br>Essa análise é feita após a realização da filtragem e o somatório desses percentuais resulta em 100%, 
                                <br>considerando todos os inscritos que passaram pelos filtros selecionados na tela de análise de dados; 
                                <br>Percentual absoluto: é o percentual de inscritos no Enem que foram filtrados em comparação com o total de todos os alunos inscritos, sem qualquer filtro aplicado; 
                                <br><br>Somatório dos inscritos que responderam: Corresponde ao somatório de todos inscritos após a filtragem nos filtros acima; 
                                
                                <br>""" + texto

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

    
def formulario_4(request):

    # Medindo o tempo que a view demora para executar
    tempo_inicial = time.time()

    global CONTAGEM
    global CONTAGEMMicrodado_Amostra

    questao= 'Q001'
    demografico = 'TP_SEXO'

    if request.method == 'GET':        
        menssagem = ("Análise de Dados Socioeconômicos do ENEM")
        menssagem1 = """Esta é uma tela web que permite realizar o somatório dos alunos que responderam ao ENEM. Esta tela também possui filtros que permitem reduzir o somatório para fins de análise dos microdados. O resultado desse somatório é obtido após a aplicação desses filtros."""

        form = Formulario()
        form_filtro = Formulario_filtros()
        context = {
            'form' : form,
            'menssagem' : menssagem,
            'menssagem1' : menssagem1,
            'form_filtro' : form_filtro
        }
        return render(request, 'base/formulario_1/quest_formulario_4.html', context=context)
    elif request.POST.get('button')!='baixar_csv_completo':
        
        print(request.POST.get('button'))
        print('000000000000000000000000000000000000000000000000000000000')
        # Recebendo fomulario da tela
        form = Formulario(request.POST)
        form_filtro = Formulario_filtros(request.POST)

        # Variáveis vindas do Formulario
        filtro_questao = form.data['questao']

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
        
        # filtros sendo desenvolvidos
        filtro_ltp_adm_escola = form_filtro.data['tp_adm_escola']
        filtro_ano_de_conclusao = form_filtro.data['ano_de_conclusao']
        
        Amostra = [demografico, questao]
        Microdado_Amostra = bd_formulario_1_4.buscar_dataframe_no_banco(
            Amostra, 
            filtro_sexo=filtro_sexo, 
            filtro_recurso=filtro_recurso,             
            filtro_ltp_adm_escola=filtro_ltp_adm_escola,            
            filtro_ano_de_conclusao=filtro_ano_de_conclusao,             
            filtro_localizacao_da_escola=filtro_localizacao_da_escola, 
            filtro_amostra=filtro_amostra, 
            filtro_estado=filtro_estado, 
            filtro_questao=filtro_questao, 
            filtro_deficiencia=filtro_deficiencia, 
            filtro_ano=filtro_ano, 
            filtro_cor=filtro_cor, 
            filtro_estado_civil=filtro_estado_civil, 
            filtro_escola=filtro_escola, 
            filtro_nacionalidade=filtro_nacionalidade)
        
        relatorio_dados_brutos = Microdado_Amostra.to_html(
            max_rows=10, justify='center', 
            classes="""table table-striped table-bordered table-sm
            text-dark"""
            )
        
        if filtro_questao == 'nenhum':
            Dataframe = Microdado_Amostra
            print('--------------------------------------------------------------------')
            print(Dataframe) 
            print('--------------------------------------------------------------------')
            Dataframe = Dataframe.describe().T
        else:
            Dataframe = Microdado_Amostra.groupby(filtro_questao)['NU_IDADE']       
            Dataframe = Dataframe.describe()    

        # print(Dataframe.count().count)

        if Dataframe.empty:

            CONTAGEM = 0
            menssagem = """Nenhum dos inscritos com essas características!"""
            context = {
                'form' : form,
                'form_filtro' : form_filtro,
                'menssagem' : menssagem,
                'quantidadeParcial' : CONTAGEM,
                'quantidadeTotal' : CONTAGEMMicrodado_Amostra,
            }
            return render(request, 'base/formulario_1/relatorio_formulario_4.html', context=context)

        rowEvenColor = 'lightgrey'
        rowOddColor = 'white'

        print("contage = " + str(CONTAGEM))
        print("contage = " + str(CONTAGEMMicrodado_Amostra))
        

        if filtro_questao == 'nenhum':
            CONTAGEM  = Dataframe['count']['NU_IDADE']
            figura_tabela = go.Figure(data=[go.Table(
                    header=dict(
                        values=['Quantidade de inscritos', 'Porcentagem parcial', 'Porcentagem absoluta'],
                        fill_color='royalblue',
                        height=40,
                        line_color='darkslategray',
                        align=['left','center'],
                        font=dict(color='white', size=12)
                    ),
                    cells=dict(
                        values=[Dataframe['count'][0:1], 
                                Dataframe['count'].apply(formatarFrequencia)[0:1],
                                Dataframe['count'].apply(formatarFrequenciaAbsoluta)[0:1]],
                        line_color='darkslategray',
                        fill_color = [[rowOddColor,rowEvenColor,rowOddColor]],
                        align = ['left', 'center'],
                        font = dict(color = 'darkslategray', size = 11)
                        ))
                    ])

        else:
            CONTAGEM = Dataframe['count'].sum()
            figura_tabela = go.Figure(data=[go.Table(
                    header=dict(
                        values=['Respostas', 'quant alunos', 'porcentagem parcial', 'porcentagem absoluta'],
                        fill_color='royalblue',
                        height=40,
                        line_color='darkslategray',
                        align=['left','center'],
                        font=dict(color='white', size=12)
                    ),
                    cells=dict(
                        values=[Dataframe.index,
                        Dataframe['count'],
                        Dataframe['count'].apply(formatarFrequencia),
                        Dataframe['count'].apply(formatarFrequenciaAbsoluta)],
                        line_color='darkslategray',
                        fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
                        align = ['left', 'center'],
                        font = dict(color = 'darkslategray', size = 11)
                        ))
                    ])
        
        if filtro_questao == 'nenhum':
            figura_tabela.update_layout(
                title_text = """Quadro de contagem das respostas das questões socioeconômicas.""",
                height = 500,
                margin = {'t':75, 'l':50},
                yaxis = {'domain': [0, .45]},
                xaxis2 = {'anchor': 'y2'},
                xaxis_title="Resposta do questionário socioeconômico",
                yaxis_title="Porcentagem",
                yaxis2 = {'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'},
                legend_title="Legenda",
                annotations=[
                    {
                        'x': 0,
                        'y': 0.7,
                        'xref': "paper",
                        'yref': "paper",
                        'text': """INFORMATIVO:
                                <br>Nesta tela, é possível realizar tanto o somatório dos dados, com a visualização dos percentuais parcial e absoluto, 
                                <br>quanto a análise comparativa entre a filtragem de dados e as respostas do questionário socioeconômico; 
                                <br><br>O percentual parcial: se refere à porcentagem de inscritos que se enquadram nas diferentes respostas do questionário socioeconômico. 
                                <br>Essa análise é feita após a realização da filtragem e o somatório desses percentuais resulta em 100%, 
                                <br>considerando todos os inscritos que passaram pelos filtros selecionados na tela de análise de dados; 
                                <br>Percentual absoluto: é o percentual de inscritos no Enem que foram filtrados em comparação com o total de todos os alunos inscritos, sem qualquer filtro aplicado; 
                                <br><br>Somatório dos inscritos que responderam: Corresponde ao somatório de todos os inscritos após a filtragem nos filtros acima; 
                                """,
                        'showarrow': False,
                        'align': 'left',
                        'font': {'family': "Arial", 'size': 13, 'color': "black"}
                    }
                ],
                font=dict(
                    family="Arial",
                    size=12,
                    color="black"
                )
            )
        else:
            figura_tabela.update_layout(
                title_text = """Quadro de contagem das respostas das questões socioeconômicas.""",
                height = 700,
                margin=dict(l=50, r=50, b=290, t=45),
                legend_title="Legenda",
                annotations=anotacao(filtro_questao),
                font=dict(
                    family="Arial",
                    size=12,
                    color="black"
                )
            )

        relatorio_em_tabela = figura_tabela.to_html()

        menssagem = 'Análise de Dados Socioeconômicos do ENEM'
        CONTAGEM = '{:.0f}'.format(CONTAGEM)


        context = {
            'form' : form,
            'form_filtro' : form_filtro,
            'menssagem' : menssagem,
            'quantidadeParcial' : CONTAGEM,
            'quantidadeTotal' : CONTAGEMMicrodado_Amostra,
            'relatorio_dados_brutos' : relatorio_dados_brutos,
            'relatorio_em_tabela' : relatorio_em_tabela
        }
        
        # Captura o tempo de fim da execução
        tempo_final = time.time()
        tempo = tempo_final - tempo_inicial
        # Exibe o tempo de execução no terminal
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        print(f"Tempo de execução: {tempo:.6f} segundos")
        
        if request.POST.get('button')=='gerar_analise':
            return render(request, 'base/formulario_1/relatorio_formulario_4.html', context=context)
        
        if request.POST.get('button')=='baixar_csv':
            # Cria o objeto response com o cabeçalho CSV
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="microdados_enem.csv"'
            
            # Cria o escritor CSV e escreve as linhas no objeto response
            writer = csv.writer(response)
            Microdado_Amostra = Microdado_Amostra.to_csv(index=False)

            for row in csv.reader(Microdado_Amostra.splitlines()):
                writer.writerow(row)
        
            return response
    else:
        # Recebendo fomulario da tela
        form = Formulario(request.POST)
        form_filtro = Formulario_filtros(request.POST)

        # Variáveis vindas do Formulario
        filtro_questao = form.data['questao']

        print(request.POST.get('button'))
        print('000000000000000000000000000000000000000000000000000000000')
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
        
        # filtros sendo desenvolvidos
        filtro_ltp_adm_escola = form_filtro.data['tp_adm_escola']
        filtro_ano_de_conclusao = form_filtro.data['ano_de_conclusao']
        
        Amostra = '*'
        Microdado_Amostra = bd_formulario_1_4.buscar_dataframe_no_banco(
            Amostra, 
            filtro_sexo=filtro_sexo, 
            filtro_recurso=filtro_recurso,             
            filtro_ltp_adm_escola=filtro_ltp_adm_escola,            
            filtro_ano_de_conclusao=filtro_ano_de_conclusao,             
            filtro_localizacao_da_escola=filtro_localizacao_da_escola, 
            filtro_amostra=filtro_amostra, 
            filtro_estado=filtro_estado, 
            filtro_questao=filtro_questao, 
            filtro_deficiencia=filtro_deficiencia, 
            filtro_ano=filtro_ano, 
            filtro_cor=filtro_cor, 
            filtro_estado_civil=filtro_estado_civil, 
            filtro_escola=filtro_escola, 
            filtro_nacionalidade=filtro_nacionalidade)
        

        # Cria o objeto response com o cabeçalho CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="microdados_enem.csv"'
        
        # Cria o escritor CSV e escreve as linhas no objeto response
        writer = csv.writer(response)
        Microdado_Amostra = Microdado_Amostra.to_csv(index=False)

        for row in csv.reader(Microdado_Amostra.splitlines()):
            writer.writerow(row)

        return response