from random import choices
from django import forms


class DashboardFormulario(forms.Form):

    choices_ano = (('todos' ,'TODOS'),    
                    ('2019', '2019'),
                    ('2018' ,'2018'),
                    ('2017' ,'2017'),
                    ('2016' ,'2016'))

    ano = forms.ChoiceField(choices=choices_ano)