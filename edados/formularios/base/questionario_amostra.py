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
        label="""<div class="m-0" title="A amostragem aleatória simples é um método utilizado para selecionar uma parte dos dados de maneira aleatória, visando obter resultados com boa precisão, sem causar uma perda significativa na análise. É possível trabalhar com diferentes volumes de dados, os quais variam de acordo com o nível de margem de erro e confiabilidade desejados. Por exemplo, pode-se optar por uma amostra com margem de erro de 3% e confiança de 90%, uma amostra com margem de erro de 5% e confiança de 95%, uma amostra com margem de erro de 1% e confiança de 99%, ou até mesmo utilizar todos os dados disponíveis. A escolha da amostra adequada dependerá das necessidades específicas da análise em questão. É importante ressaltar que a precisão dos resultados pode variar de acordo com a técnica de amostragem utilizada, sendo fundamental considerar a margem de erro e a confiabilidade desejada para obter conclusões mais robustas.">Método de Amostragem: <i class="fas fa-info-circle text-danger"></i></div>""", 
        choices=choices_amostra,
        initial='a_1_99',
        required=False,
        widget=forms.Select(attrs={
            'title': """Ao utilizar o método de amostragem aleatória simples com uma margem de erro de 5% e uma confiabilidade de 90%, em muitos casos os resultados são satisfatórios. No entanto, quando é necessário realizar análises mais precisas, é recomendável optar por amostras com margem de erro menor e maior nível de confiabilidade. Por exemplo, utilizar uma amostra aleatória simples com margem de erro de 3% e confiabilidade de 95%, ou até mesmo uma amostra com margem de erro de 1% e confiabilidade de 99%. Alternativamente, pode-se considerar o uso de todos os dados disponíveis, o que proporciona resultados ainda mais precisos."""
        }))
    
    return amostra