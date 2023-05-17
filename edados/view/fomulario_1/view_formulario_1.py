from django.shortcuts import render
import plotly.graph_objects as go
from django.utils.html import format_html_join
import pandas as pd
import plotly.express as px
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

def anotacao(Questao):

    if Questao == 'Q001':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 1 no questionario socioeconômico:
                            A: Nunca estudou.
                            B: Não completou a 4ª série/5º ano do Ensino Fundamental.
                            C: Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.
                            D: Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio.
                            E: Completou o Ensino Médio, mas não completou a Faculdade.
                            F: Completou a Faculdade, mas não completou a Pós-graduação.
                            G: Completou a Pós-graduação.
                            H: Não sei."""
    elif Questao == 'Q002':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 2 no questionario socioeconômico:
                            A: Nunca estudou.
                            B: Não completou a 4ª série/5º ano do Ensino Fundamental.
                            C: Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.
                            D: Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio.
                            E: Completou o Ensino Médio, mas não completou a Faculdade.
                            F: Completou a Faculdade, mas não completou a Pós-graduação.
                            G: Completou a Pós-graduação.
                            H: Não sei."""
    elif Questao == 'Q003':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 3 no questionario socioeconômico:
                            
                            Grupo 1: Lavrador, agricultor sem empregados, bóia fria, criador de animais (gado, porcos, galinhas, ovelhas, cavalos etc.), apicultor,
pescador, lenhador, seringueiro, extrativista.
                            Grupo 2: Diarista, empregado doméstico, cuidador de idosos, babá, cozinheiro (em casas particulares), motorista particular, jardineiro, f
axineiro de empresas e prédios, vigilante, porteiro, carteiro, office-boy, vendedor, caixa, atendente de loja, auxiliar administrativo, recepcionista, servente de pedreiro, repositor de mercadoria.
                            Grupo 3: Padeiro, cozinheiro industrial ou em restaurantes, sapateiro, costureiro, joalheiro, torneiro mecânico, operador de máquinas, 
soldador, operário de fábrica, trabalhador da mineração, pedreiro, pintor, eletricista, encanador, motorista, caminhoneiro, taxista.
                            Grupo 4: Professor (de ensino fundamental ou médio, idioma, música, artes etc.), técnico (de enfermagem, contabilidade, eletrônica etc.), 
policial, militar de baixa patente (soldado, cabo, sargento), corretor de imóveis, supervisor, gerente, mestre de obras, pastor, microempresário (proprietário de
empresa com menos de 10 empregados), pequeno comerciante, pequeno proprietário de terras, trabalhador autônomo ou por conta própria.
                            Grupo 5: Médico, engenheiro, dentista, psicólogo, economista, advogado, juiz, promotor, defensor, delegado, tenente, capitão, coronel,
professor universitário, diretor em empresas públicas ou privadas, político, proprietário de empresas com mais de 10 empregados.
                            Não sei.."""
    elif Questao == 'Q004':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 4 no questionario socioeconômico:
                            
                            Grupo 1: Lavradora, agricultora sem empregados, bóia fria, criadora de animais (gado, porcos, galinhas, ovelhas,
cavalos etc.), apicultora, pescadora, lenhadora, seringueira, extrativista.
Grupo 2: Diarista, empregada doméstica, cuidadora de idosos, babá, cozinheira (em casas particulares), motorista particular, jardineira, 
faxineira de empresas e prédios, vigilante, porteira, carteira, office-boy, vendedora, caixa, atendente de loja, auxiliar administrativa, recepcionista, servente de pedreiro, repositora de mercadoria.
Grupo 3: Padeira, cozinheira industrial ou em restaurantes, sapateira, costureira, joalheira, torneira mecânica, operadora de máquinas, 
soldadora, operária de fábrica, trabalhadora da mineração, pedreira, pintora, eletricista, encanadora, motorista, caminhoneira, taxista.
Grupo 4: Professora (de ensino fundamental ou médio, idioma, música, artes etc.), técnica (de enfermagem, contabilidade, eletrônica etc.), 
policial, militar de baixa patente (soldado, cabo, sargento), corretora de imóveis, supervisora, gerente, mestre de obras, pastora,
microempresária (proprietária de empresa com menos de 10 empregados), pequena comerciante, pequena proprietária de terras, trabalhadora autônoma ou por conta própria.
Grupo 5: Médica, engenheira, dentista, psicóloga, economista, advogada, juíza, promotora, defensora, delegada, tenente, capitã, coronel,
professora universitária, diretora em empresas públicas ou privadas, política, proprietária de empresas com mais de 10 empregados.
Não sei."""
    elif Questao == 'Q005':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 5 no questionario socioeconômico:
                            1: Moro sozinho(a)
