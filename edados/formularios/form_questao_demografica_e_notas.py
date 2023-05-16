from django import forms
from edados.formularios.base import questionario_demografico



class MeuFormulario(forms.Form):

    choices_nota = (('NU_NOTA_MT' ,'NU_NOTA_MT - Matemática'),    
                    ('NU_NOTA_CH', 'NU_NOTA_CH - Ciências da Natureza'),
                    ('NU_NOTA_CN' ,'NU_NOTA_CN - Ciências Humanas'),
                    ('NU_NOTA_LC', 'NU_NOTA_LC - Linguagens e Códigos'),
                    ('NU_NOTA_COMP1', 'NU_NOTA_COMP1 - Nota da competência 1'),
                    ('NU_NOTA_COMP2', 'NU_NOTA_COMP2 - Nota da competência 2'),
                    ('NU_NOTA_COMP3', 'NU_NOTA_COMP3 - Nota da competência 3'),
                    ('NU_NOTA_COMP4', 'NU_NOTA_COMP4 - Nota da competência 4'),
                    ('NU_NOTA_COMP5', 'NU_NOTA_COMP5 - Nota da competência 5'),
                    ('NU_NOTA_REDACAO', 'NU_NOTA_REDACAO - Redação'))
                    

    questao = questionario_demografico.questionario_demografico(Form=forms.Form)
    nota = forms.ChoiceField(choices=choices_nota)