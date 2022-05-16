from django.db import models
from apps.empregados.models import Empregados


class registrohoras (models.Model):
    motivo = models.CharField(max_length=100)
    empregados=models.ForeignKey(Empregados,on_delete=models.PROTECT)
    horas=models.DecimalField(max_digits=5,decimal_places=2)



    def __str__(self):
        return self.motivo


# Create your models here.