2: 2 pessoas
3: 3 pessoas
4: 4 pessoas
5: 5 pessoas
6: 6 pessoas
7: 7 pessoas
8: 8 pessoas
9: 9 pessoas
10: 10 pessoas
11: 11 pessoas
12: 12 pessoas
13: 13 pessoas
14: 14 pessoas
15: 15 pessoas
16: 16 pessoas
17: 17 pessoas
18: 18 pessoas
19: 19 pessoas
20: 20 pessoas"""
    elif Questao == 'Q006':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 6 no questionario socioeconômico:
                            
                            A: Nenhuma renda
B: Até R$ 998,00
C: De R$ 998,01 até R$ 1.497,00
D: De R$ 1.497,01 até R$ 1.996,00
E: De R$ 1.996,01 até R$ 2.495,00
F: De R$ 2.495,01 até R$ 2.994,00
G: De R$ 2.994,01 até R$ 3.992,00
H: De R$ 3.992,01 até R$ 4.990,00
I: De R$ 4.990,01 até R$ 5.988,00
J: De R$ 5.988,01 até R$ 6.986,00
K: De R$ 6.986,01 até R$ 7.984,00
L: De R$ 7.984,01 até R$ 8.982,00
M: De R$ 8.982,01 até R$ 9.980,00
N: De R$ 9.980,01 até R$ 11.976,00
O: De R$ 11.976,01 até R$ 14.970,00
P: De R$ 14.970,01 até R$ 19.960,00
Q: Mais de R$ 19.960,00"""
    elif Questao == 'Q007':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 7 no questionario socioeconômico:
                            A: Não.
B: Sim, um ou dois dias por semana.
C: Sim, três ou quatro dias por semana.
D: Sim, pelo menos cinco dias por semana."""
    elif Questao == 'Q008':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 8 no questionario socioeconômico:
                            
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
    elif Questao == 'Q009':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 9 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
    elif Questao == 'Q010':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 10 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
    elif Questao == 'Q011':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 11 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
    elif Questao == 'Q012':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 12 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
    elif Questao == 'Q013':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 13 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
    elif Questao == 'Q014':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 14 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
    elif Questao == 'Q015':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 15 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
    elif Questao == 'Q016':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 16 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
    elif Questao == 'Q017':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 17 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
    elif Questao == 'Q018':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 18 no questionario socioeconômico:
                            A: Sim.
B Não."""
    elif Questao == 'Q019':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 19 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
    elif Questao == 'Q020':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 20 no questionario socioeconômico:
                            A: Sim.
B Não."""
    elif Questao == 'Q021':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 21 no questionario socioeconômico:
                            A: Sim.
B Não."""
    elif Questao == 'Q022':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 22 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
    elif Questao == 'Q023':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 23 no questionario socioeconômico:
                            A: Sim.
