from random import choices
from django import forms

def questionario_cor(Form):

    choices_cor = (('todos', 'TODOS'),
                    ('0', 'Não declarado'),
                    ('1' ,'Branca'),
                    ('2' ,'Preta'),
                    ('3' ,'Parda'),
                    ('4' ,'Amarela'),
                    ('5' ,'Indígena'))

    cor = forms.ChoiceField(label='cor:', choices=choices_cor)
    return cor