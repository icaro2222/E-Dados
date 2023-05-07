from random import choices
from django import forms

# DADOS DOS PEDIDOS DE ATENDIMENTO ESPECIALIZADO
def questionario_de_deficiencia(Form):

    choices_deficiencia = (
        ('todos', 'Todos inscritos do enem'),
        ('nenhuma', 'Apenas inscritos que não possuem deficiência'),
        ('todas', 'Apenas inscritos que possuem deficiência'),
        ('IN_BAIXA_VISAO', 'baixa visão'),
        ('IN_CEGUEIRA', 'cegueira'),
        ('IN_SURDEZ', 'surdez'),
        ('IN_DEFICIENCIA_AUDITIVA', 'deficiência auditiva'),
        ('IN_SURDO_CEGUEIRA', 'surdo-cegueira'),
        ('IN_DEFICIENCIA_FISICA', 'deficiência física'),
        ('IN_DEFICIENCIA_MENTAL', 'deficiência mental'),
        ('IN_DEFICIT_ATENCAO', 'déficit de atenção'),
        ('IN_DISLEXIA', 'dislexia'),
        ('IN_DISCALCULIA', 'discalculia'),
        ('IN_AUTISMO', 'autismo'),
        ('IN_VISAO_MONOCULAR', 'visão monocular'),
        ('IN_OUTRA_DEF', 'outra deficiência ou condição especial'))


    deficiencia = forms.ChoiceField(label='Tipo de deficiência:' , choices=choices_deficiencia)
    
    return deficiencia
