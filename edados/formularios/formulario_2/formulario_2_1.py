from django import forms
from edados.formularios.base import questionario_socioeconomico, questionario_ano


class Formulario(forms.Form):

    # ano = questionario_ano.questionario_ano(Form=forms.Form)
    questao = questionario_socioeconomico.questionario_socioeconomico(Form=forms.Form)
    ano = questionario_ano.questionario_ano(Form=forms.Form)

