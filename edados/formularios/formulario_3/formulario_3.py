from django import forms
from edados.formularios.base import questionario_de_deficiencia, questionario_prova, questionario_prova_cores


class Formulario_3(forms.Form):

    # ano = questionario_ano.questionario_ano(Form=forms.Form)
    questao = questionario_prova.questionario_prova(Form=forms.Form)
    prova_cor = questionario_prova_cores.questionario_prova(Form=forms.Form)
    deficiencia = questionario_de_deficiencia.questionario_de_deficiencia(Form=forms.Form)


