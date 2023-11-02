from django.db import models

# Create your models here.


class Medication(models.Model):
    name = models.CharField(max_length = 200)
    classification = models.CharField(max_length=200)
    intention = models.TextField(max_length=200)
    implications = models.TextField(max_length=200)
    dose = models.CharField(max_length=200)
    route = models.CharField(max_length=200)
    frequency = models.CharField(max_length=200)

    def __str__(self):
        return self.name