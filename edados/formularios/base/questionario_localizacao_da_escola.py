from random import choices
from django import forms

def questionario_localizacao(Form):
    
    choices_localizacao = (('todos', 'Todas'),
                           ('null', 'Não informou'),
                           ('1', 'Urbana'),
                           ('2', 'Rural'))

    localizacao = forms.ChoiceField(label='Localização (Escola):', choices=choices_localizacao, required=False)
    return localizacao
