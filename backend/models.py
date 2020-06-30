from django.db import models
from solo.models import SingletonModel

class WeightUnit(models.Model):
    name = models.CharField(max_length=20)
    factor = models.FloatField()

    def __str__(self):
        return self.name

class BaseWeightUnit(SingletonModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"Base Weight Unit [{self.name}]"

    class Meta:
        verbose_name = "Base Weight Unit"



class VolumeUnit(models.Model):
    name = models.CharField(max_length=20)
    factor = models.FloatField()

    def __str__(self):
        return self.name

class BaseVolumeUnit(SingletonModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"Base Volume Unit [{self.name}]"

    class Meta:
        verbose_name = "Base Volume Unit"






