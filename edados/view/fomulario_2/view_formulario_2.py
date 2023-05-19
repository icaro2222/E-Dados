from django.shortcuts import render
import plotly.graph_objects as go
import plotly.express as px
from edados.formularios.formulario_2.formulario_2 import Formulario_2
from edados.formularios.filtros.formulario_1_filtros import Formulario_filtros
from django.utils.html import format_html_join
from edados.database import bd_quest_socio_notas_deficiencia
from django.contrib.auth.decorators import login_required

CONTAGEM = 0
CONTAGEMMicrodado_Amostra = 0

def formatar(valor):
    return "{:,.2f}".format(valor)

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
        y = -0.8
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
        y = -0.8
    elif Questao == 'Q003':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 3 no questionario socioeconômico:
                            
                            Grupo 1: Lavrador, agricultor sem empregados, bóia fria, criador de animais (gado, porcos, galinhas, ovelhas, cavalos etc.), apicultor,
<br pescador, lenhador, seringueiro, extrativista.
                            Grupo 2: Diarista, empregado doméstico, cuidador de idosos, babá, cozinheiro (em casas particulares), motorista particular, jardineiro, f
<braxineiro de empresas e prédios, vigilante, porteiro, carteiro, office-boy, vendedor, caixa, atendente de loja, auxiliar administrativo, recepcionista, servente de pedreiro, repositor de mercadoria.
                            Grupo 3: Padeiro, cozinheiro industrial ou em restaurantes, sapateiro, costureiro, joalheiro, torneiro mecânico, operador de máquinas, 
<brsoldador, operário de fábrica, trabalhador da mineração, pedreiro, pintor, eletricista, encanador, motorista, caminhoneiro, taxista.
                            Grupo 4: Professor (de ensino fundamental ou médio, idioma, música, artes etc.), técnico (de enfermagem, contabilidade, eletrônica etc.), 
<brpolicial, militar de baixa patente (soldado, cabo, sargento), corretor de imóveis, supervisor, gerente, mestre de obras, pastor, microempresário (proprietário de
<br empresa com menos de 10 empregados), pequeno comerciante, pequeno proprietário de terras, trabalhador autônomo ou por conta própria.
                            Grupo 5: Médico, engenheiro, dentista, psicólogo, economista, advogado, juiz, promotor, defensor, delegado, tenente, capitão, coronel,
<br professor universitário, diretor em empresas públicas ou privadas, político, proprietário de empresas com mais de 10 empregados.
                            Não sei.."""
        y = -0.8
    elif Questao == 'Q004':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 4 no questionario socioeconômico:
                            
                            Grupo 1: Lavradora, agricultora sem empregados, bóia fria, criadora de animais (gado, porcos, galinhas, ovelhas,
<br cavalos etc.), apicultora, pescadora, lenhadora, seringueira, extrativista.
Grupo 2: Diarista, empregada doméstica, cuidadora de idosos, babá, cozinheira (em casas particulares), motorista particular, jardineira, 
<brfaxineira de empresas e prédios, vigilante, porteira, carteira, office-boy, vendedora, caixa, atendente de loja, auxiliar administrativa, recepcionista, servente de pedreiro, repositora de mercadoria.
Grupo 3: Padeira, cozinheira industrial ou em restaurantes, sapateira, costureira, joalheira, torneira mecânica, operadora de máquinas, 
<brsoldadora, operária de fábrica, trabalhadora da mineração, pedreira, pintora, eletricista, encanadora, motorista, caminhoneira, taxista.
Grupo 4: Professora (de ensino fundamental ou médio, idioma, música, artes etc.), técnica (de enfermagem, contabilidade, eletrônica etc.), 
<brpolicial, militar de baixa patente (soldado, cabo, sargento), corretora de imóveis, supervisora, gerente, mestre de obras, pastora,
<br microempresária (proprietária de empresa com menos de 10 empregados), pequena comerciante, pequena proprietária de terras, trabalhadora autônoma ou por conta própria.
Grupo 5: Médica, engenheira, dentista, psicóloga, economista, advogada, juíza, promotora, defensora, delegada, tenente, capitã, coronel,
<br professora universitária, diretora em empresas públicas ou privadas, política, proprietária de empresas com mais de 10 empregados.
Não sei."""
        y = -0.8
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
        y = -0.8
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
        y = -0.8
    elif Questao == 'Q007':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 7 no questionario socioeconômico:
                            A: Não.
