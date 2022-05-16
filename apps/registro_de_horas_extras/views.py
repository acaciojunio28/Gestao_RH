from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
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

class HorasextraCreate(CreateView):
    model = registrohoras
    fields = ['motivo', 'empregados','horas']

    def form_valid(self, form):
        horas = form.save(commit=False)
        horas.empresa = self.request.user.empregados.empresa
        horas.save()
        return super(HorasextraCreate, self).form_valid(form)
    success_url = "/horas/"