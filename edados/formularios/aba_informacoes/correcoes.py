from django import forms

class form_correcoes(forms.Form):
    
    nome = forms.CharField(label='Nome:', max_length=100)
    senha = forms.CharField(label='Senha:', max_length=100)
    descricao = forms.CharField(
    label='Descrição sobre o usuário:', 
    widget=forms.Textarea(attrs={'rows': 4}))
    email = forms.CharField(label='E-mail:', max_length=100)

