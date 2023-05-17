from random import choices
from django import forms

def questionario_ano_de_conclusao(Form):

    choices_ano = (('vazio', 'TODOS'),
                ('0', 'Não informado'),
                ('1', '2018'),
                ('2', '2017'),
                ('3', '2016'),
                ('4', '2015'),
                ('5', '2014'),
                ('6', '2013'),
                ('7', '2012'),
                ('8', '2011'),
                ('9', '2010'),
                ('10', '2009'),
                ('11', '2008'),
                ('12', '2007'),
                ('13', 'Antes de 2007'))

    ano_de_conclusao = forms.ChoiceField(label='Ano de Conclusão do Ensino Médio:', choices=choices_ano, required=False)
    return ano_de_conclusao


