from django.db import models

# Create your models here.


class Medication(models.Model):
    name = models.CharField(max_length = 200)
    classification = models.CharField(max_length=200)
    intention = models.CharField(max_length=200)
    implications = models.CharField(max_length=200)
    dose = models.CharField(max_length=200)
    route = models.CharField(max_length=200)
    frequency = models.CharField(max_length=200)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name
    
    def get_absolute_path(self):
        pass
