from django.db import models

# Create your models here.


class Modelone(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    message = models.TextField()
    created  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

