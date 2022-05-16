from django.urls import path
from .views import HorasextraList,\
    HorasextraEdit,\
    HorasextraDelete

urlpatterns = [
    path('', HorasextraList.as_view(),name='HorasextraList'),
    path('editar/<int:pk>/', HorasextraEdit.as_view(),name='HorasextraEdit'),
    path('delete/<int:pk>/', HorasextraDelete.as_view(), name='HorasextraDelete'),
    ]