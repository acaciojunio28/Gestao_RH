from django.db import models
from audioop import reverse

class Empresa(models.Model):
    nome = models.CharField(max_length=100,help_text='nome da empresa')

    def __str__(self):
        return self.nome
