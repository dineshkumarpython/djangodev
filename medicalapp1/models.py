from django.db import models


# Create your models here.
class CountNumber(models.Model):
    title = models.CharField(max_length=200)
    numbers = models.CharField(max_length=255)


    def __str__(self):
        return self.title

class Profie(models.Model):
    name = models.CharField(max_length=20)