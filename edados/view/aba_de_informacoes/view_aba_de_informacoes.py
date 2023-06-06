from django.contrib.auth.decorators import login_required, user_passes_test
from edados.formularios.filtros.filtros_ano import Formulario_filtro_ano
from django.contrib.auth.decorators import login_required
from django.utils.html  import  format_html_join
from usuarios.forms  import LoginForm as forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from usuarios.models import  Usuario
from django.contrib import messages
from collections import deque
import os

def formatar(valor):
    return "{:,.2f}".format(valor)


@login_required
def aba_de_informacoes(request):

    if request.method == 'GET':

        menssagem1 ="""Informações da plataforma E-DADOS V1.26""" 
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
@user_passes_test(lambda user: user.is_superuser)
def cadastrar_usuarios(request):

    if request.method == 'GET':

        correcoes ="""Cadastrar Usuários na Plataforma:""" 
        # menssagem = """"""
        menssagem = """Antes de criar um login para um usuário verifique se ele está comprometido com os termos da plataforma."""

        menssagem = menssagem.split('\n')
        menssagem = format_html_join(
            '\n', '<h6 class="font-weight-normal">{}</h6>', ((line,) for line in menssagem))

        correcoes = correcoes.split('\n')
        correcoes = format_html_join(
            '\n', '<h4 class="font-weight-normal mt-3 mb-0">{}</h4>', ((line,) for line in correcoes))
        
        form = forms()

        context = {
            'form': form,
            'menssagem': menssagem,
            'correcoes': correcoes,
        }
        return render(request, 'base/aba_de_informacoes/cadastrar_usuarios.html', context=context)
    else:
        
        import os
        from pathlib import Path
        from edados.database import conect_db
        from sqlalchemy.orm import sessionmaker

        correcoes ="""Cadastrar Usuários na Plataforma:""" 
        # menssagem = """"""
        menssagem = """Antes de criar um login para um usuário verifique se ele está comprometido com os termos da plataforma."""

        menssagem = menssagem.split('\n')
        menssagem = format_html_join(
            '\n', '<h6 class="font-weight-normal">{}</h6>', ((line,) for line in menssagem))

        correcoes = correcoes.split('\n')
        correcoes = format_html_join(
            '\n', '<h4 class="font-weight-normal mt-3 mb-0">{}</h4>', ((line,) for line in correcoes))
        

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # Verificar se o nome de usuário já existe com um ID diferente
            usuario_existente = User.objects.get(username=nome)
            
        
            messages.info(request, 'O nome de usuário já está em uso!')
            form = forms(initial={'nome': nome, 'email': email})
            
            context = {
                'form': form,
                'nome_usuario': nome,
                'email_usuario': email,
                'menssagem': menssagem,
                'correcoes': correcoes,
            }
            return render(request, 'base/aba_de_informacoes/editar_usuario.html', context=context)
            
        except User.DoesNotExist:
            # Se o nome de usuário não estiver em uso, continue com o restante do código
            pass
            
        engine = conect_db.connect()
        # Conectando com o Banco de Dados
        Session = sessionmaker(bind=engine)
        session = Session()
        comando_sql = """ INSERT INTO "csv" ("nome") VALUES""" + "('"+nome+"');"
        session.execute(comando_sql)
        session.commit()
    
        # Crie uma instância do usuário
        user = User(username=nome, email=email)
        user.set_password(password)
        user.save()
        
        BASE_DIR = Path(__file__).resolve().parents[3]
        caminho = str(BASE_DIR) + '/static/csv/'
        
        pasta_usuario = os.path.join(caminho, nome)
        os.makedirs(pasta_usuario, exist_ok=True)
        
        arquivo_usuario = os.path.join(pasta_usuario, 'microdados_enem.csv')
        with open(arquivo_usuario, 'w') as arquivo:
            # Faça qualquer operação de escrita necessária no arquivo
            arquivo.write('')
                
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        email = request.POST.get('email')
        
        # correcao = Usuario(nome=nome, descricao=descricao, email=email)
        # correcao.save()

        
        messages.success(request, 'Usuário Cadastrado com Sucesso!')
        form = forms(request.POST)
        if form.is_valid():
            # Lida com os dados do formulário aqui
            nome = form.cleaned_data['nome']
            descricao = form.cleaned_data['descricao']
            email = form.cleaned_data['email']
            # Limpa o formulário

        form = forms()

        context = {
            'form': form,
            'menssagem': menssagem,
            'correcoes': correcoes,
        }
        return render(request, 'base/aba_de_informacoes/cadastrar_usuarios.html', context=context)

