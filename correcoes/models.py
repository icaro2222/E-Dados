from django.db import models

class Correcao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    email = models.EmailField()
