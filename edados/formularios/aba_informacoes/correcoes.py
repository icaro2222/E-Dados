from django import forms

class form_correcoes(forms.Form):
    
    nome = forms.CharField(label='Seu nome:', max_length=100)
    descricao = forms.CharField(
    label='Descrição do Bug / Erro:', 
    widget=forms.Textarea(attrs={'rows': 4}))
    email = forms.CharField(label='Seu e-mail:', max_length=100)