B Não."""
    elif Questao == 'Q024':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 24 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
    elif Questao == 'Q025':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 25 no questionario socioeconômico:
                            A: Sim.
B Não."""
    else:
        texto="Nenhum"
    texto_quadro = """Quadro informativo: apresenta o quantitativo de alunos de acordo com os filtros selecionados. Ele fornece uma visão detalhada da distribuição dos alunos com base nos critérios de filtro aplicados, permitindo uma análise específica e segmentada dos dados. Esse quadro ajuda a compreender a quantidade de alunos que atendem aos diferentes critérios e fornece insights importantes para a tomada de decisões e análise estatística.
    """

    return [texto_quadro, texto]

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
        
        if(questao!="nenhum"):
            Amostra = [demografico, questao]
        else:
            Amostra = [demografico]
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
            

        CONTAGEM  = Microdado_Amostra[demografico].count()
        menssagem = 'Análise de Dados Socioeconômicos do ENEM'
        relatorio_em_grafico=''
        relatorio=""
        relatorio_em_quadro=''

        if (demografico == 'TP_SEXO'):

            if (filtro_sexo == 'todos'):
                vetor = demografico_sexo(
                    Microdado_Amostra, demografico, questao)
                relatorio=""
                relatorio_em_grafico  = vetor[0]
                relatorio_em_quadro  = vetor[1]
            else:
                vetor = demografico_sexo_unilateral(
                    Microdado_Amostra, demografico, questao, filtro_sexo)
                relatorio_em_grafico = vetor[0]
                relatorio_em_quadro  = vetor[1]

        elif (demografico == 'TP_ESTADO_CIVIL'):
            vetor = demografico_estado_civil(
                Microdado_Amostra, demografico, questao, filtro_ano)
            relatorio_em_grafico = vetor[0]
            # relatorio_em_grafico = vetor[1]

        elif (demografico == 'TP_COR_RACA'):
            vetor = demografico_raca(Microdado_Amostra, demografico, questao)
            relatorio_em_grafico = vetor[0]

        elif (demografico == 'TP_NACIONALIDADE'):
            vetor = demografico_nascionalidade(
                Microdado_Amostra, demografico, questao)
            relatorio_em_grafico = vetor[0]

        elif (demografico == 'TP_ESCOLA'):
            vetor = demografico_escolaridade(
                Microdado_Amostra, demografico, questao)
            relatorio_em_grafico = vetor[0]

        elif (demografico == 'TP_ENSINO'):
            vetor = demografico_instituicao_aonde_conclui_ensino_medio(
                Microdado_Amostra, demografico, questao)
            relatorio_em_grafico = vetor[0]

        elif (demografico == 'TP_ANO_CONCLUIU'):
            vetor = demografico_ano_de_conclusao(
                Microdado_Amostra, demografico, questao, filtro_ano=filtro_ano)
            relatorio_em_grafico = vetor[0]


        if(questao=="nenhum"):        
            anotacao_mensagem = anotacao(questao)
        else:      
            anotacao_mensagem = anotacao(questao)
        
        if(questao=="nenhum"):
            anotacao_quadro   = anotacao_mensagem[0]
            anotacao_mensagem = "Gráfico de Pizza: é uma forma visual eficaz de representar a distribuição de dados categorizados em formato de porcentagem. Ele mostra a proporção de diferentes categorias em um conjunto de dados. Ao calcular as porcentagens para cada categoria (masculino e feminino) em relação ao total, é possível observar facilmente a distribuição das respostas por gênero em relação aos filtros selecionados. As fatias do gráfico representam as porcentagens das respostas masculinas e femininas, proporcionando uma compreensão visual rápida e clara da distribuição."
            anotacao_mensagem = anotacao_mensagem.split('\n')
            anotacao_mensagem = format_html_join(
                '\n', '<div class="col-md-12 mt-2"><h6 class="font-weight-normal mb-0">{}</h6></div>', ((line,) for line in anotacao_mensagem))
            # Cria a mensagem de anotação
            informativo = '<h5 class="mb-0">Informativo:</h5>'

            anotacao_quadro = anotacao_quadro.split('\n')
            anotacao_quadro = format_html_join(
                '\n', '<div class="col-md-11 mt-2"><h6 class="font-weight-normal mb-0">{}</h6></div>', ((line,) for line in anotacao_quadro))
            
            # Formata a mensagem em HTML
            anotacao_mensagem = f'<div class="col-md-11 border"><div class="col-md-11 mt-2">{informativo}</div><hr class="mt-0">{anotacao_quadro}<hr class="mt-0">{anotacao_mensagem}</div>'
            # anotacao_mensagem="teste"
            print(anotacao_mensagem)
        else:
            anotacao_quadro = anotacao_mensagem[0]
            anotacao_mensagem = anotacao_mensagem[1]
            anotacao_mensagem = anotacao_mensagem.split('\n')
            anotacao_mensagem = format_html_join(
                '\n', '<div class="col-md-12 mt-2"><h6 class="font-weight-normal mb-0">{}</h6></div>', ((line,) for line in anotacao_mensagem))
            # Cria a mensagem de anotação
            informativo = '<h5 class="mb-0">Informativo:</h5>'

            anotacao_quadro = anotacao_quadro.split('\n')
            anotacao_quadro = format_html_join(
                '\n', '<div class="col-md-11 mt-2"><h6 class="font-weight-normal mb-0">{}</h6></div>', ((line,) for line in anotacao_quadro))
            
            # Formata a mensagem em HTML
            anotacao_mensagem = f'<div class="col-md-11 border"><div class="col-md-11 mt-2">{informativo}</div><hr class="mt-0">{anotacao_quadro}<hr class="mt-0">{anotacao_mensagem}</div>'
            
        context = {
            'form': form,
            'anotacao_mensagem' : anotacao_mensagem,
            'form_filtro': form_filtro,
            'menssagem': menssagem,
            'relatorio_em_grafico': relatorio_em_grafico,
            'quantidadeParcial' : CONTAGEM,
            'quantidadeTotal' : CONTAGEMMicrodado_Amostra,
            'relatorio_em_quadro': relatorio_em_quadro,
            'relatorio': relatorio
        }

    return render(request, 'base/formulario_1/relatorio_formulario_1.html', context=context)

