from django.db import models

# Criando modelo do Usuário

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    cpf = models.CharField(max_length=15)
    cep = models.CharField(max_length=10)
    numero = models.CharField(max_length=5)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return self.nome