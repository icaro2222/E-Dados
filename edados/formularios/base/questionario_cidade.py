from random import choices
from django import forms


def questionario_cidade(Form):

    choices_cidade = (('todos', 'Todos'),    )
    
    cidade=forms.ChoiceField(
        label="Cidade:", choices=choices_cidade, required=False)
    return cidade