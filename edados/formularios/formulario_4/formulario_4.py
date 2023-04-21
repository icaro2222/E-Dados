from django import forms
from edados.formularios.base import questionario_de_deficiencia, questionario_prova, questionario_prova_cores, questionario_acerto_erro


class Formulario_4(forms.Form):
    
    # prova = questionario_prova.questionario_prova(Form=forms.Form)
    cor_da_prova = questionario_prova_cores.questionario_prova(Form=forms.Form)
    deficiencia = questionario_de_deficiencia.questionario_de_deficiencia(Form=forms.Form)
    acerto_erro = questionario_acerto_erro.questionario_acerto_erro(Form=forms.Form)


