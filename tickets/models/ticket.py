from django.db import models
from .travel_class import TravelClass

class Ticket(models.Model):
    origin = models.CharField(max_length=100)
    destiny = models.CharField(max_length=100)
    departure_date = models.DateField()
    back_date = models.DateField()
    search_date = models.DateField()
    infos = models.TextField(max_length=200, blank=True)
    class_type = models.CharField(max_length=4,choices=TravelClass.choices, default=0)
