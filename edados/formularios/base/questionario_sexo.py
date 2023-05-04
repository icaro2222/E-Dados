from random import choices
from django import forms

def questionario_sexo(Form):

    choices_sexo = (('todos' ,'Ambos'),    
                    ('F', 'Feminino'),
                    ('M' ,'Masculino'))

    sexo = forms.ChoiceField(label='Sexo:', choices=choices_sexo)
    return sexo