from random import choices
from django import forms

# DADOS DOS PEDIDOS DE ATENDIMENTO ESPECIALIZADO
def questionario_de_escola(Form):

    choices_escola = (('todos', 'TODOS'),
        ('0', 'Não Respondeu'),
        ('1', 'Pública'),
        ('2', 'Privada'),
        ('3', 'Exterior'))

    escola = forms.ChoiceField(label='Tipo de escola do Ensino Médio:' , choices=choices_escola)
    
    return escola