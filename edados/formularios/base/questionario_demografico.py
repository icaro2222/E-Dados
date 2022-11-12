from random import choices
from django import forms

def questionario_demografico(Form):

    choices_questao = ( ('TP_SEXO' ,'Sexo'),
                        ('TP_ESTADO_CIVIL', 'Estado Civil'),
                        ('TP_COR_RACA', 'Cor / Raça'),
                        ('TP_NACIONALIDADE', 'Nacionalidade'),
                        ('TP_ST_CONCLUSAO', 'Situação de conclusão do Ensino Médio'),
                        ('TP_ANO_CONCLUIU', 'Ano de Conclusão do Ensino Médio'),
                        ('TP_ESCOLA', 'Tipo de escola do Ensino Médio'),
                        ('TP_ENSINO', 'Tipo de instituição que concluiu ou concluirá o Ensino Médio '),
                        ('IN_TREINEIRO', 'Indica se o inscrito fez a prova com intuito de apenas treinar seus conhecimentos'))
            
    questao = forms.ChoiceField(label='Demográcifo', choices=choices_questao)
    return questao