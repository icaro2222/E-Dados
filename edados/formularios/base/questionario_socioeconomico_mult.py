from random import choices
from django import forms

# DADOS DO QUESTIONÁRIO SOCIOECONÔMICO
def questionario_socioeconomico(Form):

    choices_questao = ( ('nenhum' ,'NENHUMA'),
                       ('todos' ,'TODAS'),
                        ('Q001' ,'Até que série seu pai, ou o homem responsável por você, estudou?'),
                        ('Q002', 'Até que série sua mãe, ou a mulher responsável por você, estudou?'),
                        # ('Q003', 'A partir da apresentação de algumas ocupações divididas em grupos ordenados, indique o grupo que contempla a ocupação mais próxima da ocupação do seu pai ou do homem responsável por você. (Se ele não estiver trabalhando, escolha uma ocupação pensando no último trabalho dele).'),
                        # ('Q004', 'A partir da apresentação de algumas ocupações divididas em grupos ordenados, indique o grupo que contempla a ocupação mais próxima da ocupação da sua mãe ou da mulher responsável por você. (Se ela não estiver trabalhando, escolha uma ocupação pensando no último trabalho dela).'),
                        ('Q003', 'Indique o grupo que contempla a ocupação mais próxima da ocupação do seu pai ou do homem responsável por você.'),
                        ('Q004', 'Indique o grupo que contempla a ocupação mais próxima da ocupação da sua mãe ou da mulher responsável por você.'),
                        ('Q005', 'Incluindo você, quantas pessoas moram atualmente em sua residência?'),
                        ('Q006', 'Qual é a renda mensal de sua família? (Some a sua renda com a dos seus familiares.)'),
                        ('Q007', 'Em sua residência trabalha empregado(a) doméstico(a)?'),
                        ('Q008', 'Na sua residência tem banheiro?'),
                        ('Q009', 'Na sua residência tem quartos para dormir?'),
                        ('Q010', 'Na sua residência tem carro?'),
                        ('Q011', 'Na sua residência tem motocicleta?'),
                        ('Q012', 'Na sua residência tem geladeira?'),
                        ('Q013', 'Na sua residência tem freezer (independente ou segunda porta da geladeira)?'),
                        ('Q014', 'Na sua residência tem máquina de lavar roupa? (o tanquinho NÃO deve ser considerado)'),
                        ('Q015', 'Na sua residência tem máquina de secar roupa (independente ou em conjunto com a máquina de lavar roupa)?'),
                        ('Q016', 'Na sua residência tem forno micro-ondas?'),
                        ('Q017', 'Na sua residência tem máquina de lavar louça?'),
                        ('Q018', 'Na sua residência tem aspirador de pó?'),
                        ('Q019', 'Na sua residência tem televisão em cores?'),
                        ('Q020', 'Na sua residência tem aparelho de DVD?'),
                        ('Q021', 'Na sua residência tem TV por assinatura?'),
                        ('Q022', 'Na sua residência tem telefone celular?'),
                        ('Q023', 'Na sua residência tem telefone fixo?'),
                        ('Q024', 'Na sua residência tem computador?'),
                        ('Q025', 'Na sua residência tem acesso à Internet?'))
            
    questao = forms.ChoiceField(label='Questão socioeconômica a ser analisada:', choices=choices_questao)
    return questao

    