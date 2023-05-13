from random import choices
from django import forms

def questionario_tipo_de_escola(Form):

    choices_escola=(('vazio', 'TODOS'),
                    ('1', 'Federal'),
                    ('2', 'Estadual'),
                    ('3', 'Municipal'),
                    ('4', 'Privada'))

    adm_escola = forms.ChoiceField(label='Dependência administrativa (Escola):', choices=choices_escola)
    return adm_escola
