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
            
    choices_nota = (('NU_NOTA_MT' ,'Nota em Matemática'),    
                    ('NU_NOTA_CH', 'Nota em Ciências da Natureza'),
                    ('NU_NOTA_CN' ,'Nota em Ciências Humanas'),
                    ('NU_NOTA_LC', 'Nota da prova de Linguagens e Códigos'),
                    ('NU_NOTA_COMP1', 'Nota da competência 1'),
                    ('NU_NOTA_COMP2', 'Nota da competência 2'),
                    ('NU_NOTA_COMP3', 'Nota da competência 3'),
                    ('NU_NOTA_REDACAO', 'Nota da prova de redação'))
                    
    choices_sexo = (('ambos' ,'Ambos'),    
                    ('f', 'Filtrar Apenas Femilino'),
                    ('m' ,'Filtrar Apenas Masculino'))


    questao = forms.ChoiceField(choices=choices_questao)
    nota = forms.ChoiceField(choices=choices_nota)
    sexo = forms.ChoiceField(choices=choices_sexo)