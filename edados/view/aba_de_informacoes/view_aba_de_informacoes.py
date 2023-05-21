from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from edados.formularios.aba_informacoes.correcoes import form_correcoes
from django.utils.html import format_html_join
from  correcoes.models import Correcao
from edados.formularios.filtros.filtros_ano import Formulario_filtro_ano
from django.contrib import messages

def formatar(valor):
    return "{:,.2f}".format(valor)


@login_required
def aba_de_informacoes(request):

    if request.method == 'GET':

        menssagem1 ="""Informações da plataforma E-DADOS V1.25.4""" 
        # menssagem = """"""
        menssagem = """
A E-DADOS é uma plataforma online cujo objetivo é estudar os dados do Enem em busca de informações relevantes sobre as pessoas com deficiência. Ela oferece uma solução para a análise de microdados socioeconômicos do ENEM referentes aos anos de 2016, 2017, 2018 e 2019 de maneira eficiente e ágil.

Utilizando técnicas avançadas da ciência de dados, a plataforma possibilita uma análise precisa e detalhada dos dados, visando fornecer insights valiosos para a tomada de decisões estratégicas em relação ao desempenho dos candidatos nas provas. Com uma interface intuitiva e funcionalidades de filtragem e visualização de dados, a plataforma é uma ferramenta poderosa para pesquisadores, gestores educacionais e profissionais da área de educação interessados em aprimorar a compreensão dos fatores que influenciam o desempenho dos estudantes no ENEM.

A E-DADOS foi desenvolvida utilizando Django, um framework web de alto nível em Python que incentiva o desenvolvimento rápido e o design limpo e pragmático. O backend da plataforma utiliza PostgreSQL, um sistema de gerenciamento de banco de dados relacional de código aberto e muito popular. Já para o frontend, a plataforma utiliza Bootstrap, um framework front-end popular para design responsivo e de fácil utilização.

Para acessar a plataforma, é necessário fazer login utilizando um usuário e senha previamente cadastrados. É possível visualizar as informações de todos os usuários cadastrados no sistema e gerenciar suas permissões de acesso. A plataforma também oferece recursos de exportação de dados para formatos como CSV e Excel.
"""

        menssagem = menssagem.split('\n')
        menssagem = format_html_join(
            '\n', '<p class="font-weight-normal">{}</p>', ((line,) for line in menssagem))

        menssagem1 = menssagem1.split('\n')
        menssagem1 = format_html_join(
            '\n', '<h4 class="font-weight-normal mb-0 mt-3">{}</h4>', ((line,) for line in menssagem1))

        context = {
            # 'form': form,
            'menssagem': menssagem,
            'menssagem1': menssagem1,
        }
        return render(request, 'base/aba_de_informacoes/aba_de_informacoes.html', context=context)
    else:



        menssagem1 = "Dados Gerais do enem"
        menssagem = """<br>
        Esta é uma plataforma online que nos períodos de 2018 e 2019."""


        context = {
            'menssagem': menssagem,
            'menssagem1': menssagem1
        }

    return render(request, 'aba_de_informacoes/aba_de_informacoes.html', context=context)

