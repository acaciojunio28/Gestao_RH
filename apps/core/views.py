from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.empregados.models import Empregados
def home(request):
    data={}
    data['usuario']=request.user
    return render(request,'core/index.html',data)
