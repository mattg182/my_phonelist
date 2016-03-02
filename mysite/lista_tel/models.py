from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length = 30)
    telefone = models.IntegerField()
    e_mail = models.CharField(max_length = 30)
