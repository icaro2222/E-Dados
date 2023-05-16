from random import choices
from django import forms

# DADOS DO QUESTIONÁRIO SOCIOECONÔMICO
def questionario_socioeconomico(Form):


    choices_questao = ( ('Q001' ,'Q001 - Até que série seu pai, ou o homem responsável por você, estudou?'),
                        ('Q002', 'Q002 - Até que série sua mãe, ou a mulher responsável por você, estudou?'),
                        # ('Q003', 'Q003 - A partir da apresentação de algumas ocupações divididas em grupos ordenados, indique o grupo que contempla a ocupação mais próxima da ocupação do seu pai ou do homem responsável por você. (Se ele não estiver trabalhando, escolha uma ocupação pensando no último trabalho dele).'),
                        # ('Q004', 'Q004 - A partir da apresentação de algumas ocupações divididas em grupos ordenados, indique o grupo que contempla a ocupação mais próxima da ocupação da sua mãe ou da mulher responsável por você. (Se ela não estiver trabalhando, escolha uma ocupação pensando no último trabalho dela).'),
                        ('Q003', 'Q003 - Indique o grupo que contempla a ocupação mais próxima da ocupação do seu pai ou do homem responsável por você.'),
                        ('Q004', 'Q004 - Indique o grupo que contempla a ocupação mais próxima da ocupação da sua mãe ou da mulher responsável por você.'),
                        ('Q005', 'Q005 - Incluindo você, quantas pessoas moram atualmente em sua residência?'),
                        ('Q006', 'Q006 - Qual é a renda mensal de sua família? (Some a sua renda com a dos seus familiares.)'),
                        ('Q007', 'Q007 - Em sua residência trabalha empregado(a) doméstico(a)?'),
                        ('Q008', 'Q008 - Na sua residência tem banheiro?'),
                        ('Q009', 'Q009 - Na sua residência tem quartos para dormir?'),
                        ('Q010', 'Q010 - Na sua residência tem carro?'),
                        ('Q011', 'Q011 - Na sua residência tem motocicleta?'),
                        ('Q012', 'Q012 - Na sua residência tem geladeira?'),
                        ('Q013', 'Q013 - Na sua residência tem freezer (independente ou segunda porta da geladeira)?'),
                        ('Q014', 'Q014 - Na sua residência tem máquina de lavar roupa? (o tanquinho NÃO deve ser considerado)'),
                        ('Q015', 'Q015 - Na sua residência tem máquina de secar roupa (independente ou em conjunto com a máquina de lavar roupa)?'),
                        ('Q016', 'Q016 - Na sua residência tem forno micro-ondas?'),
                        ('Q017', 'Q017 - Na sua residência tem máquina de lavar louça?'),
                        ('Q018', 'Q018 - Na sua residência tem aspirador de pó?'),
                        ('Q019', 'Q019 - Na sua residência tem televisão em cores?'),
                        ('Q020', 'Q020 - Na sua residência tem aparelho de DVD?'),
                        ('Q021', 'Q021 - Na sua residência tem TV por assinatura?'),
                        ('Q022', 'Q022 - Na sua residência tem telefone celular?'),
                        ('Q023', 'Q023 - Na sua residência tem telefone fixo?'),
                        ('Q024', 'Q024 - Na sua residência tem computador?'),
                        ('Q025', 'Q025 - Na sua residência tem acesso à Internet?'))
            
    # questao = forms.ChoiceField(label='Questão socioeconômica a ser analisada:', choices=choices_questao)
    
    
    questao = forms.ChoiceField(
        label="""<div class="m-0" title="Essa opção permite que você escolha uma das questões socioeconômicas do Enem, e então ela contrastada com a opção de dados demográficos, como sexo, etc. A partir dessa análise, um gráfico é gerado, proporcionando insights que podem ser utilizados na criação de trabalhos ou estudos.">Questão socioeconômica a ser analisada:* <i class="fas fa-info-circle"></i></div>""", 
        choices=choices_questao,
        required=False,
        widget=forms.Select(attrs={
            'title': """Essas questões socioeconômicas têm como objetivo coletar informações sobre o contexto familiar e socioeconômico dos participantes. Elas abordam características como o nível de escolaridade dos pais ou responsáveis, ocupação dos pais, tamanho da família, renda familiar, presença de empregado doméstico, disponibilidade de recursos na residência (como banheiro, quartos, carro, eletrodomésticos, entre outros) e acesso à tecnologia (como telefone celular, computador e Internet).

Essas questões fornecem dados relevantes para a análise e compreensão do perfil socioeconômico dos participantes, auxiliando na identificação de possíveis desigualdades e impactos socioeconômicos na educação. As respostas a essas perguntas podem ser utilizadas para a elaboração de estudos, pesquisas e formulação de políticas públicas na área da educação e inclusão social.

É importante destacar que essas questões são parte integrante de um questionário mais amplo, que visa obter informações demográficas e socioeconômicas para análise estatística e compreensão do contexto dos participantes em relação ao desempenho no Exame Nacional do Ensino Médio (Enem)."""
        }))
    
    return questao