def demografico_sexo(Microdado_Amostra, demografico, questao):
    
    if questao!="nenhum":
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

        fig.update_layout(
            title_text='Gráfico de correlação entre a resposta da questão socioeconômica: '+questao+' e a questão demográfica: '+demografico,
            height=400,
            margin=dict(l=50, r=50, b=20, t=50),
            xaxis_title="Resposta da questão: "+questao+" do questionário socioeconômico por sexo",
            yaxis_title="Porcentagem",
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )

        relatorio_em_quadro = pd.DataFrame(DataFrame_para_criar_a_grafico)
        relatorio_em_quadro = relatorio_em_quadro.to_html()
        
        relatorio_em_grafico = px.bar(
            DataFrame_para_criar_a_grafico,
            barmode='group',
            text_auto=True)

        relatorio_em_grafico.update_layout(
            title_text='Gráfico de correlação entre a resposta da questão socioeconômica: '+questao+' e a questão demográfica: '+demografico,
            height=400,
            margin=dict(l=50, r=50, b=20, t=50),
            xaxis_title="Resposta da questão: "+questao+" do questionário socioeconômico por sexo.",
            yaxis_title="Porcentagem",
            legend_title="Legenda",
            font={'family': "Arial", 'size': 12, 'color': "black"}
        )

        rowEvenColor = 'lightgrey'
        rowOddColor = 'white'
        DataFrame = DataFrame.unstack()
        DataFrame = DataFrame.T
        print('----------------------------------------------')
        print(DataFrame)
        figura_tabela = go.Figure(data=[
            go.Table(
                header=dict(
                    values=['Respostas', 'Feminino', 'Masculino', 'Total'],
                    # values=['Respostas'],
                    fill_color='royalblue',
                    height=40,
                    line_color='darkslategray',
                    align=['left', 'center'],
                    font=dict(color='white', size=12)
                ),
                cells=dict(
                    values=[DataFrame.index, DataFrame.F, DataFrame.M, (DataFrame.F+DataFrame.M)],
                    line_color='darkslategray',
                    fill_color=[[rowOddColor, rowEvenColor, rowOddColor, rowEvenColor, rowOddColor]*5],
                    align=['left', 'center'],
                    font=dict(color='darkslategray', size=11)
                )
            )
        ])
        
                
        figura_tabela.update_layout(
            title_text="Quadro informativo sobre a proporção de alunos por resposta do questionário socioeconômica, na questão: "+questao,
            height=400,
            margin=dict(l=50, r=50, b=20, t=50),
            yaxis={'domain': [0, .45]},
            xaxis2={'anchor': 'y2'},
            xaxis_title=("Resposta da questão: "+questao+" do questionário socioeconômico"),
            yaxis_title="Porcentagem Parcial",
            yaxis2={'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'},
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )
        
        relatorio_em_grafico = relatorio_em_grafico.to_html()
        figura_tabela = figura_tabela.to_html()
        relatorio = fig.to_html()
    else:
        relatorio_em_grafico = ""
        figura_tabela = ""
        relatorio = ""
        print('----------------------------------------------')
        print(Microdado_Amostra)
        Microdado_Amostra = Microdado_Amostra.groupby([demografico])
        Microdado_Amostra = Microdado_Amostra[demografico].count()
        
        rowEvenColor = 'lightgrey'
        rowOddColor = 'white'
        if("M" not in Microdado_Amostra.index):
            Microdado_Amostra.M =0
        if("F" not in Microdado_Amostra.index):
            Microdado_Amostra.F =0
            
        
        figura_tabela = go.Figure(data=[
            go.Table(
                header=dict(
                    values=['Respostas', 'Feminino', 'Masculino', 'Total'],
                    # values=['Respostas'],
                    fill_color='royalblue',
                    height=40,
                    line_color='darkslategray',
                    align=['left', 'center'],
                    font=dict(color='white', size=12)
                ),
                cells=dict(
                    values=["TP_SEXO", Microdado_Amostra.F, Microdado_Amostra.M, (Microdado_Amostra.F+Microdado_Amostra.M)],
                    line_color='darkslategray',
                    fill_color=[[rowOddColor, rowEvenColor, rowOddColor, rowEvenColor, rowOddColor]*5],
                    align=['left', 'center'],
                    font=dict(color='darkslategray', size=11)
                )
            )
        ])
                
        figura_tabela.update_layout(
            title_text="Quadro informativo sobre a proporção de alunos por 'Gênero'",
            height=150,
            margin=dict(l=50, r=50, b=20, t=50),
            yaxis={'domain': [0, .45]},
            xaxis2={'anchor': 'y2'},
            xaxis_title=("Resposta da questão: "+questao+" do questionário socioeconômico"),
            yaxis_title="Porcentagem Parcial",
            yaxis2={'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'},
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )
        
        
        # Dados do gráfico
        labels = Microdado_Amostra.index
        values_feminino = Microdado_Amostra.F
        values_masculino = Microdado_Amostra.M
        values_total = Microdado_Amostra.F + Microdado_Amostra.M

        # Criando o gráfico de pizza
        relatorio_em_grafico = go.Figure(data=[go.Pie(labels=labels, values=[ Microdado_Amostra.M, Microdado_Amostra.F])])

        # Personalizando o layout do gráfico
        relatorio_em_grafico.update_layout(title='Distribuição de alunos por Gênero',
                        title_font_size=16,
                        legend=dict(
                            orientation='h',
                            yanchor='bottom',
                            y=1.02,
                            xanchor='center',
                            x=0.5
                        ))


        
        figura_tabela = figura_tabela.to_html()
        relatorio_em_grafico = relatorio_em_grafico.to_html()
        relatorio = relatorio_em_grafico
        print('----------------------------------------------')
        print(Microdado_Amostra)
        # print(Microdado_Amostra['index'])

    return [relatorio_em_grafico, figura_tabela, relatorio]

