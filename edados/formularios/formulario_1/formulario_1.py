from django import forms
from edados.formularios.base import questionario_socioeconomico, questionario_de_deficiencia, questionario_demografico


class Formulario_1(forms.Form):

    # ano = questionario_ano.questionario_ano(Form=forms.Form)
    questao = questionario_socioeconomico.questionario_socioeconomico(Form=forms.Form)
    demografico = questionario_demografico.questionario_demografico(Form=forms.Form)
    deficiencia = questionario_de_deficiencia.questionario_de_deficiencia(Form=forms.Form)


