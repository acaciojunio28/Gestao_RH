from django.urls import path
from .views import DocumentosCreate

urlpatterns = [
    path('novo/<int:empregado>/', DocumentosCreate.as_view(), name='DocumentosCreate'),

    ]