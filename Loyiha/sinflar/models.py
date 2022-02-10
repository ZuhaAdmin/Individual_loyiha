from django.db import models

# Create your models here.
class Sinflar(models.Model):
    classname = models.CharField(verbose_name="Sinflar_nomi", max_length=10)
    number = models.IntegerField(verbose_name="O'quvchilar_soni")
    classroom = models.IntegerField(verbose_name="Biriktirilgan_xona")
    leader = models.CharField(verbose_name="Rahbari", max_length=50)
    part = models.IntegerField(verbose_name="Smenasi")
    image = models.ImageField(verbose_name="Surati", upload_to='Sinflar/')

    def __str__(self):
        return self.classname

    class Meta:
        verbose_name = "Sinf"
        verbose_name_plural = "Sinflar"