from random import choices
from django import forms

def questionario_sexo(Form):

    choices_sexo = (('ambos' ,'Ambos'),    
                    ('F', 'Femilino'),
                    ('M' ,'Masculino'))

    sexo = forms.ChoiceField(label='Sexo:', choices=choices_sexo)
    return sexo