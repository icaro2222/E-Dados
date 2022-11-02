from random import choices
from django import forms
from edados.formularios import questionario_socioeconomico


class MeuFormulario(forms.Form):
            
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


    questao = questionario_socioeconomico.questionario_socioeconomico(Form=forms.Form)
    nota = forms.ChoiceField(choices=choices_nota)
    sexo = forms.ChoiceField(choices=choices_sexo)