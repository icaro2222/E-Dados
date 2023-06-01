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

        # Recebendo fomulario da tela
        form = Formulario_4(request.POST)
        form_filtro = Formulario_filtros(request.POST)
        
        global CONTAGEM
        global CONTAGEMMicrodado_Amostra
        # Formulario de Filtro
        menssagem = ("Mapa de Distribuição de Alunos")
        menssagem_informativa = """A tela web em questão disponibiliza uma ferramenta de análise da densidade demográfica 
        dos inscritos no ENEM utilizando os microdados."""

        # df = pd.read_csv(BASE_DIR/'fomulario_4/municipios_brasileiros.csv')
        # trace = go.Scattergeo(
        #     locationmode='ISO-3',
        #     lon=df['longitude'],
        #     lat=df['latitude'],
        #     text=df['nome_municipio'] + '- População: ' + df['codigo_ibge'].astype(str),
        #     marker=dict(
        #         size=df['codigo_ibge'] / 300000,
        #         color='#2980b9',
        #         line={'width': 1, 'color': '#2c3e50'},
        #         sizemode='area'
        #     )
        # )
        # data = [trace]
        # layout = go.Layout(
        #     height=700,
        #     autosize=True,
        #     margin=dict(l=0, r=0, b=10, t=0),
        #     title='<b>Inscritos do Enem de 2019</b>',
        #     titlefont={'family': 'Arial', 'size': 24},
        #     geo=dict(
        #         scope='south america',
        #         projection={'type': 'mercator'},
        #         showland=True,
        #         landcolor='#ecf0f1',
        #         showlakes=True,
        #         lakecolor='#eaeef0',
        #         subunitwidth=1,
        #         subunitcolor="rgb(255, 255, 255)"
        #     )
        # )

        # fig = go.Figure(data=data, layout=layout)


        # relatorio = fig.to_html()
        # relatorio = ''

# -------------------------------------------------------------------------------------------------------

        from edados.database import bd_formulario_4

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
        
        if(filtro_ano=="2019"):
            CONTAGEMMicrodado_Amostra = 3702008
        elif(filtro_ano=="2018"):
            # CONTAGEMMicrodado_Amostra = 3893743
            CONTAGEMMicrodado_Amostra = 3893671
        elif(filtro_ano=="2017"):
            CONTAGEMMicrodado_Amostra = 4426755
            
        CONTAGEM  = Microdado_Amostra['SG_UF_RESIDENCIA'].count()
            
        print(Microdado_Amostra)
        # Formulario de Filtro
        menssagem = ("Mapa de Distribuição de Alunos")
        menssagem_informativa = """A tela web em questão disponibiliza uma ferramenta de análise da densidade demográfica 
        dos inscritos no ENEM utilizando os microdados."""
        
        import json

        # with open(BASE_DIR/'fomulario_4/geojs-100-mun.json') as json_file:
        #     geojson = json.load(json_file)
            
        
        # # Criar o Choroplethmapbox
        # relatorio_mapa = go.Figure(data=go.Choroplethmapbox(
        #     geojson=geojson,
        #     locations=df['codigo_ibge'],
        #     z=df['codigo_ibge']/30000,  # Utilizando o código IBGE como valor para o mapa de calor
        #     text=df['nome_municipio'] + '- População: ' + df['codigo_ibge'].astype(str),
        #     colorscale='Viridis',  # Escolha da escala de cores
        #     reversescale=True,  # Inverter a escala de cores
        #     colorbar_title='Código IBGE'  # Título da barra de cores
        # ))

        # # Configurar o layout
        # relatorio_mapa.update_layout(
        #     mapbox_style="carto-positron",  # Estilo do mapa
        #     mapbox_zoom=3,  # Nível de zoom inicial
        #     mapbox_center={"lat": -14.235, "lon": -51.925},  # Coordenadas de latitude e longitude iniciais
        #     margin=dict(l=0, r=0, b=10, t=50),
        #     title=('<b>'+filtro_questao+'</b>'),
        #     titlefont={'family': 'Arial', 'size': 24},
        # )


        # relatorio_mapa.update_geos(
        #     visible=True,  # Ocultar mapa mundial completo
        #     resolution=50,  # Resolução do mapa
        #     showcountries=True,  # Ocultar bordas dos países
        #     lataxis_range=[-35, 6],  # Latitude mínima e máxima para exibir o Brasil
        #     lonaxis_range=[-75, -33]  # Longitude mínima e máxima para exibir o Brasil
        # )

        # relatorio_mapa.update_layout(
        #     mapbox_style="carto-positron",  # Estilo do mapa
        #     mapbox_zoom=3,  # Nível de zoom inicial
        #     mapbox_center={"lat": -14.235, "lon": -51.925},  # Coordenadas de latitude e longitude iniciais
        #     margin=dict(l=0, r=0, b=10, t=50),
        #     title='<b>Inscritos do Enem de 2019</b>',
        #     titlefont={'family': 'Arial', 'size': 24},
        # )
        
        if filtro_questao=='nenhum':
            filtro_questao="SG_UF_RESIDENCIA"
        import plotly.express as px
        brazil_states = json.load(open(BASE_DIR/"fomulario_4/brazil_geo.json", "r"))
        # df_states = pd.read_csv("/var/www/edados/edados/view/fomulario_4/Dashboard COVID-19/df_states.csv")
        df_states = Microdado_Amostra
        fig = px.choropleth_mapbox(
            df_states,             
            height=700,
            locations="SG_UF_RESIDENCIA",
            geojson=brazil_states, 
            center={"lat": -16.95, "lon": -47.78},
            zoom=3, color=filtro_questao, 
            color_continuous_scale="blues", 
            opacity=0.4)
        fig.update_layout(
            mapbox_style="carto-positron",  # Estilo do mapa
            mapbox_zoom=3,  # Nível de zoom inicial
            mapbox_center={"lat": -14.235, "lon": -51.925},  # Coordenadas de latitude e longitude iniciais
            margin=dict(l=0, r=0, b=10, t=50),
            title=('<b>'+filtro_questao+'</b>'),
            titlefont={'family': 'Arial', 'size': 24},
        )

        relatorio_mapa = fig.to_html()
        relatorio = ''
        # import plotly as plt
        # import plotly.express as px
        # import json
        # from urllib.request import urlopen
        
        # with urlopen('https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson') as response:
        #     Brazil = json.load(response) # Javascrip object notation 
        # Brazil
        # state_id_map = {}
        # for feature in Brazil ['features']:
        #     feature['id'] = feature['properties']['name']
        #     state_id_map[feature['properties']['sigla']] = feature['id']
        # soybean = pd.read_csv('https://raw.githubusercontent.com/nayanemaia/Dataset_Soja/main/soja%20sidra.csv')
        # print(soybean)
        # relatorio_mapa = px.choropleth(
        # soybean, #soybean database
        # locations = geojson, #define the limits on the map/geography
        # geojson = Brazil, #shape information
        # color = "Produção", #defining the color of the scale through the database
        # hover_name = geojson, #the information in the box
        # hover_data =["Produção","Longitude","Latitude"],
        # title = "Produtivida da soja (Toneladas)", #title of the map
        # animation_frame = geojson#creating the application based on the year
        # )
        # relatorio_mapa.update_geos(fitbounds = "locations", visible = False)
        # relatorio_mapa=relatorio_mapa.to_html()

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
    