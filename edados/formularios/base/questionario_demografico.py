from random import choices
from django import forms

def questionario_demografico(Form):

    choices_questao = ( ('TP_SEXO' ,'Sexo'),
                        ('TP_ESTADO_CIVIL', 'Estado Civil'),
                        ('TP_COR_RACA', 'Cor / Raça'),
                        ('TP_NACIONALIDADE', 'Nacionalidade'),
                        # ('TP_ST_CONCLUSAO', 'Situação de conclusão do Ensino Médio'),
                        ('TP_ANO_CONCLUIU', 'Ano de Conclusão do Ensino Médio'),
                        ('TP_ESCOLA', 'Tipo de escola do Ensino Médio'),
                        ('TP_ENSINO', 'Tipo de instituição que concluiu ou concluirá o Ensino Médio '),
                        # ('IN_TREINEIRO', 'Indica se o inscrito fez a prova com intuito de apenas treinar seus conhecimentos')
                        )
            
    questao = forms.ChoiceField(
        label="""<div class="m-0" title="Esta opção permite selecionar uma variável demográfica que será contrastada com a questão socioeconômica, a fim de criar um gráfico comparativo entre essas duas variáveis. Isso possibilita a análise da relação entre características demográficas dos participantes (como sexo, estado civil, cor/raça, nacionalidade, etc.) e as respostas socioeconômicas. O gráfico resultante oferece insights sobre possíveis padrões ou correlações entre essas variáveis, contribuindo para uma compreensão mais completa do perfil dos participantes.">Demográfico: <i class="fas fa-info-circle"></i></div>""", 
        choices=choices_questao,
        required=False,
        widget=forms.Select(attrs={
            'title': """Sexo: Essa opção permite que você analise a distribuição dos inscritos por gênero. Um gráfico com essa opção poderia mostrar a proporção de participantes do sexo masculino e feminino.

Estado Civil: Essa opção permite que você entenda a distribuição dos inscritos em diferentes estados civis, como solteiro, casado, divorciado, etc. Um gráfico com essa opção poderia mostrar a quantidade de participantes em cada estado civil.

Cor / Raça: Essa opção permite que você visualize a autodeclaração dos participantes em relação à cor ou raça. Um gráfico com essa opção poderia mostrar a proporção de participantes em cada categoria racial.

Nacionalidade: Essa opção permite que você identifique a proporção de inscritos brasileiros e estrangeiros. Um gráfico com essa opção poderia mostrar a distribuição dos participantes por nacionalidade.

Ano de Conclusão do Ensino Médio: Essa opção permite que você veja em qual ano os participantes concluíram o Ensino Médio. Um gráfico com essa opção poderia mostrar a distribuição dos inscritos ao longo dos anos.

Tipo de escola do Ensino Médio: Essa opção permite que você saiba em que tipo de escola os participantes estudaram durante o Ensino Médio, como escola pública ou escola privada. Um gráfico com essa opção poderia mostrar a proporção de participantes em cada tipo de escola.

Tipo de instituição que concluiu ou concluirá o Ensino Médio: Essa opção permite que você identifique o tipo de instituição em que os participantes concluíram ou concluirão o Ensino Médio, como escola regular, Educação de Jovens e Adultos (EJA) ou outro tipo. Um gráfico com essa opção poderia mostrar a distribuição dos inscritos nas diferentes categorias de instituição."""
        }))
    
    # questao = forms.ChoiceField(label='Demográfico', choices=choices_questao)
    return questao