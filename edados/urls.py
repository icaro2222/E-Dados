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
from django.conf.urls.static import static
from django.conf import settings
from .view.dashboard import dashboard
from .view.aba_de_informacoes import view_aba_de_informacoes
from .view.fomulario_1 import view_formulario_1, view_formulario_1_4
from .view.fomulario_2 import view_formulario_2
from .view.fomulario_3 import view_formulario_3
from .view.fomulario_4 import view_formulario_4
from .view.tasks import criar_csv, verificar_csv

urlpatterns = [
    path('', dashboard.dashboard, name="dashboard"),
    path('admin/', admin.site.urls),

    # URLs do usuario da plataforma
    path('', include('usuarios.urls')),

    # Formulários
    path('Desempenho_no_exame/', view_formulario_2.formulario_2, name="Quest_Soc_Notas_Deficiencia"),
    path('Dados_brutos_Infor/', view_formulario_1_4.formulario_4, name="formulario_1_4"),
    path('Perfil_do_Inscrito/', view_formulario_1.formulario_1, name="formulario_1"),
    
    path('Acertos_por_Prova/', view_formulario_3.formulario_3, name="formulario_3"),
    
    path('Mapa_de_Distribuição_de_alunos/', view_formulario_4.formulario_4, name="formulario_4"),
    
    path('criar_csv/',criar_csv , name="criar_csv"),
    path('verificar_csv/',verificar_csv , name="verificar_status_csv"),
    
    path('Infor/', view_aba_de_informacoes.aba_de_informacoes, name="aba_de_informacoes"),
    path('listar_usuarios/', view_aba_de_informacoes.listar_usuarios, name="listar_usuarios"),
    path('excluir/', view_aba_de_informacoes.listar_usuarios, name="excluir"),
    path('log_de_acesso/', view_aba_de_informacoes.log_de_acesso, name="log_de_acesso"),
    path('Cadastrar_Usuário/', view_aba_de_informacoes.cadastrar_usuarios, name="cadastrar_usuario"),
    path('Editar_Usuário/', view_aba_de_informacoes.editar_usuario, name="editar_usuario"),
    path('Dicionário_Microdados/', view_aba_de_informacoes.dicionario_microdados, name="dicionario"),
    
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if (settings.DEBUG):
#     import debug_toolbar
#     urlpatterns += [path('__debug__/', include(debug_toolbar.urls)),]