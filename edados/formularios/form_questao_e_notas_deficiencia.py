from random import choices
from django import forms


class MeuFormulario(forms.Form):

    choices_questao = ( ('Q001' ,'Escolaridade do Pai'),
                        ('Q002', 'Escolaridade da Mãe'),
                        ('Q003', 'Ocupações do Pai'),
                        ('Q004', 'Ocupação da Mãe'),
                        ('Q005', 'Quantidade de Pessoas Moranda na Residência'),
                        ('Q006', 'Questão 06'),
                        ('Q007', 'Questão 07'),
                        ('Q008', 'Questão 08'),
                        ('Q009', 'Questão 09'),
                        ('Q010', 'Questão 10'),
                        ('Q011', 'Questão 11'),
                        ('Q012', 'Questão 12'),
                        ('Q013', 'Questão 13'),
                        ('Q014', 'Questão 14'),
                        ('Q015', 'Questão 15'),
                        ('Q016', 'Questão 16'),
                        ('Q017', 'Questão 17'),
                        ('Q018', 'Questão 18'),
                        ('Q019', 'Questão 19'),
                        ('Q020', 'Questão 20'),
                        ('Q021', 'Questão 21'),
                        ('Q022', 'Questão 22'),
                        ('Q023', 'Questão 23'),
                        ('Q024', 'Questão 24'),
                        ('Q025', 'Questão 25'),
                        ('TP_SEXO', 'Comparar Nota ao Sexo'))

# A partir da apresentação de algumas ocupações divididas em grupos ordenados, indique o grupo que contempla a ocupação mais próxima da ocupação da sua mãe ou da mulher responsável por você. (Se ela não estiver trabalhando, escolha uma ocupação pensando no último trabalho dela).
# A partir da apresentação de algumas ocupações divididas em grupos ordenados, indique o grupo que contempla a ocupação mais próxima da ocupação do seu pai ou do homem responsável por você. (Se ele não estiver trabalhando, escolha uma ocupação pensando no último trabalho dele).
# Até que série seu pai, ou o homem responsável por você, estudou?
# Até que série sua mãe, ou a mulher responsável por você, estudou?
# Em sua residência trabalha empregado(a) doméstico(a)?
# Incluindo você, quantas pessoas moram atualmente em sua residência?
# Na sua residência tem acesso à Internet?
# Na sua residência tem aparelho de DVD?
# Na sua residência tem aspirador de pó?
# Na sua residência tem banheiro?
# Na sua residência tem carro?
# Na sua residência tem computador?
# Na sua residência tem forno micro-ondas?
# Na sua residência tem freezer (independente ou segunda porta da geladeira)?
# Na sua residência tem geladeira?          
# Na sua residência tem máquina de lavar louça?
# Na sua residência tem máquina de lavar roupa? (o tanquinho NÃO deve ser considerado)
# Na sua residência tem máquina de secar roupa (independente ou em conjunto com a máquina de lavar roupa)?
# Na sua residência tem motocicleta?
# Na sua residência tem quartos para dormir?
# Na sua residência tem telefone celular?
# Na sua residência tem telefone fixo?
# Na sua residência tem televisão em cores?
# Na sua residência tem TV por assinatura?
# Qual é a renda mensal de sua família? (Some a sua renda com a dos seus familiares.)


    choices_nota = (('NU_NOTA_MT' ,'Nota em Matemática'),    
                    ('NU_NOTA_CH', 'Nota em Ciências da Natureza'),
                    ('NU_NOTA_CN' ,'Nota em Ciências Humanas'),
                    ('NU_NOTA_LC', 'Nota da prova de Linguagens e Códigos'),
                    ('NU_NOTA_COMP1', 'Nota da competência 1'),
                    ('NU_NOTA_COMP2', 'Nota da competência 2'),
                    ('NU_NOTA_COMP3', 'Nota da competência 3'),
                    ('NU_NOTA_REDACAO', 'Nota da prova de redação'))
                    
    choices_deficiencia = (('ambos' ,'Todos'),    
                    ('IN_SEM_RECURSO', 'IN SEM RECURSO'),
                    ('IN_BRAILLE', 'IN BRAILLE'),
                    ('IN_AMPLIADA_18', 'Prova Ampliada 18'),
                    ('IN_LEDOR', 'IN LEDOR'),
                    ('IN_ACESSO', 'IN ACESSO'),
                    ('IN_NOME_SOCIAL', 'Usou Nome Social'))
# 'IN_TRANSCRICAO'
# 'IN_LIBRAS'
# 'IN_TEMPO_ADICIONAL'
# 'IN_LEITURA_LABIAL'
# 'IN_MESA_CADEIRA_RODAS'
# 'IN_MESA_CADEIRA_SEPARADA'
# 'IN_APOIO_PERNA'
# 'IN_GUIA_INTERPRETE'
# 'IN_COMPUTADOR'
# 'IN_CADEIRA_ESPECIAL'
# 'IN_CADEIRA_CANHOTO'
# 'IN_CADEIRA_ACOLCHOADA'
# 'IN_PROVA_DEITADO'
# 'IN_MOBILIARIO_OBESO'
# 'IN_LAMINA_OVERLAY'
# 'IN_PROTETOR_AURICULAR'
# 'IN_MEDIDOR_GLICOSE'
# 'IN_MAQUINA_BRAILE'
# 'IN_SOROBAN'
# 'IN_MARCA_PASSO'
# 'IN_SONDA'
# 'IN_MEDICAMENTOS'
# 'IN_SALA_INDIVIDUAL'
# 'IN_SALA_ESPECIAL'
# 'IN_SALA_ACOMPANHANTE'
# 'IN_MOBILIARIO_ESPECIFICO'
# 'IN_MATERIAL_ESPECIFICO'
    questao = forms.ChoiceField(choices=choices_questao)
    nota = forms.ChoiceField(choices=choices_nota)
    deficiencia = forms.ChoiceField(choices=choices_deficiencia)