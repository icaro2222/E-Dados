from random import choices
from django import forms

def questionario_amostra(Form):

    choices_amostra = (
                    # (' LIMIT 0' ,'Teste-Bugs - 0 registros'),
                    # (' LIMIT 1000' ,'Teste - 1.000 registros'),
                    ('a_5_90' ,'Aleatoria simples, 5% marge de Erro e 90% Confiabilidade'),
                    ('a_3_95' ,'Aleatoria simples, 3% marge de Erro e 95% Confiabilidade'),
                    ('a_1_99' ,'Aleatoria simples, 1% marge de Erro e 99% Confiabilidade'),
                    ('todos_os_dados', 'Todos os dados'))

    amostra = forms.ChoiceField(
        label="""<div class="m-0" title="A amostra é uma técnica utilizada para selecionar uma parte dos dados, visando obter resultados com boa precisão, ou seja, sem uma perda significativa na análise. É possível escolher diferentes quantidades de dados, tais como uma amostra com margem de erro de 3% e confiança de 90%, uma amostra com margem de erro de 5% e confiança de 95%, uma amostra com margem de erro de 1% e confiança de 99%, ou utilizar todos os dados disponíveis.">Método de Amostragem: <i class="fas fa-info-circle text-danger"></i></div>""", 
        choices=choices_amostra,
        initial='a_1_99',
        required=False,
        widget=forms.Select(attrs={
            'title': """A amostra aleatória simples, com uma margem de erro de 5% e uma confiabilidade de 90%, traz resultados satisfatórios em grande parte dos casos. No entanto, para análises mais precisas, é recomendada a amostra aleatória simples com uma margem de erro de 3% e uma confiabilidade de 95%. Além disso, também é possível utilizar uma amostra aleatória simples com uma margem de erro de 1% e uma confiabilidade de 99%, ou utilizar todos os dados disponíveis, para obter resultados ainda mais precisos."""
        }))
    
    return amostra