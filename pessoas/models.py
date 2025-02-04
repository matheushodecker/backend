from django.db import models

# Create your models here.
class pessoa(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nome} ({self.data_nascimento})"