from random import choices
from django import forms

# DADOS DOS PEDIDOS DE ATENDIMENTO ESPECIALIZADO
def questionario_de_escola(Form):

    choices_escola = (('todos', 'TODOS'),
        ('1', 'Não Respondeu'),
        ('2', 'Pública'),
        ('3', 'Privada'),
        ('4', 'Exterior'))

    escola = forms.ChoiceField(label='Tipo de escola do Ensino Médio:' , choices=choices_escola, required=False)
    
    return escola