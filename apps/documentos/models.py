from django.db import models
from django.urls import reverse
from apps.empregados.models import Empregados

class documentos(models.Model):
    descricao= models.CharField(max_length=100)
    pertence=models.ForeignKey(Empregados,on_delete=models.PROTECT)
    arquivo= models.FileField (upload_to='documentos')

    def get_absolute_url(self):
        return reverse('EmpregadoEdit', args=[self.pertence.id])

    def __str__(self):
        return self.descricao

# Create your models here.
