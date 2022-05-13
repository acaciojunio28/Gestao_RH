from django.db import models
from apps.empregados.models import Empregados

class documentos(models.Model):
    descricao= models.CharField(max_length=100)
    pertence=models.ForeignKey(Empregados,on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao

# Create your models here.
