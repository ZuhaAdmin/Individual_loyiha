from django.shortcuts import render
from .models import Oqituvchilar

# Create your views here.
def oqituvchilar(request):
    objects = Oqituvchilar.objects.all()

    data = {
        'objects':objects,
    }
    return render(request, template_name='oqituvchilar.html', context=data)