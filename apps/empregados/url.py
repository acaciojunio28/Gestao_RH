from django.urls import path
from .views import EmpregadoList,EmpregadoEdit,EmpregadoDelet,EmpregadoCreate

urlpatterns = [
    path('', EmpregadoList.as_view(),name='EmpregadoList'),
    path('editar/<int:pk>/', EmpregadoEdit.as_view(), name='EmpregadoEdit'),
    path('delete/<int:pk>/', EmpregadoDelet.as_view(), name='EmpregadoDelet'),
path('Create', EmpregadoCreate.as_view(), name='EmpregadoCreate'),

]
