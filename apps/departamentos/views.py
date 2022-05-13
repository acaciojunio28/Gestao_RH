from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import departamento

class DepartamentosList(ListView):
    model = departamento

    def get_queryset(self):
        empresa_logada = self.request.user.empregados.empresa
        return departamento.objects.filter(empresa=empresa_logada)


class DepartamentosCreate(CreateView):
    model = departamento
    fields=['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.empregados.empresa
        departamento.save()
        return super(DepartamentosCreate, self).form_valid(form)

    success_url = "/departamento/"