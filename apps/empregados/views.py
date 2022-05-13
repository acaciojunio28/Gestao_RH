from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views.generic.edit import UpdateView,DeleteView,CreateView

from .models import Empregados

# Create your views here.

class EmpregadoList(ListView):
    model=Empregados

    def get_queryset(self):
        empresa_logada=self.request.user.empregados.empresa
        return Empregados.objects.filter(empresa=empresa_logada)

class EmpregadoEdit(UpdateView):
    model = Empregados
    fields =['nome','departamento']
    success_url = "/empregados/"

class EmpregadoDelet(DeleteView):
    model = Empregados
    success_url = "/empregados/"

class EmpregadoCreate(CreateView):
    model=Empregados
    fields = ['nome', 'departamento']

    def form_valid(self, form):
        empregados = form.save(commit=False)
        username = empregados.nome.split(' ')[0] + empregados.nome.split(' ')[1]
        empregados.empresa = self.request.user.empregados.empresa
        empregados.user = User.objects.create(username=username)
        empregados.save()
        return super(EmpregadoCreate, self).form_valid(form)

    success_url = "/empregados/"

