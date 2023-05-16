from random import choices
from django import forms

def questionario_prova(Form):

    choices_prova= (('CO_PROVA_CN', 'CO_PROVA_CN - Ciências da Natureza'),
                    ('CO_PROVA_CH' ,'CO_PROVA_CH - Ciências Humanas'),
                    ('CO_PROVA_LC' ,'CO_PROVA_LC - Linguagens e Códigos'),
                    ('CO_PROVA_MT' ,'CO_PROVA_MT - Matemática'))

    # prova = forms.ChoiceField(label='Prova:', choices=choices_prova)
    
    prova = forms.ChoiceField(
        label="""<div class="m-0" title="PROVAS / Áreas do conhecimento">Prova:<i class="fas fa-info-circle"></i></div>""", 
        choices=choices_prova,
        required=False,
        widget=forms.Select(attrs={
            'title': """Análise das provas/ Áreas do conhecimento."""
        }))
    
    return prova










