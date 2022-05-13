from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import departamento
from apps.empresas.models import Empresa

class Empregados(models.Model):
    nome=models.CharField(max_length=100, )
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamento = models.ManyToManyField(departamento)
    empresa=models.ForeignKey(Empresa,on_delete=models.PROTECT,null=True,blank=True)

    def __str__(self):
        return self.nome
