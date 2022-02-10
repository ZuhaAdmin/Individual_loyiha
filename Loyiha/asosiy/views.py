from django.shortcuts import render

# Create your views here.
def asosiysahifa(qiymat):
    return render(qiymat, template_name = 'index.html')