def demografico_sexo_unilateral(Microdado_Amostra, demografico, questao, filtro_sexo):

    if questao!="nenhum":
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
            title_text='Gráfico de correlação entre a resposta da questão socioeconômica: '+questao+' e a questão demográfica: '+demografico,
            height=400,
            margin=dict(l=50, r=50, b=20, t=50),
            xaxis_title="Resposta da questão: "+questao+" do questionário socioeconômico",
            yaxis_title="Porcentagem",
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )
        relatorio = fig.to_html()
    else:
        relatorio_em_grafico = ""
        figura_tabela = ""
        relatorio = ""
        Microdado_Amostra = Microdado_Amostra.groupby([demografico])
        Microdado_Amostra = Microdado_Amostra[demografico].count()
        print('----------------------------------------------')
        print(Microdado_Amostra)
        
        # Dados do gráfico
        labels = Microdado_Amostra.index

        if("M" == filtro_sexo and Microdado_Amostra.empty):
            labels=["Masculino"]
            Microdado_Amostra["M"] =0
        if("F" == filtro_sexo and Microdado_Amostra.empty):
            labels=["Feminino"]
            Microdado_Amostra["F"] =0
            
        rowEvenColor = 'lightgrey'
        rowOddColor = 'white'
        figura_tabela = go.Figure(data=[
            go.Table(
                header=dict(
                    values=['Respostas',labels],
                    # values=['Respostas'],
                    fill_color='royalblue',
                    height=40,
                    line_color='darkslategray',
                    align=['left', 'center'],
                    font=dict(color='white', size=12)
                ),
                cells=dict(
                    values=["TP_SEXO", Microdado_Amostra],
                    line_color='darkslategray',
                    fill_color=[[rowOddColor, rowEvenColor, rowOddColor, rowEvenColor, rowOddColor]*5],
                    align=['left', 'center'],
                    font=dict(color='darkslategray', size=11)
                )
            )
        ])
                
        figura_tabela.update_layout(
            title_text="Quadro informativo sobre a proporção de alunos por 'Gênero'",
            height=150,
            margin=dict(l=50, r=50, b=20, t=50),
            yaxis={'domain': [0, .45]},
            xaxis2={'anchor': 'y2'},
            xaxis_title=("Resposta da questão: "+questao+" do questionário socioeconômico"),
            yaxis_title="Porcentagem Parcial",
            yaxis2={'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'},
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )
        
        if(Microdado_Amostra.empty):
            return [relatorio, figura_tabela]
        
        # Criando o gráfico de pizza
        relatorio_em_grafico = go.Figure(data=[go.Pie(labels=labels, values=Microdado_Amostra)])

        # Personalizando o layout do gráfico
        relatorio_em_grafico.update_layout(title='Distribuição de alunos por Gênero',
                        title_font_size=16,
                        legend=dict(
                            orientation='h',
                            yanchor='bottom',
                            y=1.02,
                            xanchor='center',
                            x=0.5
                        ))


        
        figura_tabela = figura_tabela.to_html()
        relatorio_em_grafico = relatorio_em_grafico.to_html()
        relatorio = relatorio_em_grafico

    return [relatorio, figura_tabela]

