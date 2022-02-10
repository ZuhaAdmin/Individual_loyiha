from django.shortcuts import render
from .models import Sinflar

# Create your views here.
def sinflar(request):
    sinf = Sinflar.objects.all()
    data = {
        'sinf':sinf,
    }
    return render(request, template_name='sinflar.html', context=data)