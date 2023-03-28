from random import choices
from django import forms

# DADOS DOS PEDIDOS DE ATENDIMENTO ESPECIALIZADO
def questionario_de_nacionalidade(Form):

    choices_nacionalidade = (('todos', 'TODOS'),
        ('0', 'Não informado'),
        ('1', 'Brasileiro(a)'),
        ('2', 'Brasileiro(a) Naturalizado(a)'),
        ('3', 'Estrangeiro(a)'),
        ('4', 'Brasileiro(a) Nato(a), nascido(a) no exterior'))

    nacionalidade = forms.ChoiceField(label='Nacionalidade:' , choices=choices_nacionalidade)
    
    return nacionalidade