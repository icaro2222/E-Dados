from random import choices
from django import forms
from edados.formularios.base import questionario_socioeconomico, questionario_de_deficiencia, questionario_ano, questionario_de_nota, questionario_sexo


class Formulario_filtros(forms.Form):

    sexo = questionario_sexo.questionario_sexo(Form=forms.Form)