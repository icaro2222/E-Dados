from random import choices
from django import forms

def questionario_prova(Form):

    choices_prova= (('CO_PROVA_CN', 'Prova de Ciências da Natureza'),
                    ('CO_PROVA_CH' ,'Prova de Ciências Humanas'),
                    ('CO_PROVA_LC' ,'Prova de Linguagens e Códigos'),
                    ('CO_PROVA_MT' ,'Prova de Matemática'))

    prova = forms.ChoiceField(label='Prova:', choices=choices_prova)
    return prova










