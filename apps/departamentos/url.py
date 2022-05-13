from django.urls import path
from .views import DepartamentosList,DepartamentosCreate

urlpatterns = [
    path('', DepartamentosList.as_view(), name='DepartamentoList'),
    path('novo', DepartamentosCreate.as_view(), name='DepartamentosCreate'),
]