B: Sim, um ou dois dias por semana.
C: Sim, três ou quatro dias por semana.
D: Sim, pelo menos cinco dias por semana."""
        y = -0.8
    elif Questao == 'Q008':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 8 no questionario socioeconômico:
                            
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
        y = -0.8
    elif Questao == 'Q009':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 9 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
        y = -0.8
    elif Questao == 'Q010':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 10 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
        y = -0.8
    elif Questao == 'Q011':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 11 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
        y = -0.8
    elif Questao == 'Q012':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 12 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
        y = -0.8
    elif Questao == 'Q013':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 13 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
        y = -0.8
    elif Questao == 'Q014':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 14 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
        y = -0.8
    elif Questao == 'Q015':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 15 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
        y = -0.8
    elif Questao == 'Q016':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 16 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
        y = -0.8
    elif Questao == 'Q017':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 17 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
        y = -0.8
    elif Questao == 'Q018':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 18 no questionario socioeconômico:
                            A: Sim.
B Não."""
        y = -0.8
    elif Questao == 'Q019':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 19 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
        y = -0.8
    elif Questao == 'Q020':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 20 no questionario socioeconômico:
                            A: Sim.
B Não."""
        y = -0.8
    elif Questao == 'Q021':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 21 no questionario socioeconômico:
                            A: Sim.
B Não."""
        y = -0.8
    elif Questao == 'Q022':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 22 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
        y = -0.8
    elif Questao == 'Q023':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 23 no questionario socioeconômico:
                            A: Sim.
B Não."""
        y = -0.8
    elif Questao == 'Q024':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 24 no questionario socioeconômico:
                            A: Não.
B: Sim, um.
C: Sim, dois.
D: Sim, três.
E: Sim, quatro ou mais."""
        y = -0.8

    elif Questao == 'Q025':
        texto = """A legenda: "A, B, C, D, ..." se referem às opções de resposta da Questão 25 no questionario socioeconômico:
                            A: Sim.
                            B Não."""
        y = -0.8
        
    texto_quadro = """- Na primeira seção da tela, há um quadro com dados sobre a média das notas dos alunos que você selecionou usando os filtros do formulário logo acima.
                - Nesse mesmo quadro, você também encontrará a maior nota obtida na prova, a menor nota e os quartis. 
                - É importante salientar que os quartis são valores que dividem o conjunto de dados em quatro partes iguais, sendo que 25% é o quartil 1, 50%(que é a mediana) é o quartil 2 e 75% é o quartil 3.
                - Na seção seguinte, há um gráfico que ilustra claramente a diferença entre a nota mínima, a média e a nota máxima.
                """
        
    
    

    return [texto_quadro, texto]



