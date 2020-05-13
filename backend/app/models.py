from django.db import models

# Create your models here.


class Modelone(models.Model):
    name = models.CharField(length = 100)