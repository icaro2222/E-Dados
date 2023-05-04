from random import choices
from django import forms

def questionario_acerto_erro(Form):

    choices_acerto_erro= (('acertos', 'Acertos'),
                    ('erros' ,'Erros'))

    acerto_erro = forms.ChoiceField(label='Analisar:', choices=choices_acerto_erro)
    return acerto_erro










