from django.shortcuts import render
from .models import rahbar

# Create your views here.
def rahbariyat(qiymat):
    objects = rahbar.objects.all()
    data = {
        'objects':objects
    }

    return render(qiymat, template_name = 'rahbariyat.html', context=data)
