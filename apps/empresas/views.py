from django.shortcuts import render,HttpResponse,redirect
from django.views.generic.edit import CreateView,UpdateView
from .models import Empresa

# Create your views here.
class EmpresaCreate(CreateView):
    model=Empresa
    fields=['nome']

    def form_valid(self,form):
        obj=form.save()
        Empregado=self.request.user.empregados
        Empregado.empresa = obj
        Empregado.save()
        return HttpResponse('ok')

class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']
    success_url = "/"



