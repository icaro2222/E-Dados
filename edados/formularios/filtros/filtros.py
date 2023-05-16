from random import choices
from django import forms
from edados.formularios.base import questionario_ano, questionario_sexo


class Formulario_filtros(forms.Form):

    sexo = questionario_sexo.questionario_sexo(Form=forms.Form)
    ano = questionario_ano.questionario_ano(Form=forms.Form)