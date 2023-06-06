from django import forms
from edados.formularios.base import questionario_ano, questionario_prova_cores_2017,  questionario_prova_cores_2018,  questionario_prova_cores_2019, questionario_acerto_erro


class Formulario_3(forms.Form):
    
    # prova = questionario_prova.questionario_prova(Form=forms.Form)
    cor_da_prova_2019 = questionario_prova_cores_2019.questionario_prova(Form=forms.Form)
    cor_da_prova_2018 = questionario_prova_cores_2018.questionario_prova(Form=forms.Form)
    cor_da_prova_2017 = questionario_prova_cores_2017.questionario_prova(Form=forms.Form)
    acerto_erro = questionario_acerto_erro.questionario_acerto_erro(Form=forms.Form)
    ano = questionario_ano.questionario_ano(Form=forms.Form)