@login_required
def correcoes_bugs(request):

    if request.method == 'GET':

        correcoes =""" Informe-nos os erros ou bugs que você encontrou na plataforma:""" 
        # menssagem = """"""
        menssagem = """Nossa equipe está empenhada em fornecer as melhores ferramentas para aprimorar ainda mais nossa plataforma."""

        menssagem = menssagem.split('\n')
        menssagem = format_html_join(
            '\n', '<h6 class="font-weight-normal">{}</h6>', ((line,) for line in menssagem))

        correcoes = correcoes.split('\n')
        correcoes = format_html_join(
            '\n', '<h4 class="font-weight-normal mt-3 mb-0">{}</h4>', ((line,) for line in correcoes))
        
        form = form_correcoes()

        context = {
            'form': form,
            'menssagem': menssagem,
            'correcoes': correcoes,
        }
        return render(request, 'base/aba_de_informacoes/correcoes_bugs.html', context=context)
    else:
        
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        email = request.POST.get('email')
        
        correcao = Correcao(nome=nome, descricao=descricao, email=email)
        correcao.save()
        messages.success(request, 'Relatório enviada com sucesso!')
        form = form_correcoes(request.POST)
        if form.is_valid():
            # Lida com os dados do formulário aqui
            nome = form.cleaned_data['nome']
            descricao = form.cleaned_data['descricao']
            email = form.cleaned_data['email']
            # Limpa o formulário

        form = form_correcoes()

        correcoes =""" Informe-nos os erros ou bugs que você encontrou na plataforma:""" 
        # menssagem = """"""
        menssagem = """Nossa equipe está empenhada em fornecer as melhores ferramentas para aprimorar ainda mais nossa plataforma."""

        menssagem = menssagem.split('\n')
        menssagem = format_html_join(
            '\n', '<h6 class="font-weight-normal">{}</h6>', ((line,) for line in menssagem))

        correcoes = correcoes.split('\n')
        correcoes = format_html_join(
            '\n', '<h4 class="font-weight-normal mt-3 mb-0">{}</h4>', ((line,) for line in correcoes))
        

        context = {
            'form': form,
            'menssagem': menssagem,
            'correcoes': correcoes,
        }
        return render(request, 'base/aba_de_informacoes/correcoes_bugs.html', context=context)

