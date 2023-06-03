from django.db import models

# Criando modelo do Usuário

class Usuario(models.Model):
    id_usuario = models.CharField( max_length=5)
    nome = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=30, null=True)
    cpf = models.CharField(max_length=15, null=True)
    cep = models.CharField(max_length=10, null=True)
    descricao = models.CharField(max_length=200, null=True)
    numero = models.CharField(max_length=5, null=True)
    cidade = models.CharField(max_length=20, null=True)
    estado = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.nome