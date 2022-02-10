from django.db import models

# Create your models here.
class Oquvchilar(models.Model):
    name = models.CharField(verbose_name="FISH", max_length=50)
    class_name = models.CharField(verbose_name="Sinfi", max_length=5)
    birthday = models.DateField(verbose_name="Tug'ilgan sanasi")
    phone = models.CharField(verbose_name="Telefon raqami", max_length=20)
    adress = models.CharField(verbose_name="Yashash manzili", max_length=300)
    image = models.ImageField(verbose_name="Surati", upload_to='oquvchilar/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Oquvchi"
        verbose_name_plural = "Oquvchilar"