@login_required
@user_passes_test(lambda user: user.is_superuser)
def editar_usuario(request):

    if request.method == 'GET':

        correcoes ="""Cadastrar Usuários na Plataforma:""" 
        
        
        menssagem = """Antes de criar um login para um usuário verifique se ele está comprometido com os termos da plataforma."""

        menssagem = menssagem.split('\n')
        menssagem = format_html_join(
            '\n', '<h6 class="font-weight-normal">{}</h6>', ((line,) for line in menssagem))

        correcoes = correcoes.split('\n')
        correcoes = format_html_join(
            '\n', '<h4 class="font-weight-normal mt-3 mb-0">{}</h4>', ((line,) for line in correcoes))
        
        form = forms()

        id_usuario  = request.GET.get('id_usuario')
        nome_usuario  = request.GET.get('nome')
        email_usuario  = request.GET.get('email')
        verificador  = request.GET.get('verificador')
        if(verificador=='true'):
            print("ID Usuário:")
            print(id_usuario)
            print(nome_usuario)
            print(email_usuario)
            print("-----------------------------------------------------------------------")
        
                
        context = {
            'form': form,
            'id_usuario': id_usuario,
            'nome_usuario': nome_usuario,
            'email_usuario': email_usuario,
            'menssagem': menssagem,
            'correcoes': correcoes,
        }
        return render(request, 'base/aba_de_informacoes/correcoes_bugs.html', context=context)
    else:
        
        from django.core.exceptions import ValidationError
        from django.db.models import Q
        from django.http import HttpResponse
        
        form = forms(request.POST)
        nome_usuario = form.data['nome']
        id_usuario  = request.POST.get('id_usuario')
        email_usuario  = request.POST.get('email')
        verificador  = request.POST.get('verificador')
        descricao  = request.POST.get('descricao')
        
        if form.is_valid():
            # Dados do formulário são válidos, pode prosseguir com a atualização
            nome_usuario = form.cleaned_data['nome']
            email_usuario = form.cleaned_data['email']
            descricao = form.cleaned_data['descricao']

        correcoes ="""Editar Usuário:""" 
        # menssagem = """"""
        menssagem = """Antes de editar o login de um usuário verifique se realmente é necessario."""

        menssagem = menssagem.split('\n')
        menssagem = format_html_join(
            '\n', '<h6 class="font-weight-normal">{}</h6>', ((line,) for line in menssagem))

        correcoes = correcoes.split('\n')
        correcoes = format_html_join(
            '\n', '<h4 class="font-weight-normal mt-3 mb-0">{}</h4>', ((line,) for line in correcoes))
    
        print("ID Usuário:")
        print(id_usuario)
        print(nome_usuario)
        print(email_usuario)
        print("-----------------------------------------------------------------------")
        try:
            # Verificar se o nome de usuário já existe com um ID diferente
            usuario_existente = User.objects.exclude(id=id_usuario).get(username=nome_usuario)
            
        
            messages.info(request, 'O nome de usuário já está em uso!')
            form = forms(initial={'nome': nome_usuario, 'email': email_usuario, 'descricao': descricao})
            
            context = {
                'form': form,
                'id_usuario': id_usuario,
                'nome_usuario': nome_usuario,
                'email_usuario': email_usuario,
                'menssagem': menssagem,
                'correcoes': correcoes,
            }
            return render(request, 'base/aba_de_informacoes/editar_usuario.html', context=context)
            
        except User.DoesNotExist:
            # Se o nome de usuário não estiver em uso, continue com o restante do código
            pass
            
            if(verificador=='true'):
                
                form = forms(initial={'nome': nome_usuario, 'email': email_usuario, 'descricao': descricao})
                
                context = {
                    'form': form,
                    'id_usuario': id_usuario,
                    'nome_usuario': nome_usuario,
                    'email_usuario': email_usuario,
                    'menssagem': menssagem,
                    'correcoes': correcoes,
                }
                return render(request, 'base/aba_de_informacoes/editar_usuario.html', context=context)
            else:
                password_usuario = form.data['password']
                
            # Buscar o usuário existente no banco de dados
            usuario = User.objects.get(id=int(id_usuario))
            usuario.set_password(password_usuario)
            
            # Atualizar os valores do usuário
            usuario.username = nome_usuario
            usuario.descricao = descricao
            usuario.email = email_usuario

            # Salvar as alterações
            
            if form.is_valid():
                usuario.save()
            messages.success(request, 'Usuário Atualizado com Sucesso!')
            
            form = forms()
            
            context = {
                'form': form,
                'menssagem': menssagem,
                'correcoes': correcoes,
            }
            return redirect('listar_usuarios')

