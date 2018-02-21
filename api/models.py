from django.db import models


class Recurso(models.Model):
    chapa = models.CharField(max_length=18)
    nome = models.CharField(max_length=50)
    funcao = models.CharField(max_length=50)
    inicio = models.CharField(max_length=10)
    fim = models.CharField(max_length=10)
    data_json = models.CharField(max_length=10)

    def __str__(self):
        return self.nome