def demografico_estado_civil(Microdado_Amostra, demografico, questao, filtro_ano):

    if questao!="nenhum":
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
            title_text='Gráfico de correlação entre a resposta da questão socioeconômica: '+questao+' e a questão demográfica: '+demografico,
            height=400,
            margin=dict(l=50, r=50, b=20, t=50),
            xaxis_title="Resposta da questão: "+questao+" do questionário socioeconômico",
            yaxis_title="Porcentagem",
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )
        relatorio_em_grafico = px.bar(
            DataFrame_para_criar_a_grafico, barmode='group')

        relatorio_em_grafico.update_layout(
            title_text='Gráfico de correlação entre a resposta da questão socioeconômica: '+questao+' e a questão demográfica: '+demografico,
            height=400,
            margin=dict(l=50, r=50, b=20, t=50),
            xaxis_title="Resposta da questão: "+questao+" do questionário socioeconômico",
            yaxis_title="Porcentagem",
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )
        relatorio_em_grafico = relatorio_em_grafico.to_html()

        relatorio = fig.to_html()
    else:
        # if(0.0 in Microdado_Amostra.index and Microdado_Amostra.empty):
        #     labels=["Masculino"]
        #     Microdado_Amostra["1"] =0
        #     print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        #     print(Microdado_Amostra["1"])
        # if("1" in Microdado_Amostra.index and Microdado_Amostra.empty):
        #     labels=["Feminino"]
        #     Microdado_Amostra["1"] =0
        relatorio_em_grafico = ""
        figura_tabela = ""
        relatorio = ""
        print('----------------------------------------------')
        print(Microdado_Amostra)
        Microdado_Amostra = Microdado_Amostra.groupby([demografico])
        Microdado_Amostra = Microdado_Amostra[demografico].count()
        
        rowEvenColor = 'lightgrey'
        rowOddColor = 'white'
        figura_tabela = go.Figure(data=[
            go.Table(
                header=dict(
                    values=['Respostas', 'Feminino', 'Masculino', 'Total'],
                    # values=['Respostas'],
                    fill_color='royalblue',
                    height=40,
                    line_color='darkslategray',
                    align=['left', 'center'],
                    font=dict(color='white', size=12)
                ),
                cells=dict(
                    values=["TP_ESTADO_CIVIL", Microdado_Amostra],
                    line_color='darkslategray',
                    fill_color=[[rowOddColor, rowEvenColor, rowOddColor, rowEvenColor, rowOddColor]*5],
                    align=['left', 'center'],
                    font=dict(color='darkslategray', size=11)
                )
            )
        ])
                
        figura_tabela.update_layout(
            title_text="Quadro informativo sobre a proporção de alunos por 'Gênero'",
            height=150,
            margin=dict(l=50, r=50, b=20, t=50),
            yaxis={'domain': [0, .45]},
            xaxis2={'anchor': 'y2'},
            xaxis_title=("Resposta da questão: "+questao+" do questionário socioeconômico"),
            yaxis_title="Porcentagem Parcial",
            yaxis2={'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'},
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )
        # Dados do gráfico
        labels = ['não informou', 'solteiro', 'casado', 'viúvo', 'divorciado']


        # Verifica se o índice existe antes de acessá-lo
        values = [Microdado_Amostra[i] for i in range(len(Microdado_Amostra)) if i in [0, 1, 2, 3, 4]]

        # Criando o gráfico de pizza
        relatorio_em_grafico = go.Figure(data=[go.Pie(labels=labels, values=values)])

        # Personalizando o layout do gráfico
        relatorio_em_grafico.update_layout(title='Distribuição de alunos por estado civil',
                        title_font_size=16,
                        legend=dict(
                            orientation='h',
                            yanchor='bottom',
                            y=1.02,
                            xanchor='center',
                            x=0.5
                        ))


        
        figura_tabela = figura_tabela.to_html()
        relatorio_em_grafico = relatorio_em_grafico.to_html()
        relatorio = relatorio_em_grafico
        print('----------------------------------------------')
        print(Microdado_Amostra)
        # print(Microdado_Amostra['index'])


    return [relatorio, relatorio_em_grafico]

