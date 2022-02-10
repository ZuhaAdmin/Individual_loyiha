from django.db import models

# Create your models here.
class Oqituvchilar(models.Model):
    name = models.CharField(verbose_name="FISH", max_length=50)
    position = models.CharField(verbose_name="Lavozimi", max_length=40)
    age = models.IntegerField(verbose_name="Yoshi")
    phone = models.CharField(verbose_name="Telefon raqami", max_length=20)
    level = models.CharField(verbose_name="Malumoti", max_length=40)
    salary = models.IntegerField(verbose_name="Maoshi")
    image = models.ImageField(verbose_name="Surati", upload_to='oqituvchi/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Oqituvchi"
        verbose_name_plural = "Oqituvchilar"