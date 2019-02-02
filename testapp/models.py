from django.db import models
from django.urls import reverse

class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=64)


    def __str__(self):
        return self.ename

    def get_absolute_url(self):
        return reverse('list')

