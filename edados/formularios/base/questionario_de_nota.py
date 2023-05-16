from random import choices
from django import forms


def questionario_de_nota(Form):

    choices_nota = (('NU_NOTA_MT' ,'NU_NOTA_MT - Matemática'),    
                    ('NU_NOTA_CH', 'NU_NOTA_CH - Ciências da Natureza'),
                    ('NU_NOTA_CN' ,'NU_NOTA_CN - Ciências Humanas'),
                    ('NU_NOTA_LC', 'NU_NOTA_LC - Linguagens e Códigos'),
                    ('NU_NOTA_COMP1', 'NU_NOTA_COMP1 - Nota da competência 1'),
                    ('NU_NOTA_COMP2', 'NU_NOTA_COMP2 - Nota da competência 2'),
                    ('NU_NOTA_COMP3', 'NU_NOTA_COMP3 - Nota da competência 3'),
                    ('NU_NOTA_COMP4', 'NU_NOTA_COMP4 - Nota da competência 4'),
                    ('NU_NOTA_COMP5', 'NU_NOTA_COMP5 - Nota da competência 5'),
                    ('NU_NOTA_REDACAO', 'NU_NOTA_REDACAO - Redação'))
                    

    
    nota = forms.ChoiceField(
        label="""<div class="m-0" title="Essa opção permite selecionar a prova que você deseja analisar e, em seguida, gera gráficos e informações que mostram a correlação entre a nota na prova e as questões socioeconômicas. Isso possibilita identificar os principais fatores socioeconômicos que influenciam o desempenho dos candidatos nas provas. Além disso, é possível identificar em qual prova os candidatos têm um desempenho melhor ou pior, relacionado às questões socioeconômicas. Essa análise ajuda a compreender como os fatores socioeconômicos impactam os resultados das provas, permitindo direcionar esforços para melhorar a equidade e a qualidade da educação.">Prova: <i class="fas fa-info-circle"></i></div>""", 
        choices=choices_nota,
        required=False,
        widget=forms.Select(attrs={
            'title': """Análise das provas/ Áreas do conhecimento."""
        }))
    return nota