from random import choices
from django import forms
from edados.formularios.base import questionario_estado, questionario_de_nacionalidade,questionario_sexo, questionario_de_escola, questionario_cor, questionario_estado_civil, questionario_de_deficiencia


class Formulario_filtros(forms.Form):

    sexo = questionario_sexo.questionario_sexo(Form=forms.Form)
    cor = questionario_cor.questionario_cor(Form=forms.Form)
    estado_civil = questionario_estado_civil.questionario_estado_civil(Form=forms.Form)
    deficiencia = questionario_de_deficiencia.questionario_de_deficiencia(Form=forms.Form)
    escola = questionario_de_escola.questionario_de_escola(Form=forms.Form)
    nacionalidade = questionario_de_nacionalidade.questionario_de_nacionalidade(Form=forms.Form)
    
    # esta função de estado ainda não está implementada
    estado_estado = questionario_estado.questionario_estado(Form=forms.Form)