from django.shortcuts import render
import plotly.graph_objects as go
import pandas as pd
from edados.formularios.filtros.formulario_1_filtros import Formulario_filtros
from edados.formularios.filtros.filtros_ano import Formulario_filtro_ano
from edados.formularios.formulario_4.formulario_4 import Formulario_4
from django.utils.html import format_html_join
from pathlib import Path
from django.contrib.auth.decorators import login_required

CONTAGEM = 0
CONTAGEMMicrodado_Amostra = 0
BASE_DIR = Path(__file__).resolve().parent.parent

def formatar(valor):
    return "{:,.2f}".format(valor)


@login_required
def formulario_4(request):

    if request.method == 'GET':        
        
        menssagem = ("Mapa de Distribuição de Alunos")
        menssagem_informativa = """O formulário web em questão disponibiliza uma ferramenta de análise da densidade demográfica dos inscritos no ENEM utilizando os microdados. Através dessa plataforma, é possível realizar análises comparativas entre diferentes regiões demográficas e identificar padrões que possam estar relacionados aos dados socioeconômicos dos inscritos.

        Com o objetivo de oferecer uma experiência de usuário intuitiva e acessível, a tela do site apresenta de forma clara e organizada as diferentes opções de análise disponíveis. É possível selecionar diferentes regiões demográficas e        comparar a densidade de inscritos em cada uma delas, além de visualizar gráficos e tabelas com informações detalhadas         sobre os dados socioeconômicos dos inscritos em cada região.

        Além disso, o site oferece opções avançadas de filtragem e segmentação de dados, permitindo que o usuário realize         análises mais específicas e detalhadas de acordo com suas necessidades. Por exemplo, é possível filtrar os dados por         gênero, idade, escolaridade e outras variáveis socioeconômicas para identificar padrões mais específicos em cada         região demográfica.

        A análise da densidade demográfica dos inscritos no ENEM é uma ferramenta valiosa para a compreensão das dinâmicas         socioeconômicas do país. Com base nesses dados, é possível identificar desigualdades regionais e propor políticas     públicas mais efetivas para a melhoria do acesso à educação e para a promoção da igualdade social.         O site web em questão representa uma importante contribuição nesse sentido, oferecendo uma plataforma de análise de dados     demográficos acessível e de fácil utilização para pesquisadores, estudantes e outros interessados em compreender melhor a realidade socioeconômica do Brasil."""
        menssagem_informativa = menssagem_informativa.split('\n')
        menssagem_informativa = format_html_join('\n', '<p>{}</p>', ((line,) for line in menssagem_informativa))


        form = Formulario_4()
        form_filtro = Formulario_filtros()

        context = {
            'form' : form,
            'menssagem' : menssagem,
            'menssagem_informativa' : menssagem_informativa,
            'form_filtro' : form_filtro
        }
        return render(request, 'base/formulario_4/quest_formulario_4.html', context=context)
    else:

        from edados.database import bd_formulario_4
        import plotly.express as px
        import json
        
        # Recebendo fomulario da tela
        form = Formulario_4(request.POST)
        form_filtro = Formulario_filtros(request.POST)
        
        global CONTAGEM
        global CONTAGEMMicrodado_Amostra
        
        # Formulario de Filtro
        menssagem = ("Mapa de Distribuição de Alunos")
        menssagem_informativa = """A tela web em questão disponibiliza uma ferramenta de análise da densidade demográfica 
        dos inscritos no ENEM utilizando os microdados."""


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
        filtro_cidade = form_filtro.data['cidade']
        filtro_amostra = form_filtro.data['amostra']
        filtro_recurso = form_filtro.data['recurso']
        filtro_localizacao_da_escola = form_filtro.data['localizacao_da_escola']
        filtro_ltp_adm_escola = form_filtro.data['tp_adm_escola']
        filtro_ano_de_conclusao = form_filtro.data['ano_de_conclusao']
           
        if(filtro_ano=="2019"):
            CONTAGEMMicrodado_Amostra = 3702008
        elif(filtro_ano=="2018"):
            CONTAGEMMicrodado_Amostra = 3893671
        elif(filtro_ano=="2017"):
            CONTAGEMMicrodado_Amostra = 4426755
            
        Amostra = '"SG_UF_RESIDENCIA"' 
        Microdado_Amostra = bd_formulario_4.buscar_dataframe_no_banco(
            Amostra, 
            filtro_cidade=filtro_cidade, 
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
        
        if Microdado_Amostra.empty:            
            context = {
                'form' : form,
                'menssagem' : menssagem,
                'relatorio_mapa' : "",
                'form_filtro' : form_filtro,
                'quantidadeParcial' : CONTAGEM,
                'quantidadeTotal' : CONTAGEMMicrodado_Amostra,
                'menssagem_informativa' : menssagem_informativa,
                'relatorio' : ""
            }
            return render(request, 'base/formulario_4/relatorio_formulario_4.html', context=context)
    
        if filtro_questao == 'vazio':
            Dataframe = Microdado_Amostra.groupby('SG_UF_RESIDENCIA')

            # Realizar a contagem de elementos em cada grupo
            Dataframe = Dataframe.size().reset_index(name='count')

            # Dataframe = Dataframe.rename_axis('SG_UF_RESIDENCIA')
            # Dataframe = Dataframe.reset_index() 
            
        else:
            Dataframe = Microdado_Amostra.groupby('SG_UF_RESIDENCIA')[filtro_questao]   
            Dataframe = Dataframe.describe() 
            Dataframe = Dataframe.rename_axis('SG_UF_RESIDENCIA')
            Dataframe = Dataframe.reset_index() 

        print(Dataframe)
        # print(contagem['SG_UF_RESIDENCIA'])
        
        CONTAGEM  = Microdado_Amostra['SG_UF_RESIDENCIA'].count()
            
        # Formulario de Filtro
        menssagem = ("Mapa de Distribuição de Alunos")
        menssagem_informativa = """A tela web em questão disponibiliza uma ferramenta de análise da densidade demográfica 
        dos inscritos no ENEM utilizando os microdados."""
        
        
        if filtro_questao=='vazio':
            variavel_para_analise = 'count'
        else:
            variavel_para_analise = 'mean'
        brazil_states = json.load(open(BASE_DIR/"fomulario_4/brazil_geo.json", "r"))
                    
        fig = px.choropleth_mapbox(
            Dataframe,             
            height=700,
            locations="SG_UF_RESIDENCIA",
            geojson=brazil_states, 
            center={"lat": -16.95, "lon": -47.78},
            zoom=3, 
            color=variavel_para_analise, 
            color_continuous_scale="blues", 
            opacity=0.4,
            custom_data=[variavel_para_analise]  # Especifica a coluna de dados personalizados
        )
        
        if filtro_questao=='vazio':
            filtro_questao="SG_UF_RESIDENCIA"
            # Calcular o percentual
            percentuais = Dataframe['count'] / Dataframe['count'].sum()

            # Converter os percentuais em formato de porcentagem com duas casas decimais
            percentuais_formatados = (percentuais * 100).round(2)

            # Atualizar o hovertemplate com os percentuais formatados
            fig.update_traces(
                hovertemplate='<b>Estado</b>: %{location}<br><b>Contagem</b>: %{customdata[0]}<br><b>Percentual</b>: ' + percentuais_formatados.astype(str) + '%',
            )
        else:
            # Atualizar o hovertemplate com os percentuais formatados
            # fig.update_traces(
            #     hovertemplate='<b>Estado</b>: %{location}<br><b>'+filtro_questao+'</b>: %{customdata[0]}<br>',
            # )
            fig.update_traces(
                hovertemplate='<b>Estado</b>: %{location}<br><b>Média</b>: %{customdata[0]:.2f}',
            )

        fig.update_layout(
            mapbox_style="carto-positron",
            mapbox_zoom=3,
            mapbox_center={"lat": -14.235, "lon": -51.925},
            margin=dict(l=0, r=0, b=10, t=50),
            title=('<b>'+filtro_questao+'</b>'),            
            titlefont={'family': 'Arial', 'size': 24},
        )

        relatorio_mapa = fig.to_html()


        relatorio = ''
        
        context = {
            'form' : form,
            'menssagem' : menssagem,
            'relatorio_mapa' : relatorio_mapa,
            'form_filtro' : form_filtro,
            'quantidadeParcial' : CONTAGEM,
            'quantidadeTotal' : CONTAGEMMicrodado_Amostra,
            'menssagem_informativa' : menssagem_informativa,
            'relatorio' : relatorio
        }

    return render(request, 'base/formulario_4/relatorio_formulario_4.html', context=context)
    