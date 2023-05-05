from random import choices
from django import forms

def questionario_localizacao(Form):
    
    choices_localizacao = (('urbana', 'Urbana'),
                           ('rural', 'Rural'))

    localizacao = forms.ChoiceField(label='Localização (Escola):', choices=choices_localizacao)
    return localizacao
