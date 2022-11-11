from random import choices
from django import forms

def questionario_ano(Form):

    choices_ano = (('todos' ,'Todos'),    
                    ('2019', '2019'),
                    ('2018' ,'2018'),
                    ('2017' ,'2017'),
                    ('2016' ,'2016'))

    ano = forms.ChoiceField(label='Ano:', choices=choices_ano)
    return ano