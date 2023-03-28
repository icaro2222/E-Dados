from django import forms
from edados.formularios import questionario_socioeconomico



class MeuFormulario(forms.Form):

    choices_nota = (('NU_NOTA_MT' ,'Nota em Matemática'),    
                    ('NU_NOTA_CH', 'Nota em Ciências da Natureza'),
                    ('NU_NOTA_CN' ,'Nota em Ciências Humanas'),
                    ('NU_NOTA_LC', 'Nota da prova de Linguagens e Códigos'),
                    ('NU_NOTA_COMP1', 'Nota da competência 1'),
                    ('NU_NOTA_COMP2', 'Nota da competência 2'),
                    ('NU_NOTA_COMP3', 'Nota da competência 3'),
                    ('NU_NOTA_REDACAO', 'Nota da prova de redação'))
                    
    # Formulario para os inscritos que se declararam com algum tipo de deficiência
    Questao_Socioeconomica_Com_Deficiencia = questionario_socioeconomico.questionario_socioeconomico(Form=forms.Form)
    Nota_da_prova_Com_Deficiencia = forms.ChoiceField(choices=choices_nota)

    # Formulario para os inscritos que declararam possuir nenhuma  deficiência
    Questao_Socioeconomica_Sem_Deficiencia = questionario_socioeconomico.questionario_socioeconomico(Form=forms.Form)
    Nota_da_prova_Sem_Deficiencia = forms.ChoiceField(choices=choices_nota)