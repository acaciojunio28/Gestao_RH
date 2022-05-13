from django.db import models
from apps.empresas.models import Empresa

class departamento(models.Model):
    nome=models.CharField(max_length=100,)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)


    def __str__(self):
        return self.nome
        return self.empresa





