from django.shortcuts import render
from .models import Oquvchilar

# Create your views here.
def oquvchilar(request):
    pupils = Oquvchilar.objects.all()

    data = {
        'pupils':pupils,
    }
    return render(request, template_name='oquvchilar.html', context=data)