@login_required
def criadores(request):

    if request.method == 'GET':
        
        menssagem1 ="""Informações dos Criadores da plataforma E-DADOS:""" 
        instituicao ="""Instituição: IFBAIANO Campos Guanambi""" 
        
        aluno ="""Discente: Ícaro Dias dos Santos""" 
        menssagem_aluno ="""ÁREA DE FORMAÇÃO: Graduando em Análise e Desenvolvimento de Sistema (IFBaiano)
        TITULAÇÃO MÁXIMA: Graduando
        icarodias2222@gmail.com""" 
        
        
        orientador ="""Orientador: Woquiton Lima Fernandes""" 
        menssagem_orientador ="""ÁREA DE FORMAÇÃO: Processamentos de Dados, 2003, FATEC SP/UNESC
        MESTRADO: Tecnologia da Informação e Comunicação na Formação em EAD. 2007. UFC
        DOUTORADO: Educação Especial.2016. UFSCAR
        TITULAÇÃO MÁXIMA: Doutorado
        ÁREA DE INGRESSO: INFORMÁTICA
        woquiton.fernandes@ifbaiano.edu.br""" 
        
        
        coo_orientador ="""Coo Orientadora: Daniele de Brito Trindade""" 
        menssagem_coo_orientador ="""ÁREA DE FORMAÇÃO: Bacharelado em Estatística (Matemática / Estatística )
        MESTRADO: Mestrado em Estatística (CCEN)
        DOUTORADO: Doutorado em Estatística (CCEN)
        TITULAÇÃO MÁXIMA: Doutorado
        daniele.trindade@ifbaiano.edu.br""" 
        
        
        menssagem = """   Instituto Federal de Educação, Ciência e Tecnologia Baiano – Campus Guanambi
        
        Zona Rural - Distrito de Ceraíma, Bahia - CEP: 46430-000

        Tel.: (77) 3493-2100
        Diretor: Carlito José de Barros Filho
        E-mail: gabinete@guanambi.ifbaiano.edu.br
        Instituto Federal de Educação, Ciência e Tecnologia Baiano
        Reitoria: Rua do Rouxinol, nº 115, Imbuí, Salvador-BA. 
        CEP: 41720-052. CNPJ: 10.724.903/0001-79 Telefone: (71) 3186-0001 | E-mail: gabinete@ifbaiano.edu.br"""

        menssagem1 = menssagem1.split('\n')
        menssagem1 = format_html_join(
            '\n', '<h4 class="font-weight-normal mt-3 mb-0 d-flex aligh-items-center justify-content-center">{}</h4>', ((line,) for line in menssagem1))

        menssagem = menssagem.split('\n')
        menssagem = format_html_join(
            '\n', '<h6 class="font-weight-normal d-flex aligh-items-center justify-content-center">{}</h6>', ((line,) for line in menssagem))

        instituicao = instituicao.split('\n')
        instituicao = format_html_join(
            '\n', '<h5 class="font-weight-normal mb-0">{}</h6>', ((line,) for line in instituicao))

        aluno = aluno.split('\n')
        aluno = format_html_join(
            '\n', '<h5 class="font-weight-normal mb-0">{}</h6>', ((line,) for line in aluno))

        menssagem_aluno = menssagem_aluno.split('\n')
        menssagem_aluno = format_html_join(
            '\n', '<h6 class="font-weight-normal mt-3 mb-3 d-flex aligh-items-center justify-content-center">{}</h6>', ((line,) for line in menssagem_aluno))

        orientador = orientador.split('\n')
        orientador = format_html_join(
            '\n', '<h5 class="font-weight-normal mb-0">{}</h6>', ((line,) for line in orientador))

        menssagem_orientador = menssagem_orientador.split('\n')
        menssagem_orientador = format_html_join(
            '\n', '<h6 class="font-weight-normal mb-3  d-flex aligh-items-center justify-content-center">{}</h6>', ((line,) for line in menssagem_orientador))

        coo_orientador = coo_orientador.split('\n')
        coo_orientador = format_html_join(
            '\n', '<h5 class="font-weight-normal mb-0">{}</h6>', ((line,) for line in coo_orientador))

        menssagem_coo_orientador = menssagem_coo_orientador.split('\n')
        menssagem_coo_orientador = format_html_join(
            '\n', '<h6 class="font-weight-normal mb-3  d-flex aligh-items-center justify-content-center">{}</h6>', ((line,) for line in menssagem_coo_orientador))

        context = {
            # 'form': form,
            'menssagem': menssagem,
            'menssagem1': menssagem1,
            'instituicao': instituicao,
            'aluno': aluno,
            'menssagem_aluno': menssagem_aluno,
            'orientador': orientador,
            'menssagem_orientador': menssagem_orientador,
            'coo_orientador': coo_orientador,
            'menssagem_coo_orientador': menssagem_coo_orientador,
        }
        return render(request, 'base/aba_de_informacoes/criadores.html', context=context)

    else:



        menssagem1 = "Dados Gerais do enem"
        menssagem = """<br>
        Esta é uma plataforma online que nos períodos de 2016, 2017, 2018 e 2019."""


        context = {
            'menssagem': menssagem,
            'menssagem1': menssagem1
        }

    return render(request, 'base/aba_de_informacoes/criadores.html', context=context)

@login_required
def dicionario_microdados(request):

        
    if request.method == 'GET':
        
        form = Formulario_filtro_ano()

        menssagem1 ="""Dicionário dos Microdados do Enem:"""       
 
        menssagem1 = menssagem1.split('\n')
        menssagem1 = format_html_join(
            '\n', '<h4 class="font-weight-normal mt-3 mb-0 d-flex aligh-items-end justify-content-end">{}</h4>', ((line,) for line in menssagem1))
        
        context = {
            'form': form,
            'menssagem1': menssagem1,
        }
        return render(request, 'base/aba_de_informacoes/dicionario_microdados.html', context=context)

    else:
        
        form = Formulario_filtro_ano()

        menssagem1 ="""Dicionário dos Microdados do Enem:"""       
 
        menssagem1 = menssagem1.split('\n')
        menssagem1 = format_html_join(
            '\n', '<h4 class="font-weight-normal mt-3 mb-0 d-flex aligh-items-end justify-content-end">{}</h4>', ((line,) for line in menssagem1))
        
        context = {
            'form': form,
            'menssagem1': menssagem1,
        }
    
    return render(request, 'base/aba_de_informacoes/dicionario_microdados.html', context=context)
