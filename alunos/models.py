from django.db import models

# Create your models here.

class estado(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)
    

    def __str__(self):
        return f"{self.nome} ({self.sigla})"