from django.contrib.auth.decorators import login_required
import plotly.graph_objects as go
from django.shortcuts import render
import pandas as pd
import plotly.express as px
from edados.formularios.dashboard.formulario_dashboard import DashboardFormulario
from edados.database import bd_quest_socio_notas_deficiencia, conect_db
from django.utils.html import format_html_join 
import logging
import datetime
import pytz

logger = logging.getLogger(__name__)
def formatar(valor):
    return "{:,.2f}".format(valor)

@login_required
def dashboard(request):
    username = request.user.username
    if(username!="eren"):
        import sys
        from pathlib import Path
        import pytz
        import datetime
        brasilia_tz = pytz.timezone('America/Sao_Paulo')
        hora_atual = datetime.datetime.now(brasilia_tz)
        hora_formatada = hora_atual.strftime('%H:%M:%S')
        dia_e_mes_formatado = hora_atual.strftime('%d/%m/%Y em uma %A')
        # Caminho para o diretório do projeto
        BASE_DIR = Path(__file__).resolve().parents[3]
        # Abrir o arquivo de log em modo de escrita
        caminho = str(BASE_DIR) + '/Registros_Acesso.log'
        log_file = open(caminho, 'a')
        # Redirecionar a saída padrão para o arquivo de log
        sys.stdout = log_file
        # Imprimir a mensagem de log formatada corretamente
        print('Acesso à página "Dashboard" por "%s" às %s na data (%s)' % (username, hora_formatada, dia_e_mes_formatado))
        # Fechar o arquivo de log
        log_file.close()
        # Restaurar a saída padrão para o terminal
        sys.stdout = sys.__stdout__

    if request.method == 'GET':
        menssagem1 = "Bem-vindo à E-DADOS!"
        
        svg = ('''<svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
        <path d="M8 15C4.13401 15 1 11.866 1 8C1 4.13401 4.13401 1 8 1C11.866 1 15 4.13401 15 8C15 11.866 11.866 15 8 15ZM8 16C12.4183 16 16 12.4183 16 8C16 3.58172 12.4183 0 8 0C3.58172 0 0 3.58172 0 8C0 12.4183 3.58172 16 8 16Z"/>
        <path d="M8.9307 6.58789L6.63969 6.875L6.55766 7.25586L7.00883 7.33789C7.3018 7.4082 7.36039 7.51367 7.29594 7.80664L6.55766 11.2754C6.3643 12.1719 6.66313 12.5938 7.36625 12.5938C7.91117 12.5938 8.54398 12.3418 8.83109 11.9961L8.91898 11.5801C8.71977 11.7559 8.4268 11.8262 8.23344 11.8262C7.95805 11.8262 7.85844 11.6328 7.92875 11.293L8.9307 6.58789Z"/>
        <path d="M9 4.5C9 5.05228 8.55229 5.5 8 5.5C7.44772 5.5 7 5.05228 7 4.5C7 3.94772 7.44772 3.5 8 3.5C8.55229 3.5 9 3.94772 9 4.5Z"/>
        </svg>''')

        from django.utils.safestring import mark_safe
        from django.template import Library
        register = Library()
        @register.filter(is_safe=True)
        def svg_to_html(value):
            return mark_safe(value)      
        
        menssagem = '''<p class="font-weight-normal">A E-Dados é um protótipo de painel especializado na análise dos microdados socioeconômicos do ENEM. Para melhor utilização, o menu lateral foi projetado de forma bastante intuitiva, apresentando para você os objetivos de cada tipo de consulta. Além disso, ao longo dos formulários, você encontrará informações indicadas pelo ícone '''+svg+''', que, ao posicionar o cursor sobre elas, exibirão detalhes, caso necessário.</p>
        <p class="font-weight-normal">Explore os dados, obtenha insights valiosos e extraia informações com eficiência.</p>
        <p class="font-weight-normal">Vamos começar!</p>'''
        menssagem = svg_to_html(menssagem)
        
        context = {
            'menssagem': menssagem,
            'menssagem1': menssagem1,
        }
        return render(request, 'dashboard/dashboard.html', context=context)
    else:

        # Recebendo fomulario da tela
        form = DashboardFormulario(request.POST)

        # Variáveis vindas do Formulario
        ano = form.data['ano']

        # if(ano != 'todos'):
        #     Microdado_Amostra = bd_quest_socio_notas_deficiencia.buscar_dataframe_no_banco(ano)
        # else:
        #     Microdado_Amostra = bd_quest_socio_notas_deficiencia.buscar_dataframe_no_banco(ano)

        relatorio = 1800

        menssagem1 = "Dados Gerais do enem"
        menssagem = """<br>
        Esta é uma plataforma online que possibilitar a realização
         de uma análise de forma simples, eficiente, e no menor período possível 
         referente aos microdados socioeconômicos do ENEM nos períodos de 2018 e 2019."""

        fig = go.Figure(data=[go.Table(
            header=dict(values=['Ano', 'Quantidade de Inscritos']),
            cells=dict(values=[['2016', '2017', '2018', '2019'],
                               [5335345, 2537645, 3433078, 5775045]
                               ]))
        ])

        relatorio_em_quadro = fig.to_html()

        context = {
            'form': form,
            'menssagem': menssagem,
            'menssagem1': menssagem1,
            'relatorio_em_quadro': relatorio_em_quadro,
            'relatorio': relatorio,
        }

    return render(request, 'dashboard/dashboard.html', context=context)
