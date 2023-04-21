from random import choices
from django import forms
from edados.formularios.base import questionario_ano

class Formulario_filtro_ano(forms.Form):

    ano = questionario_ano.questionario_ano(Form=forms.Form)