def demografico_raca(Microdado_Amostra, demografico, questao):

    if questao!="nenhum":
        DataFrame = Microdado_Amostra.sort_values(by=[questao])
        DataFrame = DataFrame.groupby([demografico, questao])
        DataFrame = DataFrame[demografico].count()

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
            title_text='Gráfico de correlação entre a resposta da questão socioeconômica: '+questao+' e a questão demográfica: '+demografico,
            height=400,
            margin=dict(l=50, r=50, b=20, t=50),
            xaxis_title="Resposta da questão: "+questao+" do questionário socioeconômico",
            yaxis_title="Porcentagem",
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )

        relatorio = fig.to_html()
    else:
        DataFrame = Microdado_Amostra.sort_values(by=[demografico])
        DataFrame = DataFrame.groupby([demografico])
        DataFrame = DataFrame[demografico].count()

        # rotacionar
        # DataFrame = DataFrame.unstack()

        # Pegando lista de index pra usá-los posteriomente.
        lista_dos_index = DataFrame.index.to_list()

        # desrotacionar
        # DataFrame = DataFrame.stack()

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
                
            print(DataFrame[index])
            fig.add_bar(
                y=([(DataFrame[index]/CONTAGEM)*100]),
                x=DataFrame.index,
                text=((DataFrame[index]/CONTAGEM)*100),
                    texttemplate='%{text:.2f}%',
                    textposition='auto',
                    name=nome
                )

        fig.update_layout(
            title_text='Gráfico de correlação entre a resposta da questão socioeconômica: '+questao+' e a questão demográfica: '+demografico,
            height=400,
            margin=dict(l=50, r=50, b=20, t=50),
            xaxis_title="Resposta da questão: "+questao+" do questionário socioeconômico",
            yaxis_title="Porcentagem",
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )

        relatorio = fig.to_html()

    return [relatorio]

def demografico_nascionalidade(Microdado_Amostra, demografico, questao):

    if questao!="nenhum":
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
                nome = 'Brasileiro(a) Nato(a)'

            fig.add_bar(
                y=((DataFrame[index]/CONTAGEM)*100),
                x=DataFrame[index].index,
                text=((DataFrame[index]/CONTAGEM)*100),
                    texttemplate='%{text:.2f}%',
                    textposition='auto',
                    name=nome
                )

        fig.update_layout(
            title_text='Gráfico de correlação entre a resposta da questão socioeconômica: '+questao+' e a questão demográfica: '+demografico,
            height=400,
            margin=dict(l=50, r=50, b=20, t=50),
            xaxis_title="Resposta da questão: "+questao+" do questionário socioeconômico",
            yaxis_title="Porcentagem",
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )

        relatorio = fig.to_html()
    else:   
        DataFrame = Microdado_Amostra.sort_values(by=[demografico])
        DataFrame = DataFrame.groupby([demografico])
        DataFrame = DataFrame[demografico].count()

        lista_dos_index = DataFrame.index.to_list()
        print(lista_dos_index)

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
                nome = 'Brasileiro(a) Nato(a)'

            fig.add_bar(
                y=([(DataFrame[index]/CONTAGEM)*100]),
                x=DataFrame.index,
                text=((DataFrame[index]/CONTAGEM)*100),
                    texttemplate='%{text:.2f}%',
                    textposition='auto',
                    name=nome
                )

        fig.update_layout(
            title_text='Gráfico de correlação entre a resposta da questão socioeconômica: '+questao+' e a questão demográfica: '+demografico,
            height=400,
            margin=dict(l=50, r=50, b=20, t=50),
            xaxis_title="Resposta da questão: "+questao+" do questionário socioeconômico",
            yaxis_title="Porcentagem",
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )

        relatorio = fig.to_html()

    return [relatorio]

def demografico_escolaridade(Microdado_Amostra, demografico, questao):

    if questao!="nenhum":
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
            title_text='Gráfico de correlação entre a resposta da questão socioeconômica: '+questao+' e a questão demográfica: '+demografico,
            height=400,
            margin=dict(l=50, r=50, b=20, t=50),
            xaxis_title="Resposta da questão: "+questao+" do questionário socioeconômico",
            yaxis_title="Porcentagem",
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )

        relatorio = fig.to_html()
    else:
        DataFrame = Microdado_Amostra.sort_values(by=[demografico])
        DataFrame = DataFrame.groupby([demografico])
        DataFrame = DataFrame[demografico].count()

        lista_dos_index = DataFrame.index.to_list()
        print(lista_dos_index)

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
                y=([(DataFrame[index]/CONTAGEM)*100]),
                x=DataFrame.index,
                text=((DataFrame[index]/CONTAGEM)*100),
                    texttemplate='%{text:.2f}%',
                    textposition='auto',
                    name=nome
                )

        fig.update_layout(
            title_text='Gráfico de correlação entre a resposta da questão socioeconômica: '+questao+' e a questão demográfica: '+demografico,
            height=400,
            margin=dict(l=50, r=50, b=20, t=50),
            xaxis_title="Resposta da questão: "+questao+" do questionário socioeconômico",
            yaxis_title="Porcentagem",
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )

        relatorio = fig.to_html()

    return [relatorio]

