from random import choices
from django import forms

def questionario_amostra(Form):

    choices_amostra = (
                    (' LIMIT 1000' ,'Teste - 1.000 registros'),
                    (' LIMIT 20000' ,'Semi-Amostra - 20.000 registros'),
                    (' LIMIT 30000' ,'Amostra - 30.000 registros'),
                    ('            ', 'Todos os dados'))

    amostra = forms.ChoiceField(
        label="""<div class="m-0" title="Amostra é uma técnica utilizada para selecionar uma parte dos dados de forma a obter resultados com uma boa precisão, ou seja, sem uma perda significativa na análise. É possível selecionar diferentes quantidades de dados, como por exemplo, uma amostra apenas para teste com 1.000 registros, uma semi-amostra com 20.000 registros, uma amostra com 30.000 registros, ou utilizar todos os dados disponíveis.">Amostra:* <i class="fas fa-info-circle text-danger"></i></div>""", 
        choices=choices_amostra,
        required=False,
        widget=forms.Select(attrs={
            'title': """1.000 registros é ideal apenas para testes preliminares. Já a semi-amostra com 20.000 registros traz resultados satisfatórios em grande parte dos casos. Para análises mais precisas, recomenda-se a amostra com 30.000 registros, ou a utilização de todos os dados disponíveis com 99% de precisão."""
        }))
    
    return amostra