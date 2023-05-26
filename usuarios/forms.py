from django import forms

class LoginForm(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    cpf = forms.CharField(max_length=15)
    cep = forms.CharField(max_length=10)
    numero = forms.CharField(max_length=5)
    descricao = forms.CharField(
    label='Descrição sobre o usuário:', 
    widget=forms.Textarea(attrs={'rows': 4}))
    cidade = forms.CharField(max_length=20)
    estado = forms.CharField(max_length=20)