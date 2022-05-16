from django.urls import path
from .views import HorasextraList,\
    HorasextraEdit,\
    HorasextraDelete,\
    HorasextraCreate


urlpatterns = [
    path('', HorasextraList.as_view(),name='HorasextraList'),
    path('novo', HorasextraCreate.as_view(),name='HorasextraCreate'),
    path('editar/<int:pk>/', HorasextraEdit.as_view(),name='HorasextraEdit'),
    path('delete/<int:pk>/', HorasextraDelete.as_view(), name='HorasextraDelete'),
    ]