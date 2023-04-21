from django import forms
from edados.formularios.base import questionario_socioeconomico_mult, questionario_ano, questionario_de_deficiencia, questionario_demografico


class Formulario_1(forms.Form):

    # ano = questionario_ano.questionario_ano(Form=forms.Form)
    questao = questionario_socioeconomico_mult.questionario_socioeconomico(Form=forms.Form)
    ano = questionario_ano.questionario_ano(Form=forms.Form)


