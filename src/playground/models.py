from statistics import mode
from django.db import models
import datetime
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    quantity = models.IntegerField()
    dates = models.DateTimeField(default =  datetime.datetime.now )
    def __str__(self) :
        return self.name
    