from django import forms
from edados.formularios import questionario_demografico, questionario_socioeconomico



class MeuFormulario(forms.Form):

    questionario_socioeconomico = questionario_socioeconomico.questionario_socioeconomico(Form=forms.Form)
    questionario_demografico = questionario_demografico.questionario_demografico(Form=forms.Form)
    