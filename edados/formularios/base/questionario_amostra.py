from random import choices
from django import forms

def questionario_amostra(Form):

    choices_amostra = (
                    (' LIMIT 0' ,'Teste-Bugs - 0 registros'),
                    (' LIMIT 1000' ,'Teste - 1.000 registros'),
                    ('a_5_90' ,'Aleatoria simples, 5% marge de Erro e 90% Confiabilidade'),
                    ('a_3_95' ,'Aleatoria simples, 3% marge de Erro e 95% Confiabilidade'),
                    ('a_1_99' ,'Aleatoria simples, 1% marge de Erro e 99% Confiabilidade'),
                    ('todos_os_dados', 'Todos os dados'))

    amostra = forms.ChoiceField(
        label="""<div class="m-0" title="Amostra é uma técnica utilizada para selecionar uma parte dos dados de forma a obter resultados com uma boa precisão, ou seja, sem uma perda significativa na análise. É possível selecionar diferentes quantidades de dados, como por exemplo, uma semi-amostra com 20.000 registros, uma amostra com 30.000 registros, ou utilizar todos os dados disponíveis.">Meétodo de Amostragem: <i class="fas fa-info-circle text-danger"></i></div>""", 
        choices=choices_amostra,
        required=False,
        widget=forms.Select(attrs={
            'title': """A semi-amostra com 20.000 registros traz resultados satisfatórios em grande parte dos casos. Para análises mais precisas, recomenda-se a amostra com 30.000 registros, ou a utilização de todos os dados disponíveis com 99% de precisão."""
        }))
    
    return amostra