from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import documentos


class DocumentosCreate(CreateView):
    model = documentos
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['empregado']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

# Create your views here.
