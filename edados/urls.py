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
from .view import view_quest_demo_notas, view_quest_socio_notas, view_quest_socio_notas_sexo , view_quest_socio_notas_deficiencia, view_regiao, view_regiao_mapa#, views, view,  view_plot

urlpatterns = [
    path('', TemplateView.as_view(template_name="dashboard.html"), name="dashboard"),
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    # path('teste/', views.teste, name='teste'),
    # path('manipulando/', views.index, name='page_dados'),
    # path('grafico_tabela/', view.Grafico_Tabela, name="grafico_tabela"),
    # path('grafico_plot_teste/', view_plot.Grafico_Plot_Teste, name="grafico_plot_teste"),
    path('Quest Soc Notas/', view_quest_socio_notas.view_quest_socio_notas, name="Quest_Soc_Notas"),
    path('Quest Demograf Notas/', view_quest_demo_notas.view_quest_demo_notas, name="Quest_Dem_Notas"),
    path('Desenpenho por Regiao/', view_regiao.regiao, name="Desenpenho_por_Regiao"),
    path('Desenpenho por Regiao Mapa/', view_regiao_mapa.view_regiao_mapa, name="Desenpenho_por_Regiao_Mapa"),
    path('Quest Soc Notas Sexo/', view_quest_socio_notas_sexo.Quest_Soc_Notas_Sexo, name="Quest_Soc_Notas_Sexo"),
    path('Quest Soc Notas Deficiencia/', view_quest_socio_notas_deficiencia.Quest_Soc_Notas_Deficiencia, name="Quest_Soc_Notas_Deficiencia"),
]
