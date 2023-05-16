from django import forms
from edados.formularios import questionario_socioeconomico
from edados.formularios.base import questionario_demografico



class MeuFormulario(forms.Form):

    questionario_socioeconomico = questionario_socioeconomico.questionario_socioeconomico(Form=forms.Form)
    questionario_demografico = questionario_demografico.questionario_demografico(Form=forms.Form)
    