from django import forms
from edados.formularios.base import questionario_socioeconomico_nenhum, questionario_demografico, questionario_ano


class Formulario_1(forms.Form):

    # ano = questionario_ano.questionario_ano(Form=forms.Form)
    questao = questionario_socioeconomico_nenhum.questionario_socioeconomico(Form=forms.Form)
    demografico = questionario_demografico.questionario_demografico(Form=forms.Form)
    ano = questionario_ano.questionario_ano(Form=forms.Form)