@login_required
@user_passes_test(lambda user: user.is_superuser)
def log_de_acesso(request):

    if request.method == 'GET':
        from pathlib import Path

        correcoes ="""Log de Acesso:""" 
        # menssagem = """"""
        menssagem = """O Log ajuda a entender e compreender como estão as requisições no Back-end."""

        menssagem = menssagem.split('\n')
        menssagem = format_html_join(
            '\n', '<h6 class="font-weight-normal">{}</h6>', ((line,) for line in menssagem))

        correcoes = correcoes.split('\n')
        correcoes = format_html_join(
            '\n', '<h4 class="font-weight-normal mt-3 mb-0">{}</h4>', ((line,) for line in correcoes))
        
        BASE_DIR = Path(__file__).resolve().parents[3]
        caminho = str(BASE_DIR) + '/Registros_Acesso.log'

        # Verificar se o arquivo existe
        if os.path.exists(caminho):
            # Criar uma deque com tamanho máximo de 100 elementos
            ultimas_linhas = deque(maxlen=1000)

            with open(caminho, 'r') as file:
                # Ler as linhas do arquivo
                for linha in file:
                    # Adicionar a linha atual à deque
                    ultimas_linhas.append(linha)

            # Converter a deque em uma string única com as últimas 100 linhas
            log_de_acesso = ''.join(ultimas_linhas)
        else:
            log_de_acesso = 'Arquivo de log não encontrado.'


        # BASE_DIR = Path(__file__).resolve().parents[3]
        # caminho = str(BASE_DIR) + '/Registros_Acesso.log'
        
        # with open(caminho, 'r') as file:
        #     log_de_acesso = file.read()

        form = forms()

        context = {
            'form': form,
            'menssagem': menssagem,
            'log_de_acesso': log_de_acesso,            
            'correcoes': correcoes,
        }
        return render(request, 'base/aba_de_informacoes/log_de_acesso.html', context=context)
    else:
        
        menssagem = """O Log ajuda a entender e compreender como estão as requisições no Back-end."""

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
        return render(request, 'base/aba_de_informacoes/log_de_acesso.html', context=context)

@login_required
@user_passes_test(lambda user: user.is_superuser)
def listar_usuarios(request):

    if request.method == 'GET':
        from django.contrib.auth.models import User

        correcoes ="""Lista de Usuários:""" 
        # menssagem = """"""
        menssagem = """Antes de deletar o login de um usuário, verifique se é realmente necessário.
        Não esqueça que há a opção de bloqueá-lo, modificando a senha de acesso dele."""

        menssagem = menssagem.split('\n')
        menssagem = format_html_join(
            '\n', '<h6 class="font-weight-normal">{}</h6>', ((line,) for line in menssagem))

        correcoes = correcoes.split('\n')
        correcoes = format_html_join(
            '\n', '<h4 class="font-weight-normal mt-3 mb-0">{}</h4>', ((line,) for line in correcoes))
        
        users = User.objects.all()

        form = forms()
        
        context = {
            'form': form,
            'users': users,
            'menssagem': menssagem,
            'correcoes': correcoes,
        }
        return render(request, 'base/aba_de_informacoes/listar_usuarios.html', context=context)
    else:
        
        from django.contrib.auth.models import User
        from django.http import HttpResponse
            
        # Obtenha o nome de usuário a ser excluído dos dados da solicitação
        username = request.POST.get('username')
        
        try:
            # Busque o usuário pelo nome de usuário
            user = User.objects.get(username=username)
            # Exclua o usuário
            user.delete()
            from pathlib import Path
            import shutil
            import os
            
            BASE_DIR = Path(__file__).resolve().parents[3]
            caminho = str(BASE_DIR) + '/static/csv/'
            
            pasta_usuario = os.path.join(caminho, username)
            os.makedirs(pasta_usuario, exist_ok=True)
            
            print('_____________________________________________________________')
            print(pasta_usuario)
            print('_____________________________________________________________')

            
            shutil.rmtree(pasta_usuario)
            # Realize qualquer outra ação necessária após a exclusão

                # Retorne uma resposta de sucesso, se necessário
            messages.success(request, 'Usuário excluído com sucesso!')
        
        except User.DoesNotExist:
            # Trate o caso em que o usuário não existe
                # Retorne uma resposta de sucesso, se necessário
            messages.success(request, 'Usuário não encontrado!')    
    
        form = forms()
        
        correcoes ="""Lista de Usuários:""" 
        # menssagem = """"""
        menssagem = """Antes de deletar o login de um usuário, verifique se é realmente necessário.
        Não esqueça que há a opção de bloqueá-lo, modificando a senha de acesso dele."""

        menssagem = menssagem.split('\n')
        menssagem = format_html_join(
            '\n', '<h6 class="font-weight-normal">{}</h6>', ((line,) for line in menssagem))

        correcoes = correcoes.split('\n')
        correcoes = format_html_join(
            '\n', '<h4 class="font-weight-normal mt-3 mb-0">{}</h4>', ((line,) for line in correcoes))
        
        users = User.objects.all()
        
        context = {
            'form': form,
            'users': users,
            'menssagem': menssagem,
            'correcoes': correcoes,
        }
        return render(request, 'base/aba_de_informacoes/listar_usuarios.html', context=context)

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
