from django import forms
from edados.formularios.base import questionario_ano, questionario_provas, questionario_prova_cores_2017,  questionario_prova_cores_2018,  questionario_prova_cores_2019, questionario_acerto_erro


class Formulario_3(forms.Form):
    
    # prova = questionario_prova.questionario_prova(Form=forms.Form)
    cor_da_prova_2019 = questionario_prova_cores_2019.questionario_prova(Form=forms.Form)
    cor_da_prova_2018 = questionario_prova_cores_2018.questionario_prova(Form=forms.Form)
    cor_da_prova_2017 = questionario_prova_cores_2017.questionario_prova(Form=forms.Form)
    acerto_erro = questionario_acerto_erro.questionario_acerto_erro(Form=forms.Form)
    ano = questionario_ano.questionario_ano(Form=forms.Form)



class Formulario_3_2(forms.Form):
    
    # prova = questionario_prova.questionario_prova(Form=forms.Form)
    # ciencia_humana = questionario_provas.questionario_prova_ciencia_humana(Form=forms.Form)
    prova1 = questionario_prova_cores_2019.questionario_prova(Form=forms.Form)
    prova2 = questionario_prova_cores_2019.questionario_prova(Form=forms.Form)
    prova3 = questionario_prova_cores_2019.questionario_prova_nenhuma(Form=forms.Form)
    prova4 = questionario_prova_cores_2019.questionario_prova_nenhuma(Form=forms.Form)
    
    prova1_2018 = questionario_prova_cores_2018.questionario_prova(Form=forms.Form)
    prova2_2018 = questionario_prova_cores_2018.questionario_prova(Form=forms.Form)
    prova3_2018 = questionario_prova_cores_2018.questionario_prova_nenhuma(Form=forms.Form)
    prova4_2018 = questionario_prova_cores_2018.questionario_prova_nenhuma(Form=forms.Form)
    
    prova1_2017 = questionario_prova_cores_2017.questionario_prova(Form=forms.Form)
    prova2_2017 = questionario_prova_cores_2017.questionario_prova(Form=forms.Form)
    prova3_2017 = questionario_prova_cores_2017.questionario_prova_nenhuma(Form=forms.Form)
    prova4_2017 = questionario_prova_cores_2017.questionario_prova_nenhuma(Form=forms.Form)
    
    questao1 = questionario_prova_cores_2019.questionario_questao(Form=forms.Form)
    questao2 = questionario_prova_cores_2019.questionario_questao(Form=forms.Form)
    questao3 = questionario_prova_cores_2019.questionario_questao_nenhuma(Form=forms.Form)
    questao4 = questionario_prova_cores_2019.questionario_questao_nenhuma(Form=forms.Form)
    
    questao1_2018 = questionario_prova_cores_2018.questionario_questao(Form=forms.Form)
    questao2_2018 = questionario_prova_cores_2018.questionario_questao(Form=forms.Form)
    questao3_2018 = questionario_prova_cores_2018.questionario_questao_nenhuma(Form=forms.Form)
    questao4_2018 = questionario_prova_cores_2018.questionario_questao_nenhuma(Form=forms.Form)
    
    questao1_2017 = questionario_prova_cores_2017.questionario_questao(Form=forms.Form)
    questao2_2017 = questionario_prova_cores_2017.questionario_questao(Form=forms.Form)
    questao3_2017 = questionario_prova_cores_2017.questionario_questao_nenhuma(Form=forms.Form)
    questao4_2017 = questionario_prova_cores_2017.questionario_questao_nenhuma(Form=forms.Form)
    
    acerto_erro = questionario_acerto_erro.questionario_acerto_erro(Form=forms.Form)
    ano = questionario_ano.questionario_ano(Form=forms.Form)

