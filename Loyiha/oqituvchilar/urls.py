from django.urls import path
from .views import oqituvchilar

urlpatterns = [
    path ('', oqituvchilar)
]