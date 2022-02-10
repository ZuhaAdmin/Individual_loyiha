from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.files import ImageField

# Create your models here.
class rahbar(models.Model):
    name = CharField(verbose_name="FISH", max_length=50)
    position = CharField(verbose_name="Lavozim", max_length=50)
    age = IntegerField(verbose_name="Yoshi")
    phone = CharField(verbose_name="Telefoni", max_length=20)
    level = CharField(verbose_name="Malumoti", max_length=30)
    image = ImageField(verbose_name="Rasm", upload_to = 'rahbariyat/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Rahbar"
        verbose_name_plural = "Rahbarlar"