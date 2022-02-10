from django.urls import path
from .views import sinflar

urlpatterns = [
    path ('', sinflar)
]