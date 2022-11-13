from django import forms
from edados.formularios.base import questionario_de_deficiencia, questionario_prova, questionario_prova_cores


class Formulario_3(forms.Form):
    
    prova = questionario_prova.questionario_prova(Form=forms.Form)
    cor_da_prova = questionario_prova_cores.questionario_prova(Form=forms.Form)
    deficiencia = questionario_de_deficiencia.questionario_de_deficiencia(Form=forms.Form)


