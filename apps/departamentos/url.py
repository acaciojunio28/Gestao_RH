from django.urls import path
from .views import DepartamentosList,\
    DepartamentosCreate,\
    DepartamentosUpdate,\
    DepartamentosDelete

urlpatterns = [
    path('', DepartamentosList.as_view(), name='DepartamentoList'),
    path('novo', DepartamentosCreate.as_view(), name='DepartamentosCreate'),
    path('update/<int:pk>/', DepartamentosUpdate.as_view(), name='DepartamentosUpdate'),
    path('delete/<int:pk>/', DepartamentosDelete.as_view(), name='DepartamentosDelete '),
]