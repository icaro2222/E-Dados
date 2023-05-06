import os
from django.contrib.auth.decorators import login_required
from typing import Sized
import plotly.graph_objects as go
from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib as mpl
from edados.formularios.dashboard.formulario_dashboard import DashboardFormulario
import numpy as np
from edados.database import bd_quest_socio_notas_deficiencia, conect_db
from django.utils.html import format_html_join


def formatar(valor):
    return "{:,.2f}".format(valor)


@login_required
def aba_de_informacoes(request):

    if request.method == 'GET':

        menssagem1 ="""Informações da plataforma E-DADOS V1.23""" 
        # menssagem = """"""
        menssagem = """
A E-DADOS é uma plataforma online que tem por objetivo estudar os dados do Enem em busca de informações relevantes sobre as pessoas com deficiência. Ela oferece uma solução para a análise de microdados socioeconômicos do ENEM referentes aos anos de 2016, 2017, 2018 e 2019 de maneira eficiente e ágil.

Utilizando técnicas avançadas da ciência de dados, a plataforma possibilita uma análise precisa e detalhada dos dados, com o objetivo de fornecer insights valiosos para a tomada de decisões estratégicas em relação ao desempenho dos candidatos nas provas. Com uma interface intuitiva e funcionalidades de filtragem e visualização de dados, a plataforma é uma ferramenta poderosa para pesquisadores, gestores educacionais e profissionais da área de educação interessados em aprimorar a compreensão dos fatores que influenciam o desempenho dos estudantes no ENEM.

A E-DADOS foi desenvolvida utilizando Django, um framework web de alto nível em Python que incentiva o desenvolvimento rápido e o design limpo e pragmático. O backend da plataforma utiliza PostgreSQL, um sistema de gerenciamento de banco de dados relacional de código aberto e muito popular. Já para o frontend, a plataforma utiliza Bootstrap, um framework front-end popular para design responsivo e de fácil utilização.

Para acessar a plataforma, é necessário fazer login utilizando um usuário e senha previamente cadastrados. É possível visualizar as informações de todos os usuários cadastrados no sistema e gerenciar suas permissões de acesso. A plataforma também oferece recursos de exportação de dados para formatos como CSV e Excel.
"""

        menssagem = menssagem.split('\n')
        menssagem = format_html_join(
            '\n', '<p class="font-weight-normal">{}</p>', ((line,) for line in menssagem))

        context = {
            # 'form': form,
            'menssagem': menssagem,
            'menssagem1': menssagem1,
        }
        return render(request, 'base/aba_de_informacoes/aba_de_informacoes.html', context=context)
    else:



        menssagem1 = "Dados Gerais do enem"
        menssagem = """<br>
        Esta é uma plataforma online quM nos periodos de 2018 e 2019."""


        context = {
            'menssagem': menssagem,
            'menssagem1': menssagem1
        }

    return render(request, 'aba_de_informacoes/aba_de_informacoes.html', context=context)
