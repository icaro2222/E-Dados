from django import forms
from edados.formularios.base import questionario_socioeconomico_nenhum, questionario_de_deficiencia, questionario_ano, questionario_de_nota, questionario_sexo


class Formulario_2(forms.Form):

    # ano = questionario_ano.questionario_ano(Form=forms.Form)
    questao = questionario_socioeconomico_nenhum.questionario_socioeconomico(Form=forms.Form)
    nota = questionario_de_nota.questionario_de_nota(Form=forms.Form)
    deficiencia = questionario_de_deficiencia.questionario_de_deficiencia(Form=forms.Form)
    ano = questionario_ano.questionario_ano(Form=forms.Form)


