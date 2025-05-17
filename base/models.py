from django.db import models
from django.urls import reverse

# Create your models here.


class Medication(models.Model):
    class Frequency(models.TextChoices):
        ONCE_DAILY = 'QD', 'Once Daily'
        TWICE_DAILY = 'BID', 'Twice Daily'
        THREE_TIMES_DAILY = 'TID', 'Three Times Daily'
        FOUR_TIMES_DAILY = 'QID', 'Four Times Daily'
        AS_NEEDED = 'PRN', 'As Needed' 

    name = models.CharField(max_length = 200)
    classification = models.CharField(max_length=200)
    intention = models.CharField(max_length=200)
    implications = models.CharField(max_length=200)
    dose = models.CharField(max_length=200)
    route = models.CharField(max_length=200)
    frequency = models.CharField(
        max_length = 3,
        choices=Frequency.choices,
        default=Frequency.ONCE_DAILY,
    )

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name
    