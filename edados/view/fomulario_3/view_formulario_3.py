
from edados.formularios.filtros.formulario_1_filtros import Formulario_filtros
from edados.formularios.formulario_3.formulario_3 import Formulario_3
from edados.formularios.formulario_3.formulario_3 import Formulario_3_2
from django.contrib.auth.decorators import login_required
from django.utils.html import format_html_join
from edados.database import bd_formulario_3
from django.shortcuts import render
import plotly.graph_objects as go
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

CONTAGEM = 0
CONTAGEMMicrodado_Amostra = 0
prova_pdf = ""

def formatar(valor):
    return "{:,.2f}".format(valor)

def prova_nome_pdf(filtro_cor_da_prova):
    if('503'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_07_DIA_2_AZUL.pdf"
    elif('504'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_05_DIA_2_AMARELO.pdf"
    elif('505'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_06_DIA_2_CINZA.pdf"
    elif('506'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_08_DIA_2_ROSA.pdf"
    elif('507'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_01_DIA_1_AZUL.pdf"
    elif('508'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_02_DIA_1_AMARELO.pdf"
    elif('509'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_03_DIA_1_BRANCO.pdf"
    elif('510'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_04_DIA_1_ROSA.pdf"
    elif('511'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_01_DIA_1_AZUL.pdf"
    elif('512'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_02_DIA_1_AMARELO.pdf"
    elif('513'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_04_DIA_1_ROSA.pdf"
    elif('514'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_03_DIA_1_BRANCO.pdf"
    elif('515'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_07_DIA_2_AZUL.pdf"
    elif('516'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_05_DIA_2_AMARELO.pdf"
    elif('517'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_08_DIA_2_ROSA.pdf"
    elif('518'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_06_DIA_2_CINZA.pdf"
    elif('519'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_11_DIA_2_LARANJA_LEDOR.pdf"
    elif('520'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
    elif('521'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
    elif('522'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_11_DIA_2_LARANJA_LEDOR.pdf"
    elif('523'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_12_DIA_2_VERDE_LIBRAS.pdf"
    elif('524'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_10_DIA_1_VERDE_LIBRAS.pdf"
    elif('525'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_10_DIA_1_VERDE_LIBRAS.pdf"
    elif('526'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_12_DIA_2_VERDE_LIBRAS.pdf"
    elif('527'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_01_DIA_1_AZUL.pdf"
    elif('528'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_02_DIA_1_AMARELO.pdf"
    elif('529'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_02_DIA_1_AMARELO_AMPLIADA.pdf"
    elif('530'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_02_DIA_1_AMARELO_SUPERAMPLIADA.pdf"
    elif('531'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_03_DIA_1_BRANCO.pdf"
    elif('532'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_04_DIA_1_ROSA.pdf"
    elif('533'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
    elif('534'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_10_DIA_1_VERDE_LIBRAS.pdf"
    elif('535'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_05_DIA_2_AMARELO.pdf"
    elif('536'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_06_DIA_2_CINZA.pdf"
    elif('537'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_06_DIA_2_CINZA_AMPLIADA.pdf"
    elif('538'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_06_DIA_2_CINZA_SUPERAMPLIADA.pdf"
    elif('539'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_07_DIA_2_AZUL.pdf"
    elif('540'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_08_DIA_2_ROSA.pdf"
    elif('541'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_11_DIA_2_LARANJA_LEDOR.pdf"
    elif('542'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P1_CAD_12_DIA_2_VERDE_LIBRAS.pdf"
    elif('543'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_05_DIA_2_AMARELO.pdf"
    elif('544'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_06_DIA_2_CINZA.pdf"
    elif('545'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_07_DIA_2_AZUL.pdf"
    elif('546'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_08_DIA_2_ROSA.pdf"
    elif('547'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_01_DIA_1_AZUL.pdf"
    elif('548'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_02_DIA_1_AMARELO.pdf"
    elif('549'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_03_DIA_1_BRANCO.pdf"
    elif('550'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_04_DIA_1_ROSA.pdf"
    elif('551'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_01_DIA_1_AZUL.pdf"
    elif('552'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_02_DIA_1_AMARELO.pdf"
    elif('553'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_03_DIA_1_BRANCO.pdf"
    elif('554'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_04_DIA_1_ROSA.pdf"
    elif('555'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_05_DIA_2_AMARELO.pdf"
    elif('556'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_06_DIA_2_CINZA.pdf"
    elif('557'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_07_DIA_2_AZUL.pdf"
    elif('558'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_08_DIA_2_ROSA.pdf"
    elif('559'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
    elif('560'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
    elif('561'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_03_DIA_1_BRANCO.pdf"
    elif('562'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_04_DIA_1_ROSA.pdf"
    elif('563'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
    elif('564'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
    elif('565'==filtro_cor_da_prova):
        prova_pdf="ENEM_2019_P2_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
    else:
        prova_pdf = "desenvolvimento.pdf"
            
    print('@------------------------------------------------------------@')
    print(filtro_cor_da_prova)
    
    return prova_pdf

@login_required
def formulario_2(request):

    if request.method == 'GET':
        menssagem = 'Análise do Desempenho Acadêmico: Quantidade de Acertos e Erros por Prova e Aplicação de Filtros'
        menssagem_informativa = """A análise de dados é uma das habilidades mais importantes na era digital em que vivemos, e é especialmente útil quando se trata de quantificar o desempenho em testes como o Exame Nacional do Ensino Médio (ENEM). Uma plataforma online com filtros pode ser uma ferramenta poderosa para analisar dados do ENEM e determinar o nível de sucesso de um determinado grupo de estudantes.

        Usando uma plataforma online com filtros, é possível analisar vários dados do ENEM, como a nota geral, a pontuação em cada área de conhecimento e a nota de redação. Além disso, é possível filtrar esses dados por região, tipo de escola, renda familiar, entre outros fatores.

        Com essa plataforma, é possível determinar o nível de sucesso de um determinado grupo de estudantes, comparando-os com o desempenho geral de outros grupos. Por exemplo, é possível analisar os dados dos estudantes de uma determinada escola de ensino médio em relação aos dados gerais de todas as escolas de ensino médio na região.

        Essa análise de dados pode ajudar a identificar possíveis áreas de melhoria no processo de ensino e aprendizagem, permitindo que os educadores tomem decisões informadas sobre a forma como ensinam e avaliam os alunos. Também pode ajudar a identificar os estudantes que precisam de mais apoio e fornecer informações valiosas para os pais sobre o desempenho dos seus filhos.


        Em resumo, a análise de dados usando uma plataforma online com filtros pode fornecer informações valiosas sobre o desempenho dos alunos no ENEM, ajudando a identificar áreas de melhoria e fornecer informações importantes para os educadores e pais."""
        
        menssagem_informativa = menssagem_informativa.split('\n')
        menssagem_informativa = format_html_join('\n', '<p>{}</p>', ((line,) for line in menssagem_informativa))
        

        form = Formulario_3_2()
        form_filtro_grupo_A = Formulario_filtros(prefix='grupo_A')
        form_filtro_grupo_B = Formulario_filtros(prefix='grupo_B')

        context = {
            'form' : form,
            'menssagem' : menssagem,
            'menssagem_informativa' : menssagem_informativa,            
            'form_filtro_grupo_A' : form_filtro_grupo_A,
            'form_filtro_grupo_B' : form_filtro_grupo_B,
        }
        return render(request, 'base/formulario_3/quest_formulario_3_2.html', context=context)
    else:


        # Recebendo fomulario da tela
        form = Formulario_3_2(request.POST)
        # form_filtro = Formulario_filtros(request.POST)
        
        form_filtro_grupo_A = Formulario_filtros(request.POST, prefix='grupo_A')
        form_filtro_grupo_B = Formulario_filtros(request.POST, prefix='grupo_B')

        acerto_erro = form.data['acerto_erro']
        filtro_ano = form.data['ano']

        if form_filtro_grupo_A.is_valid() and form_filtro_grupo_B.is_valid():
            
            # Formulario de Filtro do GRUPO A
            filtro_deficiencia = form_filtro_grupo_A.cleaned_data['deficiencia']
            filtro_estado_civil = form_filtro_grupo_A.cleaned_data['estado_civil']
            filtro_cor = form_filtro_grupo_A.cleaned_data['cor']
            filtro_sexo = form_filtro_grupo_A.cleaned_data['sexo']
            filtro_estado = form_filtro_grupo_A.cleaned_data['estado']
            filtro_cidade = form_filtro_grupo_A.cleaned_data['cidade']
            filtro_amostra = form_filtro_grupo_A.cleaned_data['amostra']
            filtro_recurso = form_filtro_grupo_A.cleaned_data['recurso']
            filtro_localizacao_da_escola = form_filtro_grupo_A.cleaned_data['localizacao_da_escola']
        
            # Formulario de Filtro do GRUPO B
            filtro_deficiencia_grupo_B = form_filtro_grupo_B.cleaned_data['deficiencia']
            filtro_estado_civil_grupo_B = form_filtro_grupo_B.cleaned_data['estado_civil']
            filtro_cor_grupo_B = form_filtro_grupo_B.cleaned_data['cor']
            filtro_sexo_grupo_B = form_filtro_grupo_B.cleaned_data['sexo']
            filtro_estado_grupo_B = form_filtro_grupo_B.cleaned_data['estado']
            filtro_cidade_grupo_B = form_filtro_grupo_B.cleaned_data['cidade']
            filtro_amostra_grupo_B = form_filtro_grupo_B.cleaned_data['amostra']
            filtro_recurso_grupo_B = form_filtro_grupo_B.cleaned_data['recurso']
            filtro_localizacao_da_escola_grupo_B = form_filtro_grupo_B.cleaned_data['localizacao_da_escola']
        
        print("-----------------------------------------------------------------------------")
        print(filtro_amostra_grupo_B)
        print("filtro_amostra_grupo_B")
        print("-----------------------------------------------------------------------------")
        # Variáveis vindas do Formulario
        if (filtro_ano=="2019"):
            filtro_cor_da_prova = request.POST.get('cor_da_prova_2019')
            print(filtro_cor_da_prova)
        elif (filtro_ano=="2018"):
            filtro_cor_da_prova = request.POST.get('cor_da_prova_2018')
            print(filtro_cor_da_prova)
        elif (filtro_ano=="2017"):
            filtro_cor_da_prova = request.POST.get('cor_da_prova_2017')
            print(filtro_cor_da_prova)

        filtro_cor_da_prova1 = request.POST.get('prova1')
        filtro_cor_da_prova2 = request.POST.get('prova2')
        filtro_cor_da_prova3 = request.POST.get('prova3')
        filtro_cor_da_prova4 = request.POST.get('prova4')
        
        questao1 = request.POST.get('questao1')
        questao2 = request.POST.get('questao2')
        questao3 = request.POST.get('questao3')
        questao4 = request.POST.get('questao4')
        
        if (questao3=="Nenhuma"):
            filtro_cor_da_prova3 = "Nenhuma"
        if (questao4=="Nenhuma"):
            filtro_cor_da_prova4 = "Nenhuma"
        

        prova_pdf = prova_nome_pdf(filtro_cor_da_prova=filtro_cor_da_prova1)
        prova_pdf = '/pdf/PROVAS_E_GABARITOS/'+prova_pdf

        if (filtro_ano=="2019"):
            if( filtro_cor_da_prova1 == '503' or 
                filtro_cor_da_prova1 == '504' or
                filtro_cor_da_prova1 == '505' or
                filtro_cor_da_prova1 == '506' or
                filtro_cor_da_prova1 == '519' or
                filtro_cor_da_prova1 == '523' or
                filtro_cor_da_prova1 == '543' or
                filtro_cor_da_prova1 == '544' or
                filtro_cor_da_prova1 == '545' or
                filtro_cor_da_prova1 == '546'):
                prova = 'CO_PROVA_CN'
            elif(
                filtro_cor_da_prova1 == '507' or 
                filtro_cor_da_prova1 == '508' or
                filtro_cor_da_prova1 == '509' or
                filtro_cor_da_prova1 == '510' or
                filtro_cor_da_prova1 == '520' or
                filtro_cor_da_prova1 == '524' or
                filtro_cor_da_prova1 == '547' or
                filtro_cor_da_prova1 == '548' or
                filtro_cor_da_prova1 == '549' or
                filtro_cor_da_prova1 == '550' or
                filtro_cor_da_prova1 == '564'):
                prova = 'CO_PROVA_CH'
            elif(
                filtro_cor_da_prova1 == '511' or 
                filtro_cor_da_prova1 == '512' or
                filtro_cor_da_prova1 == '513' or
                filtro_cor_da_prova1 == '514' or
                filtro_cor_da_prova1 == '521' or
                filtro_cor_da_prova1 == '525' or
                filtro_cor_da_prova1 == '551' or
                filtro_cor_da_prova1 == '552' or
                filtro_cor_da_prova1 == '553' or
                filtro_cor_da_prova1 == '554' or
                filtro_cor_da_prova1 == '565'):
                prova = 'CO_PROVA_LC'
            elif(
                filtro_cor_da_prova1 == '515' or
                filtro_cor_da_prova1 == '516' or
                filtro_cor_da_prova1 == '517' or
                filtro_cor_da_prova1 == '518' or
                filtro_cor_da_prova1 == '522' or
                filtro_cor_da_prova1 == '526' or
                filtro_cor_da_prova1 == '555' or
                filtro_cor_da_prova1 == '556' or
                filtro_cor_da_prova1 == '557' or
                filtro_cor_da_prova1 == '558'):
                prova = 'CO_PROVA_MT'
            else:
                prova = 'CO_PROVA_MT'
        elif (filtro_ano=="2018"):
            if( filtro_cor_da_prova1 == '447' or 
                filtro_cor_da_prova1 == '448' or
                filtro_cor_da_prova1 == '449' or
                filtro_cor_da_prova1 == '450' or
                filtro_cor_da_prova1 == '463' or
                filtro_cor_da_prova1 == '467' or
                filtro_cor_da_prova1 == '487' or
                filtro_cor_da_prova1 == '488' or
                filtro_cor_da_prova1 == '489' or
                filtro_cor_da_prova1 == '490'):
                prova = 'CO_PROVA_CN'
            elif(
                filtro_cor_da_prova1 == '451' or 
                filtro_cor_da_prova1 == '452' or
                filtro_cor_da_prova1 == '453' or
                filtro_cor_da_prova1 == '454' or
                filtro_cor_da_prova1 == '464' or
                filtro_cor_da_prova1 == '468' or
                filtro_cor_da_prova1 == '491' or
                filtro_cor_da_prova1 == '492' or
                filtro_cor_da_prova1 == '493' or
                filtro_cor_da_prova1 == '494'):
                prova = 'CO_PROVA_CH'
            elif(
                filtro_cor_da_prova1 == '455' or 
                filtro_cor_da_prova1 == '456' or
                filtro_cor_da_prova1 == '457' or
                filtro_cor_da_prova1 == '458' or
                filtro_cor_da_prova1 == '465' or
                filtro_cor_da_prova1 == '469' or
                filtro_cor_da_prova1 == '495' or
                filtro_cor_da_prova1 == '496' or
                filtro_cor_da_prova1 == '497' or
                filtro_cor_da_prova1 == '498' ):
                prova = 'CO_PROVA_LC'
            elif(
                filtro_cor_da_prova1 == '459' or
                filtro_cor_da_prova1 == '460' or
                filtro_cor_da_prova1 == '461' or
                filtro_cor_da_prova1 == '462' or
                filtro_cor_da_prova1 == '466' or
                filtro_cor_da_prova1 == '470' or
                filtro_cor_da_prova1 == '499' or
                filtro_cor_da_prova1 == '500' or
                filtro_cor_da_prova1 == '501' or
                filtro_cor_da_prova1 == '502'):
                prova = 'CO_PROVA_MT'
            else:
                prova = 'CO_PROVA_MT'
        elif (filtro_ano=="2017"):
            if( filtro_cor_da_prova1 == '391' or 
                filtro_cor_da_prova1 == '392' or
                filtro_cor_da_prova1 == '393' or
                filtro_cor_da_prova1 == '394' or
                filtro_cor_da_prova1 == '407' or
                filtro_cor_da_prova1 == '411' or
                filtro_cor_da_prova1 == '431' or
                filtro_cor_da_prova1 == '432' or
                filtro_cor_da_prova1 == '433' or
                filtro_cor_da_prova1 == '434'):
                prova = 'CO_PROVA_CN'
            elif(
                filtro_cor_da_prova1 == '395' or 
                filtro_cor_da_prova1 == '396' or
                filtro_cor_da_prova1 == '397' or
                filtro_cor_da_prova1 == '398' or
                filtro_cor_da_prova1 == '408' or
                filtro_cor_da_prova1 == '412' or
                filtro_cor_da_prova1 == '435' or
                filtro_cor_da_prova1 == '436' or
                filtro_cor_da_prova1 == '437' or
                filtro_cor_da_prova1 == '438'):
                prova = 'CO_PROVA_CH'
            elif(
                filtro_cor_da_prova1 == '399' or 
                filtro_cor_da_prova1 == '400' or
                filtro_cor_da_prova1 == '401' or
                filtro_cor_da_prova1 == '402' or
                filtro_cor_da_prova1 == '409' or
                filtro_cor_da_prova1 == '413' or
                filtro_cor_da_prova1 == '439' or
                filtro_cor_da_prova1 == '440' or
                filtro_cor_da_prova1 == '441' or
                filtro_cor_da_prova1 == '442'):
                prova = 'CO_PROVA_LC'
            elif(
                filtro_cor_da_prova1 == '403' or
                filtro_cor_da_prova1 == '404' or
                filtro_cor_da_prova1 == '405' or
                filtro_cor_da_prova1 == '406' or
                filtro_cor_da_prova1 == '410' or
                filtro_cor_da_prova1 == '414' or
                filtro_cor_da_prova1 == '443' or
                filtro_cor_da_prova1 == '444' or
                filtro_cor_da_prova1 == '445' or
                filtro_cor_da_prova1 == '446'):
                prova = 'CO_PROVA_MT'
            else:
                prova = 'CO_PROVA_MT'
        
        # Formulario de Filtro
        if prova == 'CO_PROVA_LC':
            respostas = "TX_RESPOSTAS_LC"
            gabarito = "TX_GABARITO_LC"
        elif prova == 'CO_PROVA_CN':
            respostas = "TX_RESPOSTAS_CN"
            gabarito = "TX_GABARITO_CN"
        elif prova == 'CO_PROVA_MT':
            respostas = "TX_RESPOSTAS_MT"
            gabarito = "TX_GABARITO_MT"
        elif prova == 'CO_PROVA_CH':
            respostas = "TX_RESPOSTAS_CH"
            gabarito = "TX_GABARITO_CH"

        if(filtro_sexo != 'todos'):
            Amostra = [prova, 'TP_SEXO', respostas, gabarito]
            Microdado_Prova1 = bd_formulario_3.buscar_dataframe_no_banco(
                Amostra, 
                filtro_sexo=filtro_sexo, 
                filtro_cidade=filtro_cidade, 
                filtro_cor_da_prova=filtro_cor_da_prova1, 
                filtro_deficiencia=filtro_deficiencia,
                filtro_amostra=filtro_amostra, 
                filtro_cor=filtro_cor, 
                filtro_estado=filtro_estado, 
                filtro_recurso=filtro_recurso,
                filtro_localizacao_da_escola=filtro_localizacao_da_escola, 
                filtro_estado_civil=filtro_estado_civil, 
                filtro_ano=filtro_ano)
            Microdado_Prova2 = bd_formulario_3.buscar_dataframe_no_banco(
                Amostra, 
                filtro_sexo=filtro_sexo_grupo_B, 
                filtro_cidade=filtro_cidade_grupo_B, 
                filtro_cor_da_prova=filtro_cor_da_prova2, 
                filtro_deficiencia=filtro_deficiencia_grupo_B,
                filtro_amostra=filtro_amostra_grupo_B, 
                filtro_cor=filtro_cor_grupo_B,   
                filtro_estado=filtro_estado_grupo_B, 
                filtro_recurso=filtro_recurso_grupo_B,
                filtro_localizacao_da_escola=filtro_localizacao_da_escola_grupo_B, 
                filtro_estado_civil=filtro_estado_civil_grupo_B, 
                filtro_ano=filtro_ano)
            if(filtro_cor_da_prova3!='Nenhuma'):                
                Microdado_Prova3 = bd_formulario_3.buscar_dataframe_no_banco(
                    Amostra, 
                    filtro_sexo=filtro_sexo_grupo_B, 
                    filtro_cidade=filtro_cidade_grupo_B, 
                    filtro_cor_da_prova=filtro_cor_da_prova3, 
                    filtro_deficiencia=filtro_deficiencia_grupo_B,
                    filtro_amostra=filtro_amostra_grupo_B, 
                    filtro_cor=filtro_cor_grupo_B,   
                    filtro_estado=filtro_estado_grupo_B, 
                    filtro_recurso=filtro_recurso_grupo_B,
                    filtro_localizacao_da_escola=filtro_localizacao_da_escola_grupo_B, 
                    filtro_estado_civil=filtro_estado_civil_grupo_B, 
                    filtro_ano=filtro_ano)
            if(filtro_cor_da_prova4!='Nenhuma'):                
                Microdado_Prova4 = bd_formulario_3.buscar_dataframe_no_banco(
                    Amostra, 
                    filtro_sexo=filtro_sexo_grupo_B, 
                    filtro_cidade=filtro_cidade_grupo_B, 
                    filtro_cor_da_prova=filtro_cor_da_prova4, 
                    filtro_deficiencia=filtro_deficiencia_grupo_B,
                    filtro_amostra=filtro_amostra_grupo_B, 
                    filtro_cor=filtro_cor_grupo_B,   
                    filtro_estado=filtro_estado_grupo_B, 
                    filtro_recurso=filtro_recurso_grupo_B,
                    filtro_localizacao_da_escola=filtro_localizacao_da_escola_grupo_B, 
                    filtro_estado_civil=filtro_estado_civil_grupo_B, 
                    filtro_ano=filtro_ano)
        else:
            Amostra = [prova, respostas, gabarito]
            Microdado_Prova1 = bd_formulario_3.buscar_dataframe_no_banco(
                Amostra, 
                filtro_sexo=filtro_sexo, 
                filtro_cidade=filtro_cidade, 
                filtro_cor_da_prova=filtro_cor_da_prova1, 
                filtro_deficiencia=filtro_deficiencia,
                filtro_amostra=filtro_amostra,    
                filtro_cor=filtro_cor, 
                filtro_estado=filtro_estado, 
                filtro_recurso=filtro_recurso,
                filtro_localizacao_da_escola=filtro_localizacao_da_escola, 
                filtro_estado_civil=filtro_estado_civil, 
                filtro_ano=filtro_ano)
            
            Microdado_Prova2 = bd_formulario_3.buscar_dataframe_no_banco(
                Amostra, 
                filtro_sexo=filtro_sexo_grupo_B, 
                filtro_cidade=filtro_cidade_grupo_B, 
                filtro_cor_da_prova=filtro_cor_da_prova2, 
                filtro_deficiencia=filtro_deficiencia_grupo_B,
                filtro_amostra=filtro_amostra_grupo_B,    
                filtro_cor=filtro_cor_grupo_B, 
                filtro_estado=filtro_estado_grupo_B, 
                filtro_recurso=filtro_recurso_grupo_B,
                filtro_localizacao_da_escola=filtro_localizacao_da_escola_grupo_B, 
                filtro_estado_civil=filtro_estado_civil_grupo_B, 
                filtro_ano=filtro_ano)
        
            if(filtro_cor_da_prova3!='Nenhuma'):                
                Microdado_Prova3 = bd_formulario_3.buscar_dataframe_no_banco(
                    Amostra, 
                    filtro_sexo=filtro_sexo_grupo_B, 
                    filtro_cidade=filtro_cidade_grupo_B, 
                    filtro_cor_da_prova=filtro_cor_da_prova3, 
                    filtro_deficiencia=filtro_deficiencia_grupo_B,
                    filtro_amostra=filtro_amostra_grupo_B, 
                    filtro_cor=filtro_cor_grupo_B,   
                    filtro_estado=filtro_estado_grupo_B, 
                    filtro_recurso=filtro_recurso_grupo_B,
                    filtro_localizacao_da_escola=filtro_localizacao_da_escola_grupo_B, 
                    filtro_estado_civil=filtro_estado_civil_grupo_B, 
                    filtro_ano=filtro_ano)
            if(filtro_cor_da_prova4!='Nenhuma'):                
                Microdado_Prova4 = bd_formulario_3.buscar_dataframe_no_banco(
                    Amostra, 
                    filtro_sexo=filtro_sexo_grupo_B, 
                    filtro_cidade=filtro_cidade_grupo_B, 
                    filtro_cor_da_prova=filtro_cor_da_prova4, 
                    filtro_deficiencia=filtro_deficiencia_grupo_B,
                    filtro_amostra=filtro_amostra_grupo_B, 
                    filtro_cor=filtro_cor_grupo_B,   
                    filtro_estado=filtro_estado_grupo_B, 
                    filtro_recurso=filtro_recurso_grupo_B,
                    filtro_localizacao_da_escola=filtro_localizacao_da_escola_grupo_B, 
                    filtro_estado_civil=filtro_estado_civil_grupo_B, 
                    filtro_ano=filtro_ano)
                
        if(filtro_ano=="2019"):
            CONTAGEMMicrodado_Amostra = 3702008
        elif(filtro_ano=="2018"):
            # CONTAGEMMicrodado_Amostra = 3893743
            CONTAGEMMicrodado_Amostra = 3893671
        elif(filtro_ano=="2017"):
            CONTAGEMMicrodado_Amostra = 4426755
        CONTAGEM = Microdado_Prova1[prova].count()
        
        menssagem = 'Análise do Desempenho Acadêmico: Quantidade de Acertos e Erros por Prova e Aplicação de Filtros'

        # Resetar o índice do DataFrame Microdado_Prova1
        Microdado_Prova1.reset_index(inplace=True)

        # Extrair as respostas da prova 1
        resposta = Microdado_Prova1[respostas]
        quantidade_de_respostas =  (Microdado_Prova1[respostas].count()-1)
        quantidadeParcial_grupo_A = Microdado_Prova1[respostas].count() 
        gabarito_prova1 = Microdado_Prova1[gabarito]

        acertos = [0] * 2
        acertos_porcentagem = [0] * 1

        if quantidade_de_respostas >= 0:
            linha_do_gabarito = gabarito_prova1.iloc[quantidade_de_respostas]
        
        print(linha_do_gabarito)

        j = 1
        questao1 = int(questao1)-1

        for i in range(quantidade_de_respostas):
            if resposta[i] == '':
                resposta[i] = "............................................."
            linha_da_resposta = resposta[i]

            resposta_gabarito = linha_do_gabarito[questao1]
            resposta_candidato = linha_da_resposta[questao1]

            if acerto_erro == 'acertos':
                if resposta_candidato == resposta_gabarito:
                    acertos[j] += 1
                    resposta_candidato = ''
            else:
                if resposta_candidato != resposta_gabarito:
                    acertos[j] += 1
                    resposta_candidato = ''

        acertos_porcentagem[0] = (acertos[j] / quantidade_de_respostas) * 100

        acertos_pd_prova1 = pd.DataFrame(acertos_porcentagem)
        acertos_pd_prova1 = acertos_pd_prova1.reset_index(drop=True)
        acertos_pd_prova1.index = acertos_pd_prova1.index + int(questao1)

        # Resetar o índice do DataFrame Microdado_Prova2
        Microdado_Prova2.reset_index(inplace=True)

        # Extrair as respostas da prova 2
        resposta = Microdado_Prova2[respostas]
        quantidade_de_respostas = Microdado_Prova2[respostas].count() - 1
        quantidadeParcial_grupo_B = Microdado_Prova2[respostas].count()
        gabarito_prova2 = Microdado_Prova2[gabarito]

        acertos = [0] * 2
        acertos_porcentagem = [0] * 1

        if quantidade_de_respostas >= 0:
            linha_do_gabarito = gabarito_prova2.iloc[quantidade_de_respostas]

        j = 1
        questao2 = int(questao2)-1

        for i in range(quantidade_de_respostas):
            if resposta[i] == '':
                resposta[i] = "............................................."
            linha_da_resposta = resposta[i]

            resposta_gabarito = linha_do_gabarito[questao2]
            resposta_candidato = linha_da_resposta[questao2]

            if acerto_erro == 'acertos':
                if resposta_candidato == resposta_gabarito:
                    acertos[j] += 1
                    resposta_candidato = ''
            else:
                if resposta_candidato != resposta_gabarito:
                    acertos[j] += 1
                    resposta_candidato = ''

        acertos_porcentagem[0] = (acertos[j] / quantidade_de_respostas) * 100

        acertos_pd_prova2 = pd.DataFrame(acertos_porcentagem)
        acertos_pd_prova2 = acertos_pd_prova2.reset_index(drop=True)
        acertos_pd_prova2.index = acertos_pd_prova2.index + int(questao2)
        print("==========================================================")
        print("acertos_pd_prova2.index")
        print(acertos_pd_prova2.index[0])
        print("==========================================================")
        
        # PROVA 3
        
        if(filtro_cor_da_prova3!='Nenhuma'):  
            # Resetar o índice do DataFrame Microdado_Prova3
            Microdado_Prova3.reset_index(inplace=True)

            # Extrair as respostas da prova 3
            resposta = Microdado_Prova3[respostas]
            quantidade_de_respostas = Microdado_Prova3[respostas].count() - 1
            gabarito_prova3 = Microdado_Prova3[gabarito]

            acertos = [0] * 2
            acertos_porcentagem = [0] * 1

            if quantidade_de_respostas >= 0:
                linha_do_gabarito = gabarito_prova3.iloc[quantidade_de_respostas]

            j = 0
            questao3 = int(questao3)-1

            for i in range(quantidade_de_respostas):
                if resposta[i] == '':
                    resposta[i] = "............................................."
                linha_da_resposta = resposta[i]

                resposta_gabarito = linha_do_gabarito[questao3]
                resposta_candidato = linha_da_resposta[questao3]

                if acerto_erro == 'acertos':
                    if resposta_candidato == resposta_gabarito:
                        acertos[j] += 1
                        resposta_candidato = ''
                else:
                    if resposta_candidato != resposta_gabarito:
                        acertos[j] += 1
                        resposta_candidato = ''

            acertos_porcentagem[0] = (acertos[j] / quantidade_de_respostas) * 100

            acertos_pd_prova3 = pd.DataFrame(acertos_porcentagem)
            acertos_pd_prova3 = acertos_pd_prova3.reset_index(drop=True)
            acertos_pd_prova3.index = acertos_pd_prova3.index + int(questao3)            
        # FINAL PROVA 3
        
        # PROVA 4        
        if(filtro_cor_da_prova4!='Nenhuma'):  
            # Resetar o índice do DataFrame Microdado_Prova3
            Microdado_Prova4.reset_index(inplace=True)

            # Extrair as respostas da prova 3
            resposta = Microdado_Prova4[respostas]
            quantidade_de_respostas = Microdado_Prova4[respostas].count() - 1
            quantidadeParcial_grupo_B = Microdado_Prova4[respostas].count()
            gabarito_prova4 = Microdado_Prova4[gabarito]

            acertos = [0] * 2
            acertos_porcentagem = [0] * 1

            if quantidade_de_respostas >= 0:
                linha_do_gabarito = gabarito_prova4.iloc[quantidade_de_respostas]

            j = 0
            questao4 = int(questao4)-1

            for i in range(quantidade_de_respostas):
                if resposta[i] == '':
                    resposta[i] = "............................................."
                linha_da_resposta = resposta[i]

                resposta_gabarito = linha_do_gabarito[questao4]
                resposta_candidato = linha_da_resposta[questao4]

                if acerto_erro == 'acertos':
                    if resposta_candidato == resposta_gabarito:
                        acertos[j] += 1
                        resposta_candidato = ''
                else:
                    if resposta_candidato != resposta_gabarito:
                        acertos[j] += 1
                        resposta_candidato = ''

            acertos_porcentagem[0] = (acertos[j] / quantidade_de_respostas) * 100

            acertos_pd_prova4 = pd.DataFrame(acertos_porcentagem)
            acertos_pd_prova4 = acertos_pd_prova4.reset_index(drop=True)
            acertos_pd_prova4.index = acertos_pd_prova4.index + int(questao4)
            
        # FINAL PROVA 4
        
        # Colocando nome no DataFrame
        acertos_pd_prova1.columns = ['porcentagem_de_acertos']
        texto = acertos_pd_prova1.porcentagem_de_acertos

        # Colocando nome no DataFrame
        acertos_pd_prova2.columns = ['porcentagem_de_acertos']
        texto = acertos_pd_prova2.porcentagem_de_acertos        
        
        # Colocando nome no DataFrame PROVA 3        
        if(filtro_cor_da_prova3!='Nenhuma'):  
            acertos_pd_prova3.columns = ['porcentagem_de_acertos']
            texto = acertos_pd_prova3.porcentagem_de_acertos

        # Colocando nome no DataFrame PROVA 4       
        if(filtro_cor_da_prova4!='Nenhuma'):  
            acertos_pd_prova4.columns = ['porcentagem_de_acertos']
            texto = acertos_pd_prova4.porcentagem_de_acertos

        print("----------------------------------------------------------------------------------")
        print(acertos_pd_prova1)
        print(acertos_pd_prova2)
        print(acertos_pd_prova3)
        print(acertos_pd_prova4)
        print("----------------------------------------------------------------------------------")

        relatorio_em_grafico = go.Figure()

        relatorio_em_grafico.add_bar(
            y=acertos_pd_prova1['porcentagem_de_acertos'],
            x=(acertos_pd_prova1.index+1),
            text=acertos_pd_prova1['porcentagem_de_acertos'],
            texttemplate='%{text:.2f}%',
            textposition='auto',
            name=filtro_cor_da_prova1
        )

        relatorio_em_grafico.add_bar(
            y=acertos_pd_prova2['porcentagem_de_acertos'],
            x=(acertos_pd_prova2.index+1),
            text=acertos_pd_prova2['porcentagem_de_acertos'],
            texttemplate='%{text:.2f}%',
            textposition='auto',
            name=filtro_cor_da_prova2
        )
        
        # Colocando nome no DataFrame PROVA 4       
        if(filtro_cor_da_prova3!='Nenhuma'):  
            relatorio_em_grafico.add_bar(
                y=acertos_pd_prova3['porcentagem_de_acertos'],
                x=(acertos_pd_prova3.index+1),
                text=acertos_pd_prova3['porcentagem_de_acertos'],
                texttemplate='%{text:.2f}%',
                textposition='auto',
                name=filtro_cor_da_prova3
            )

        # Colocando nome no DataFrame PROVA 4       
        if(filtro_cor_da_prova4!='Nenhuma'):  
            relatorio_em_grafico.add_bar(
                y=acertos_pd_prova4['porcentagem_de_acertos'],
                x=(acertos_pd_prova4.index+1),
                text=acertos_pd_prova4['porcentagem_de_acertos'],
                texttemplate='%{text:.2f}%',
                textposition='auto',
                name=filtro_cor_da_prova4
            )
            
        if(filtro_cor_da_prova3=='Nenhuma' and filtro_cor_da_prova4=='Nenhuma'):
            indexes = [int(questao1)+1, int(questao2)+1 ]
        elif(filtro_cor_da_prova3!='Nenhuma' and filtro_cor_da_prova4=='Nenhuma'):
            indexes = [int(questao1)+1, int(questao2)+1, int(questao3)+1]
        elif(filtro_cor_da_prova3=='Nenhuma' and filtro_cor_da_prova4!='Nenhuma'):
            indexes = [int(questao1)+1, int(questao2)+1, int(questao4)+1]
        elif(filtro_cor_da_prova3!='Nenhuma' and filtro_cor_da_prova4!='Nenhuma'):
            indexes = [int(questao1)+1, int(questao2)+1, int(questao3)+1, int(questao4)+1]
        
        print(filtro_cor_da_prova1)
        print(filtro_cor_da_prova2)
        print(filtro_cor_da_prova3)
        print(filtro_cor_da_prova4)
        
        print(indexes)
            
        relatorio_em_grafico.update_layout(
            xaxis=dict(
                tickvals=indexes,
                tickmode="array",
                titlefont=dict(size=10),
            ),
            title="Percentual de " + acerto_erro + " nas questões na prova de " + prova + " no ano de " + filtro_ano,
            height=500,
            margin={'t': 50, 'l': 50},
            yaxis={'domain': [0, 1]},
            xaxis2={'anchor': 'y2'},
            xaxis_title=("Número da da questão na prova: " + prova),
            yaxis_title="Desempenho em percentual de acertos.",
            yaxis2={'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'},
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )

        relatorio = relatorio_em_grafico.to_html()


        
        menssagem1 = 'PDF da prova de '+prova
        anotacao_mensagem = 'Q1, Q2, Q3, Q4, ..., Corresponde ao numero da questão na prova '+ prova
        anotacao = """Através deste gráfico, é possível visualizar a proporção em 
        porcentagem de quantos alunos acertaram ou erraram a questão especificada pelo 
        "Q". Dessa forma, é possível identificar em qual questão da prova deve-se 
        fazer uma análise para entender o motivo de a questão ter uma maior porcentagem 
        de alunos que erraram."""
        
        # Cria a mensagem de anotação
        informativo = '<h5 class="mb-0">Informativo:</h5>'

        # Formata a mensagem em HTML
        anotacao_mensagem = f'<div class="col-md-11 border"><div class="col-md-11 mt-2">{informativo}</div><hr class="mt-0">{anotacao}<hr class="mt-0">{anotacao_mensagem}</div>'
        
        context = {
            'form' : form,
            'menssagem':menssagem,
            'relatorio'  :relatorio,
            'anotacao_mensagem' : anotacao_mensagem,
            'menssagem1' : menssagem1,
            'prova_pdf'  :  prova_pdf,
            'form_filtro_grupo_A' : form_filtro_grupo_A,
            'form_filtro_grupo_B' : form_filtro_grupo_B,
            'quantidadeParcial_grupo_A' : quantidadeParcial_grupo_A,
            'quantidadeParcial_grupo_B' : quantidadeParcial_grupo_B,
            'quantidadeTotal' : CONTAGEMMicrodado_Amostra,
        }

    return render(request, 'base/formulario_3/relatorio_formulario_3_2.html', context=context)


@login_required
def formulario_3(request):

    if request.method == 'GET':
        menssagem = 'Análise do Desempenho Acadêmico: Quantidade de Acertos e Erros por Prova e Aplicação de Filtros'
        menssagem_informativa = """A análise de dados é uma das habilidades mais importantes na era digital em que vivemos, e é especialmente útil quando se trata de quantificar o desempenho em testes como o Exame Nacional do Ensino Médio (ENEM). Uma plataforma online com filtros pode ser uma ferramenta poderosa para analisar dados do ENEM e determinar o nível de sucesso de um determinado grupo de estudantes.

        Usando uma plataforma online com filtros, é possível analisar vários dados do ENEM, como a nota geral, a pontuação em cada área de conhecimento e a nota de redação. Além disso, é possível filtrar esses dados por região, tipo de escola, renda familiar, entre outros fatores.

        Com essa plataforma, é possível determinar o nível de sucesso de um determinado grupo de estudantes, comparando-os com o desempenho geral de outros grupos. Por exemplo, é possível analisar os dados dos estudantes de uma determinada escola de ensino médio em relação aos dados gerais de todas as escolas de ensino médio na região.

        Essa análise de dados pode ajudar a identificar possíveis áreas de melhoria no processo de ensino e aprendizagem, permitindo que os educadores tomem decisões informadas sobre a forma como ensinam e avaliam os alunos. Também pode ajudar a identificar os estudantes que precisam de mais apoio e fornecer informações valiosas para os pais sobre o desempenho dos seus filhos.


        Em resumo, a análise de dados usando uma plataforma online com filtros pode fornecer informações valiosas sobre o desempenho dos alunos no ENEM, ajudando a identificar áreas de melhoria e fornecer informações importantes para os educadores e pais."""
        
        menssagem_informativa = menssagem_informativa.split('\n')
        menssagem_informativa = format_html_join('\n', '<p>{}</p>', ((line,) for line in menssagem_informativa))
        

        form = Formulario_3()
        form_filtro = Formulario_filtros()

        context = {
            'form' : form,
            'menssagem' : menssagem,
            'menssagem_informativa' : menssagem_informativa,
            'form_filtro' : form_filtro
        }
        return render(request, 'base/formulario_3/quest_formulario_3.html', context=context)
    else:


        # Recebendo fomulario da tela
        form = Formulario_3(request.POST)
        form_filtro = Formulario_filtros(request.POST)

        filtro_deficiencia = form.data['deficiencia']
        acerto_erro = form.data['acerto_erro']

        # Formulario de Filtro
        filtro_deficiencia = form_filtro.data['deficiencia']
        filtro_estado_civil = form_filtro.data['estado_civil']
        filtro_cor = form_filtro.data['cor']
        filtro_sexo = form_filtro.data['sexo']
        filtro_ano = form_filtro.data['ano']
        filtro_escola = form_filtro.data['escola']
        filtro_nacionalidade = form_filtro.data['nacionalidade']
        filtro_estado = form_filtro.data['estado']
        filtro_cidade = form_filtro.data['cidade']
        filtro_amostra = form_filtro.data['amostra']
        filtro_recurso = form_filtro.data['recurso']
        filtro_localizacao_da_escola = form_filtro.data['localizacao_da_escola']
        filtro_ltp_adm_escola = form_filtro.data['tp_adm_escola']
        filtro_ano_de_conclusao = form_filtro.data['ano_de_conclusao']
        
        # Variáveis vindas do Formulario
        if (filtro_ano=="2019"):
            filtro_cor_da_prova = request.POST.get('cor_da_prova_2019')
            print(filtro_cor_da_prova)
        elif (filtro_ano=="2018"):
            filtro_cor_da_prova = request.POST.get('cor_da_prova_2018')
            print(filtro_cor_da_prova)
        elif (filtro_ano=="2017"):
            filtro_cor_da_prova = request.POST.get('cor_da_prova_2017')
            print(filtro_cor_da_prova)

        # em desenvolvimento
        

        prova_pdf = prova_nome_pdf(filtro_cor_da_prova=filtro_cor_da_prova)
        prova_pdf = '/pdf/PROVAS_E_GABARITOS/'+prova_pdf

        if (filtro_ano=="2019"):
            if( filtro_cor_da_prova == '503' or 
                filtro_cor_da_prova == '504' or
                filtro_cor_da_prova == '505' or
                filtro_cor_da_prova == '506' or
                filtro_cor_da_prova == '519' or
                filtro_cor_da_prova == '523' or
                filtro_cor_da_prova == '543' or
                filtro_cor_da_prova == '544' or
                filtro_cor_da_prova == '545' or
                filtro_cor_da_prova == '546'):
                prova = 'CO_PROVA_CN'
            elif(
                filtro_cor_da_prova == '507' or 
                filtro_cor_da_prova == '508' or
                filtro_cor_da_prova == '509' or
                filtro_cor_da_prova == '510' or
                filtro_cor_da_prova == '520' or
                filtro_cor_da_prova == '524' or
                filtro_cor_da_prova == '547' or
                filtro_cor_da_prova == '548' or
                filtro_cor_da_prova == '549' or
                filtro_cor_da_prova == '550' or
                filtro_cor_da_prova == '564'):
                prova = 'CO_PROVA_CH'
            elif(
                filtro_cor_da_prova == '511' or 
                filtro_cor_da_prova == '512' or
                filtro_cor_da_prova == '513' or
                filtro_cor_da_prova == '514' or
                filtro_cor_da_prova == '521' or
                filtro_cor_da_prova == '525' or
                filtro_cor_da_prova == '551' or
                filtro_cor_da_prova == '552' or
                filtro_cor_da_prova == '553' or
                filtro_cor_da_prova == '554' or
                filtro_cor_da_prova == '565'):
                prova = 'CO_PROVA_LC'
            elif(
                filtro_cor_da_prova == '515' or
                filtro_cor_da_prova == '516' or
                filtro_cor_da_prova == '517' or
                filtro_cor_da_prova == '518' or
                filtro_cor_da_prova == '522' or
                filtro_cor_da_prova == '526' or
                filtro_cor_da_prova == '555' or
                filtro_cor_da_prova == '556' or
                filtro_cor_da_prova == '557' or
                filtro_cor_da_prova == '558'):
                prova = 'CO_PROVA_MT'
            else:
                prova = 'CO_PROVA_MT'
        elif (filtro_ano=="2018"):
            if( filtro_cor_da_prova == '447' or 
                filtro_cor_da_prova == '448' or
                filtro_cor_da_prova == '449' or
                filtro_cor_da_prova == '450' or
                filtro_cor_da_prova == '463' or
                filtro_cor_da_prova == '467' or
                filtro_cor_da_prova == '487' or
                filtro_cor_da_prova == '488' or
                filtro_cor_da_prova == '489' or
                filtro_cor_da_prova == '490'):
                prova = 'CO_PROVA_CN'
            elif(
                filtro_cor_da_prova == '451' or 
                filtro_cor_da_prova == '452' or
                filtro_cor_da_prova == '453' or
                filtro_cor_da_prova == '454' or
                filtro_cor_da_prova == '464' or
                filtro_cor_da_prova == '468' or
                filtro_cor_da_prova == '491' or
                filtro_cor_da_prova == '492' or
                filtro_cor_da_prova == '493' or
                filtro_cor_da_prova == '494'):
                prova = 'CO_PROVA_CH'
            elif(
                filtro_cor_da_prova == '455' or 
                filtro_cor_da_prova == '456' or
                filtro_cor_da_prova == '457' or
                filtro_cor_da_prova == '458' or
                filtro_cor_da_prova == '465' or
                filtro_cor_da_prova == '469' or
                filtro_cor_da_prova == '495' or
                filtro_cor_da_prova == '496' or
                filtro_cor_da_prova == '497' or
                filtro_cor_da_prova == '498' ):
                prova = 'CO_PROVA_LC'
            elif(
                filtro_cor_da_prova == '459' or
                filtro_cor_da_prova == '460' or
                filtro_cor_da_prova == '461' or
                filtro_cor_da_prova == '462' or
                filtro_cor_da_prova == '466' or
                filtro_cor_da_prova == '470' or
                filtro_cor_da_prova == '499' or
                filtro_cor_da_prova == '500' or
                filtro_cor_da_prova == '501' or
                filtro_cor_da_prova == '502'):
                prova = 'CO_PROVA_MT'
            else:
                prova = 'CO_PROVA_MT'
        elif (filtro_ano=="2017"):
            if( filtro_cor_da_prova == '391' or 
                filtro_cor_da_prova == '392' or
                filtro_cor_da_prova == '393' or
                filtro_cor_da_prova == '394' or
                filtro_cor_da_prova == '407' or
                filtro_cor_da_prova == '411' or
                filtro_cor_da_prova == '431' or
                filtro_cor_da_prova == '432' or
                filtro_cor_da_prova == '433' or
                filtro_cor_da_prova == '434'):
                prova = 'CO_PROVA_CN'
            elif(
                filtro_cor_da_prova == '395' or 
                filtro_cor_da_prova == '396' or
                filtro_cor_da_prova == '397' or
                filtro_cor_da_prova == '398' or
                filtro_cor_da_prova == '408' or
                filtro_cor_da_prova == '412' or
                filtro_cor_da_prova == '435' or
                filtro_cor_da_prova == '436' or
                filtro_cor_da_prova == '437' or
                filtro_cor_da_prova == '438'):
                prova = 'CO_PROVA_CH'
            elif(
                filtro_cor_da_prova == '399' or 
                filtro_cor_da_prova == '400' or
                filtro_cor_da_prova == '401' or
                filtro_cor_da_prova == '402' or
                filtro_cor_da_prova == '409' or
                filtro_cor_da_prova == '413' or
                filtro_cor_da_prova == '439' or
                filtro_cor_da_prova == '440' or
                filtro_cor_da_prova == '441' or
                filtro_cor_da_prova == '442'):
                prova = 'CO_PROVA_LC'
            elif(
                filtro_cor_da_prova == '403' or
                filtro_cor_da_prova == '404' or
                filtro_cor_da_prova == '405' or
                filtro_cor_da_prova == '406' or
                filtro_cor_da_prova == '410' or
                filtro_cor_da_prova == '414' or
                filtro_cor_da_prova == '443' or
                filtro_cor_da_prova == '444' or
                filtro_cor_da_prova == '445' or
                filtro_cor_da_prova == '446'):
                prova = 'CO_PROVA_MT'
            else:
                prova = 'CO_PROVA_MT'
        
        print(prova_pdf)
        # Formulario de Filtro
        if prova == 'CO_PROVA_LC':
            respostas = "TX_RESPOSTAS_LC"
            gabarito = "TX_GABARITO_LC"
        elif prova == 'CO_PROVA_CN':
            respostas = "TX_RESPOSTAS_CN"
            gabarito = "TX_GABARITO_CN"
        elif prova == 'CO_PROVA_MT':
            respostas = "TX_RESPOSTAS_MT"
            gabarito = "TX_GABARITO_MT"
        elif prova == 'CO_PROVA_CH':
            respostas = "TX_RESPOSTAS_CH"
            gabarito = "TX_GABARITO_CH"

        if(filtro_sexo != 'todos'):
            Amostra = [prova, 'TP_SEXO', respostas, gabarito]
            Microdado_Amostra = bd_formulario_3.buscar_dataframe_no_banco(
                Amostra, 
                filtro_sexo=filtro_sexo, 
            filtro_cidade=filtro_cidade, 
                filtro_cor_da_prova=filtro_cor_da_prova, 
                filtro_deficiencia=filtro_deficiencia,
                filtro_amostra=filtro_amostra, 
                filtro_cor=filtro_cor, 
                filtro_ltp_adm_escola=filtro_ltp_adm_escola,            
                filtro_ano_de_conclusao=filtro_ano_de_conclusao,     
                filtro_estado=filtro_estado, 
                filtro_recurso=filtro_recurso,
                filtro_localizacao_da_escola=filtro_localizacao_da_escola, 
                filtro_estado_civil=filtro_estado_civil, 
                filtro_escola=filtro_escola, 
                filtro_nacionalidade=filtro_nacionalidade,
                filtro_ano=filtro_ano)
        else:
            Amostra = [prova, respostas, gabarito]
            Microdado_Amostra = bd_formulario_3.buscar_dataframe_no_banco(
                Amostra, 
                filtro_sexo=filtro_sexo, 
            filtro_cidade=filtro_cidade, 
                filtro_cor_da_prova=filtro_cor_da_prova, 
                filtro_deficiencia=filtro_deficiencia,
                filtro_amostra=filtro_amostra, 
                filtro_ltp_adm_escola=filtro_ltp_adm_escola,            
                filtro_ano_de_conclusao=filtro_ano_de_conclusao,     
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
        
        menssagem = 'Análise do Desempenho Acadêmico: Quantidade de Acertos e Erros por Prova e Aplicação de Filtros'

        Microdado_Amostra.reset_index(inplace=True)
        resposta = Microdado_Amostra[respostas]
        quantidade_de_respostas = (Microdado_Amostra[respostas].count()-1)
        gabarito = Microdado_Amostra[gabarito]

        acertos = [0]*46
        acertos_porcentagem = [0]*46
        if(quantidade_de_respostas >= 0):
            linha_do_gabarito = gabarito[quantidade_de_respostas]

        for j in range(0, 45):
            for i in range(0, quantidade_de_respostas):
                # print(i)
                # print(quantidade_de_respostas)
                # print('resposta[i]:'+resposta[i])
                # print("linha_da_resposta[j] :" +linha_da_resposta[j] )
                if(resposta[i] == ''):
                    resposta[i] = "............................................."
                linha_da_resposta = resposta[i]

                resposta_gabarito = linha_do_gabarito[j]
                resposta_candidato = linha_da_resposta[j]
                
                if acerto_erro == 'acertos':
                    if resposta_candidato == resposta_gabarito:
                        acertos[j] = acertos[j] + 1
                        resposta_candidato = ''
                else:
                    if resposta_candidato != resposta_gabarito:
                        acertos[j] = acertos[j] + 1
                        resposta_candidato = ''

            acertos_porcentagem[j+1] = (acertos[j] / quantidade_de_respostas)*100
        
        # print(acertos_porcentagem)
        print(acertos_porcentagem)
        acertos_porcentagem = acertos_porcentagem[1:]
        print(acertos_porcentagem)
        acertos_pd = pd.DataFrame(acertos_porcentagem)
        
        # Colocando nome no DataFrame
        acertos_pd.columns = ['porcentagem_de_acertos']
        texto = acertos_pd.porcentagem_de_acertos
        print(acertos_pd)
        
        relatorio_em_grafico = go.Figure()
        nome = "Percentual Conforme os critérios estabelecidos"
        relatorio_em_grafico.add_bar(
            y=(acertos_pd['porcentagem_de_acertos']),
            x=(acertos_pd.index).map(lambda x: f"Q{x+1}"),
            text=(acertos_pd['porcentagem_de_acertos']),
            texttemplate='%{text:.2f}%',
            textposition='auto',
            name=nome
        )
        relatorio_em_grafico.update_layout(
            xaxis=dict(
                tickvals =acertos_pd.index,
                tickmode="array",
                titlefont=dict(size=10),
            ),
            title="Percentual de " + acerto_erro + " nas questões na prova de " + prova + " no ano de " + filtro_ano + " dos inscritos que possuem " + filtro_deficiencia + " deficiência.",
            height = 500,
            margin = {'t':50, 'l':50},
            yaxis = {'domain': [0, 1]},
            xaxis2 = {'anchor': 'y2'},
            xaxis_title=("Número da da questão na prova: "+prova),
            yaxis_title="Desempenho em percentual de acertos.",
            yaxis2 = {'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'},
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )
        relatorio = relatorio_em_grafico.to_html()
        
        menssagem1 = 'PDF da prova de '+prova
        anotacao_mensagem = 'Q1, Q2, Q3, Q4, ..., Corresponde ao numero da questão na prova '+ prova
        anotacao = """Através deste gráfico, é possível visualizar a proporção em 
        porcentagem de quantos alunos acertaram ou erraram a questão especificada pelo 
        "Q". Dessa forma, é possível identificar em qual questão da prova deve-se 
        fazer uma análise para entender o motivo de a questão ter uma maior porcentagem 
        de alunos que erraram."""
        
        # Cria a mensagem de anotação
        informativo = '<h5 class="mb-0">Informativo:</h5>'

        # Formata a mensagem em HTML
        anotacao_mensagem = f'<div class="col-md-11 border"><div class="col-md-11 mt-2">{informativo}</div><hr class="mt-0">{anotacao}<hr class="mt-0">{anotacao_mensagem}</div>'
        
        context = {
            'form' : form,
            'menssagem':menssagem,
            'relatorio'  :relatorio,
            'anotacao_mensagem' : anotacao_mensagem,
            'menssagem1' : menssagem1,
            'prova_pdf'  :  prova_pdf,
            'form_filtro' : form_filtro,
            'quantidadeParcial' : CONTAGEM,
            'quantidadeTotal' : CONTAGEMMicrodado_Amostra,
        }

    return render(request, 'base/formulario_3/relatorio_formulario_3.html', context=context)