def demografico_conclusao_ensino_medio(Microdado_Amostra, demografico, questao):

    if questao!="nenhum":
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
            title_text='Gráfico de correlação entre a resposta da questão socioeconômica: '+questao+' e a questão demográfica: '+demografico,
            height=400,
            margin=dict(l=50, r=50, b=20, t=50),
            xaxis_title="Resposta da questão: "+questao+" do questionário socioeconômico",
            yaxis_title="Porcentagem",
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )

        relatorio = fig.to_html()
    else:
        DataFrame = Microdado_Amostra.sort_values(by=[demografico])
        DataFrame = DataFrame.groupby([demografico])
        DataFrame = DataFrame[demografico].count()

        lista_dos_index = DataFrame.index.to_list()
        print(lista_dos_index)

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
                y=([(DataFrame[index]/CONTAGEM)*100]),
                x=DataFrame.index,
                text=((DataFrame[index]/CONTAGEM)*100),
                    texttemplate='%{text:.2f}%',
                    textposition='auto',
                    name=nome
                )

        fig.update_layout(
            title_text='Gráfico de correlação entre a resposta da questão socioeconômica: '+questao+' e a questão demográfica: '+demografico,
            height=400,
            margin=dict(l=50, r=50, b=20, t=50),
            xaxis_title="Resposta da questão: "+questao+" do questionário socioeconômico",
            yaxis_title="Porcentagem",
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )

        relatorio = fig.to_html()


    return [relatorio]

def demografico_ano_de_conclusao(Microdado_Amostra, demografico, questao, filtro_ano):

    if questao!="nenhum":
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
                print('----------------------')
                print(index)
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
            else:
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
            title_text='Gráfico de correlação entre a resposta da questão socioeconômica: '+questao+' e a questão demográfica: '+demografico,
            height=400,
            margin=dict(l=50, r=50, b=20, t=50),
            xaxis_title="Resposta da questão: "+questao+" do questionário socioeconômico",
            yaxis_title="Porcentagem",
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )

        relatorio = fig.to_html()
    else:
        DataFrame = Microdado_Amostra.sort_values(by=[demografico])
        DataFrame = DataFrame.groupby([demografico])
        DataFrame = DataFrame[demografico].count()

        lista_dos_index = DataFrame.index.to_list()
        print(lista_dos_index)

        fig = go.Figure()

        for index in lista_dos_index:

            if filtro_ano == '2019':
                print('----------------------')
                print(index)
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
            else:
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
                y=([(DataFrame[index]/CONTAGEM)*100]),
                x=DataFrame.index,
                text=((DataFrame[index]/CONTAGEM)*100),
                    texttemplate='%{text:.2f}%',
                    textposition='auto',
                    name=nome
                )

        fig.update_layout(
            title_text='Gráfico de correlação entre a resposta da questão socioeconômica: '+questao+' e a questão demográfica: '+demografico,
            height=400,
            margin=dict(l=50, r=50, b=20, t=50),
            xaxis_title="Resposta da questão: "+questao+" do questionário socioeconômico",
            yaxis_title="Porcentagem",
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )

        relatorio = fig.to_html()

    return [relatorio]

def demografico_instituicao_aonde_conclui_ensino_medio(Microdado_Amostra, demografico, questao):

    if questao!="nenhum":
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
            title_text='Gráfico de correlação entre a resposta da questão socioeconômica: '+questao+' e a questão demográfica: '+demografico,
            height=400,
            margin=dict(l=50, r=50, b=20, t=50),
            xaxis_title="Resposta da questão: "+questao+" do questionário socioeconômico",
            yaxis_title="Porcentagem",
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )

        relatorio = fig.to_html()
    else:
        DataFrame = Microdado_Amostra.sort_values(by=[demografico])
        DataFrame = DataFrame.groupby([demografico])
        DataFrame = DataFrame[demografico].count()


        lista_dos_index = DataFrame.index.to_list()
        print(lista_dos_index)

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
                y=([(DataFrame[index]/CONTAGEM)*100]),
                x=DataFrame.index,
                text=((DataFrame[index]/CONTAGEM)*100),
                    texttemplate='%{text:.2f}%',
                    textposition='auto',
                    name=nome
                )

        fig.update_layout(
            title_text='Gráfico de correlação entre a resposta da questão socioeconômica: '+questao+' e a questão demográfica: '+demografico,
            height=400,
            margin=dict(l=50, r=50, b=20, t=50),
            xaxis_title="Resposta da questão: "+questao+" do questionário socioeconômico",
            yaxis_title="Desempenho",
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )

        relatorio = fig.to_html()

    return [relatorio]
