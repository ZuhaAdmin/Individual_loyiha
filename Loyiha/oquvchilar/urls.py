from django.urls import path
from .views import oquvchilar

urlpatterns = [
    path ('', oquvchilar)
]