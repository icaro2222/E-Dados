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

#         menssagem1 = "Dados Gerais do Enem"        
#         menssagem = """Esta plataforma online oferece uma solução para análise de microdados socioeconômicos do ENEM, referentes aos anos de 2017, 2018 e 2019. No entanto, algumas colunas importantes foram removidas pelo INEP, como os dados sobre alunos com deficiência, o que inviabilizou a análise sem essas informações específicas.
# Para garantir dados consistentes, foram utilizados apenas os dados dos inscritos presentes em todas as provas, ou seja, aqueles com TP_PRESENCA_CN ==1, TP_PRESENCA_CH==1, TP_PRESENCA_LC == 1 e TP_PRESENCA_MT == 1. Dessa forma, alunos que não compareceram não interferem nos resultados.
# A plataforma utiliza técnicas avançadas da ciência de dados para permitir uma análise precisa e detalhada dos dados, fornecendo insights valiosos para a tomada de decisões estratégicas em relação ao desempenho dos candidatos. Com uma interface intuitiva e funcionalidades de filtragem e visualização de dados, é uma ferramenta poderosa para pesquisadores, gestores educacionais e profissionais da área de educação que buscam aprimorar a compreensão dos fatores que influenciam o desempenho dos estudantes no ENEM."""


        menssagem1 = "Bem-vindo à E-DADOS!"
        # menssagem = """Essa plataforma online oferece uma solução para a análise de microdados socioeconômicos do ENEM referentes aos anos de 2016, 2017, 2018 e 2019 de maneira eficiente e ágil. Utilizando técnicas avançadas da ciência de dados, a plataforma possibilita uma análise precisa e detalhada dos dados, com o objetivo de fornecer insights valiosos para a tomada de decisões estratégicas em relação ao desempenho dos candidatos nas provas. Com uma interface intuitiva e funcionalidades de filtragem e visualização de dados, a plataforma é uma ferramenta poderosa para pesquisadores, gestores educacionais e profissionais da área de educação interessados em aprimorar a compreensão dos fatores que influenciam o desempenho dos estudantes no ENEM."""
        menssagem = """A plataforma (protótipo) especializada em análise dos microdados socioeconômicos do ENEM. Explore os dados, obtenha insights valiosos e tome decisões estratégicas com eficiência. Vamos começar!"""

        menssagem = menssagem.split('\n')
        menssagem = format_html_join(
            '\n', '<p class="font-weight-normal">{}</p>', ((line,) for line in menssagem))

        # form = DashboardFormulario()

        # fig = go.Figure(data=[go.Table(
        #     header=dict(
        #         values=['Ano', 'Quantidade de Inscritos']),
        #     cells=dict(
        #         values=[['2021', '2020', '2019', '2018', '2017', '2016',
        #                  '2015', '2014', '2013', '2012', '2011', '2010'],
        #                 [4004764, 5783357, 5095308, 5513662,
        #                  6731186, 8627371, 7792025, 8722290,
        #                  7173574, 5791332, 5380857, 4626094
        #                  ]
        #                 ]))
        # ])

        # figura = go.Figure()

        # figura.add_bar(
        #     x=['2010', '2011', '2012', '2013', '2014', '2015',
        #        '2016', '2017', '2018', '2019', '2020', '2021'],
        #     y=[4626094, 5380857,  5791332, 7173574,
        #        8722290, 7792025,  8627371,	6731186,
        #        5513662, 5095308, 5783357, 4004764
        #        ],
        #     name='Num de inscritos')

        # figura.add_scatter(
        #     x=['2010', '2011', '2012', '2013', '2014', '2015',
        #        '2016', '2017', '2018', '2019', '2020', '2021'],
        #     y=[4626094, 5380857,  5791332, 7173574,
        #        8722290, 7792025,  8627371,	6731186,
        #        5513662, 5095308, 5783357, 4004764
        #        ],
        #     name='Num de inscritos')

        # figura.update_layout(
        #     title_text='Quantidade de inscrições no Enem, por ano.',
        #     width=500,
        #     margin=dict(l=50, r=50, b=150, t=50),
        #     xaxis=dict(
        #         title="Ano",
        #         title_standoff=10
        #     ),
        #     yaxis_title="Quantidade de Inscritos",
        #     font=dict(
        #         family="Arial",
        #         size=12,
        #         color="black"
        #     ),
        #     annotations=[
        #         dict(
        #             x=0,
        #             y=-0.5,
        #             xref="paper",
        #             yref="paper",
        #             text="Legenda: <br>Num de inscritos: esta legenda indica o número de alunos<br>que realizaram a inscrição no Enem no respectivo ano.",
        #             showarrow=False,
        #             align="left",
        #             font=dict(
        #                 family="Arial",
        #                 size=13,
        #                 color="black"
        #             )
        #         )
        #     ],
        #     plot_bgcolor='white'
        # )

        # fig.update_layout(
        #     title_text='Quantidade de inscrições no Enem, por ano.',
        #     width=500,
        #     xaxis_title="Ano",
        #     yaxis_title="Quantidade de Inscritos",
        #     legend_title="Legenda",
        #     margin=dict(l=50, r=50, b=150, t=50),
        #     font=dict(
        #         family="Arial",
        #         size=12,
        #         color="black"
        #     ),
        #     annotations=[
        #         dict(
        #             x=0,
        #             y=-0.5,
        #             xref="paper",
        #             yref="paper",
        #             text="Legenda: <br>Quantidade de Inscritos: esta legenda indica o número de alunos<br>que realizaram a inscrição no Enem no respectivo ano.",
        #             showarrow=False,
        #             align="left"
        #             # ,
        #             # font=dict(
        #             #     family="Arial",
        #             #     size=13,
        #             #     color="dark"
        #             # )
        #         )
        #     ]
        # )

        # relatorio_em_quadro = fig.to_html()
        # relatorio = figura.to_html()

        context = {
            # 'form': form,
            'menssagem': menssagem,
            'menssagem1': menssagem1,
            # 'relatorio': relatorio,
            # 'relatorio_em_quadro': relatorio_em_quadro
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
