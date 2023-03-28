from random import choices
from django import forms
from edados.formularios.base import questionario_ano, questionario_de_deficiencia


class DashboardFormulario(forms.Form):

    ano = questionario_ano.questionario_ano(Form=forms.Form)
    deficiencia = questionario_de_deficiencia.questionario_de_deficiencia(Form=forms.Form)