@login_required
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
        
        
        # Formulario de Filtro
        filtro_sexo = form_filtro.data['sexo']
        filtro_ano = form_filtro.data['ano']

        if(filtro_sexo != 'todos'):
            if(Q=='nenhum'):            
                Amostra = [prova, 'TP_SEXO']
            else:
                Amostra = [prova, Q, 'TP_SEXO']
            if(filtro_deficiencia != 'todas' and filtro_deficiencia != 'nenhuma'):
                Microdado_Amostra = bd_quest_socio_notas_deficiencia.buscar_dataframe_no_banco(
                    Amostra, 
                    filtro_sexo=filtro_sexo,                
                    filtro_amostra=filtro_amostra, 
                    filtro_deficiencia=filtro_deficiencia,
                    filtro_cor=filtro_cor, 
                    filtro_estado=filtro_estado, 
                    filtro_recurso=filtro_recurso, 
                    filtro_questao=Q, 
                    filtro_localizacao_da_escola=filtro_localizacao_da_escola, 
                    filtro_estado_civil=filtro_estado_civil, 
                    filtro_escola=filtro_escola, 
                    filtro_nacionalidade=filtro_nacionalidade,
                    filtro_ano=filtro_ano)
            else:
                Microdado_Amostra = bd_quest_socio_notas_deficiencia.buscar_dataframe_no_banco(
                    Amostra, 
                    filtro_sexo=filtro_sexo,                
                    filtro_amostra=filtro_amostra, 
                    filtro_cor=filtro_cor, 
                    filtro_estado=filtro_estado, 
                    filtro_recurso=filtro_recurso, 
                    filtro_localizacao_da_escola=filtro_localizacao_da_escola, 
                    filtro_estado_civil=filtro_estado_civil, 
                    filtro_escola=filtro_escola, 
                    filtro_nacionalidade=filtro_nacionalidade,
                    filtro_ano=filtro_ano)
        else:
            if(Q=='nenhum'):            
                Amostra = [prova]
            else:
                Amostra = [prova, Q]
            if(filtro_deficiencia != 'todas' and filtro_deficiencia != 'nenhuma'):
                Microdado_Amostra = bd_quest_socio_notas_deficiencia.buscar_dataframe_no_banco(
                    Amostra,              
                    filtro_amostra=filtro_amostra, 
                    filtro_deficiencia=filtro_deficiencia,
                    filtro_cor=filtro_cor, 
                    filtro_estado=filtro_estado, 
                    filtro_recurso=filtro_recurso, 
                    filtro_localizacao_da_escola=filtro_localizacao_da_escola, 
                    filtro_estado_civil=filtro_estado_civil, 
                    filtro_escola=filtro_escola, 
                    filtro_nacionalidade=filtro_nacionalidade,
                    filtro_ano=filtro_ano)
            else:
                Microdado_Amostra = bd_quest_socio_notas_deficiencia.buscar_dataframe_no_banco(
                    Amostra,                
                    filtro_amostra=filtro_amostra, 
                    filtro_cor=filtro_cor, 
                    filtro_estado=filtro_estado, 
                    filtro_recurso=filtro_recurso, 
                    filtro_localizacao_da_escola=filtro_localizacao_da_escola, 
                    filtro_estado_civil=filtro_estado_civil, 
                    filtro_escola=filtro_escola, 
                    filtro_nacionalidade=filtro_nacionalidade,
                    filtro_ano=filtro_ano)
            
        if(filtro_ano=="2019"):
            CONTAGEMMicrodado_Amostra = 3702008
        elif(filtro_ano=="2018"):
            # CONTAGEMMicrodado_Amostra = 3893743
            CONTAGEMMicrodado_Amostra = 3893671
        elif(filtro_ano=="2017"):
            CONTAGEMMicrodado_Amostra = 4426755
            
        CONTAGEM = Microdado_Amostra[prova].count()
        
        if(CONTAGEM==0):
            menssagem = """Nenhum aluno com esse perfil:"""
            menssagem1 = """Nenhum aluno com esse perfil:"""
            context = {
                'form' : form,
                'menssagem' : menssagem,
                'menssagem1' : menssagem1,
                'form_filtro' : form_filtro
            }

            return render(request, 'base/formulario_2/relatorio_formulario_2.html', context=context)
    
        width = 0.25         # A largura das barras
        
        Dataframe = Microdado_Amostra.filter(items = Amostra)
            
        if Q == 'nenhum':
            Dataframe = Microdado_Amostra
            print('--------------------------------------------------------------------')
            print(Dataframe) 
            print('--------------------------------------------------------------------')
            Dataframe = Dataframe.describe().T
        else:
            Dataframe = Dataframe.sort_values(by=[Q])
            Dataframe = Dataframe.groupby(Q)[prova]    
            Dataframe = Dataframe.describe()    
            
            
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

        
        if(Q=="nenhum"):
            
            relatorio_em_grafico=""
            anotacao_mensagem=""
            
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
                xaxis_title="Resposta do questionário socioeconômico",
                yaxis_title="Desempenho",
                yaxis2 = {'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'},
                legend_title="Legenda",
                annotations = [
                    {
                        'x': 0,
                        'y': -0.6,
                        'xref': "paper",
                        'yref': "paper",
                        'text': """Informativo:
                            <br>- Na primeira seção da tela, há um quadro com dados sobre a média das notas dos alunos que você selecionou<br> usando os filtros do formulário logo acima.
                            <br>- Nesse mesmo quadro, você também encontrará a maior nota obtida na prova, a menor nota e os quartis. 
                            <br>- É importante salientar que os quartis são valores que dividem o conjunto de dados em quatro partes iguais, <br>sendo que 25% é o quartil 1, 50%(que é a mediana) é o quartil 2 e 75% é o quartil 3.
                            <br>- Na seção seguinte, há um gráfico que ilustra claramente a diferença entre a nota mínima, a média e a nota máxima.""",
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
            anotacao_mensagem = anotacao(Q)
            relatorio_em_grafico = go.Figure()
            nome = "Mínino"
            relatorio_em_grafico.add_bar(
                y=(Dataframe['min']),
                x=Dataframe.index,
                text=(Dataframe['min']),
                texttemplate='%{text:.2f}',
                textposition='auto',
                name=nome
            )
            nome = "Média"
            relatorio_em_grafico.add_bar(
                y=(Dataframe['mean']),
                x=Dataframe.index,
                text=(Dataframe['mean']),
                texttemplate='%{text:.2f}',
                textposition='auto',
                name=nome
            )
            nome = "Máximo"
            relatorio_em_grafico.add_bar(
                y=(Dataframe['max']),
                x=Dataframe.index,
                text=(Dataframe['max']),
                texttemplate='%{text:.2f}',
                textposition='auto',
                name=nome
            )
            
            figura_tabela.update_layout(
                title_text = "Quadro de correlação entre a nota da prova: "+prova+" e a resposta socioeconômica da questão: "+Q,
                height=400,
                margin=dict(l=50, r=50, b=20, t=50),
                yaxis = {'domain': [0, .45]},
                xaxis2 = {'anchor': 'y2'},
                xaxis_title="Resposta do questionário socioeconômico",
                yaxis_title=("Desempenho na prova:"+prova),
                yaxis2 = {'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'},
                legend_title="Legenda",
                font=dict(
                    family="Arial",
                    size=12,
                    color="black"
                )
            )
            relatorio_em_grafico.update_layout(
                title_text = "Gráfico de correlação entre a nota da prova: "+prova+" e a resposta socioeconômica da questão: "+Q,
                # margin=dict(l=50, r=50, b=20, t=0),
                # yaxis = {'domain': [0, .1]},
                xaxis2 = {'anchor': 'y2'},
                xaxis_title=("Resposta do questionário socioeconômico da questão: "+Q),
                yaxis_title=("Desempenho na prova: "+prova),
                yaxis2 = {'domain': [.1, 0], 'anchor': 'x2', 'title': 'Goals'},
                legend_title="Legenda",
                font=dict(
                    family="Arial",
                    size=12,
                    color="black"
                )
            )
            
            relatorio_em_grafico = relatorio_em_grafico.to_html()

        relatorio_em_tabela = figura_tabela.to_html()

        if form.is_valid():
            print(form.changed_data)
        else:
            pass

        menssagem1 = """Formulário da análise do Desempenho do inscrito em relação aos dados socioêconomicos :"""
        menssagem = """Correlação entre as respostas do questionário socioeconômico e
        o desempenho no exame."""

        if(anotacao_mensagem!=""):
            anotacao_quadro = anotacao_mensagem[0]
            anotacao_mensagem = anotacao_mensagem[1]
            anotacao_mensagem = anotacao_mensagem.split('\n')
            anotacao_mensagem = format_html_join(
                '\n', '<div class="col-md-11 mt-2"><h6 class="font-weight-normal mb-0">{}</h6></div>', ((line,) for line in anotacao_mensagem))
            
            anotacao_quadro = anotacao_quadro.split('\n')
            anotacao_quadro = format_html_join(
                '\n', '<div class="col-md-11 mt-2"><h6 class="font-weight-normal mb-0">{}</h6></div>', ((line,) for line in anotacao_quadro))
            
            # Cria a mensagem de anotação
            informativo = '<h5 class="mb-0">Informativo:</h5>'

            # Formata a mensagem em HTML
            anotacao_mensagem = f'<div class="col-md-11 border"><div class="col-md-11 mt-2">{informativo}</div><hr class="mt-0">{anotacao_quadro}<hr class="mt-0">{anotacao_mensagem}</div>'
        
        context = {
            'form' : form,
            'menssagem' : menssagem,
            'anotacao_mensagem' : anotacao_mensagem,
            'menssagem1' : menssagem1,
            'form_filtro' : form_filtro,
            'quantidadeParcial' : CONTAGEM,
            'relatorio_em_tabela' : relatorio_em_tabela,
            'relatorio_em_grafico' : relatorio_em_grafico,
            'quantidadeTotal' : CONTAGEMMicrodado_Amostra,
            'figura_com_criador_de_tabela' : figura_com_criador_de_tabela,
        }

    return render(request, 'base/formulario_2/relatorio_formulario_2.html', context=context)
    
