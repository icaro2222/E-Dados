from django import forms
from edados.formularios.base import questionario_ano, questionario_questao

class Formulario_4(forms.Form):
    
    questao = questionario_questao.questionario_questao(Form=forms.Form)
    ano = questionario_ano.questionario_ano(Form=forms.Form)
