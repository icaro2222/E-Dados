"""EDados URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .view.outros import view_quest_demo_notas
# from .view import view_quest_socio_notas, view_quest_demo_socioe, view_quest_socio_notas_sexo , view_quest_socio_notas_deficiencia, view_regiao, view_regiao_mapa#, views, view,  view_plot
from .view.contraste import view_contrast_quest_socio_notas
from .view.dashboard import dashboard
from .view.aba_de_informacoes import view_aba_de_informacoes
from .view.fomulario_1 import view_formulario_1, view_formulario_1_4
from .view.fomulario_2 import view_formulario_2
from .view.fomulario_3 import view_formulario_3
from .view.fomulario_4 import view_formulario_4

urlpatterns = [
    path('', dashboard.Dashboard, name="dashboard"),
    path('admin/', admin.site.urls),

    # URLs do usuario da plataforma
    path('', include('usuarios.urls')),

    # Formulários
    path('Quest Soc Notas Deficiencia/', view_formulario_2.formulario_2, name="Quest_Soc_Notas_Deficiencia"),
    path('Perfil_4_do_Inscrito/', view_formulario_1_4.formulario_4, name="formulario_1_4"),
    path('Perfil_do_Inscrito/', view_formulario_1.formulario_1, name="formulario_1"),
    
    path('Acerto_por_Prova/', view_formulario_3.formulario_3, name="formulario_3"),
    
    path('regiao_demografica/', view_formulario_4.formulario_4, name="formulario_4"),
    
    path('Infor/', view_aba_de_informacoes.aba_de_informacoes, name="aba_de_informacoes"),
    path('Criadores/', view_aba_de_informacoes.criadores, name="criadores"),
    path('Correcoes/', view_aba_de_informacoes.correcoes_bugs, name="correcoes"),
    path('Dicionário Microdados/', view_aba_de_informacoes.dicionario_microdados, name="dicionario"),
    
    # path('teste/', views.teste, name='teste'),
    # path('manipulando/', views.index, name='page_dados'),
    # path('grafico_tabela/', view.Grafico_Tabela, name="grafico_tabela"),
    # path('grafico_plot_teste/', view_plot.Grafico_Plot_Teste, name="grafico_plot_teste"),
    # path('Quest Soc Notas/', view_quest_socio_notas.view_quest_socio_notas, name="Quest_Soc_Notas"),
    # path('Quest Demograf Notas/', view_quest_demo_notas.view_quest_demo_notas, name="Quest_Dem_Notas"),
    # path('Questão_Demográfica_vs_Socioeconômica/', view_quest_demo_socioe.view_quest_demo_socioe, name="Quest_Dem_Socioe"),
    # path('Desenpenho por Regiao/', view_regiao.regiao, name="Desenpenho_por_Regiao"),
    # path('Desenpenho por Regiao Mapa/', view_regiao_mapa.view_regiao_mapa, name="Desenpenho_por_Regiao_Mapa"),
    # path('Quest Soc Notas Sexo/', view_quest_socio_notas_sexo.Quest_Soc_Notas_Sexo, name="Quest_Soc_Notas_Sexo"),

    # URLs de Contraste entre Deficiêntes e Não deficiêntes
    # path('Contrast Quest Soc Notas/', view_contrast_quest_socio_notas.contrast_quest_socio_notas, name="Contrast_Quest_Soc_Notas_Deficiencia"),

]
