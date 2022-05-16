from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView,DeleteView
from .models import registrohoras

# Create your views here.

class HorasextraList(ListView):
    model=registrohoras

    def get_queryset(self):
        empresa_logada=self.request.user.empregados.empresa
        return registrohoras.objects.filter(empregados__empresa=empresa_logada)

class HorasextraEdit(UpdateView):
    model = registrohoras
    fields = ['motivo', 'empregados','horas']
    success_url = "/horas/"

class HorasextraDelete(DeleteView):
    model = registrohoras
    success_url = "/horas/"