from django.db import models

# Create your models here.

class estado(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)
    

    def __str__(self):
        return f"{self.nome} ({self.sigla})"
    
class cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(estado, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.nome} ({self.estado.sigla})"

class pessoa(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField(max_length=100)
    cidade = models.ForeignKey('cidade', on_delete=models.PROTECT)
    def __str__(self):
        return f"{self.nome} ({self.data_nascimento})"