from django.db import models

class Person(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()