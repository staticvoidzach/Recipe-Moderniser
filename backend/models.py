from django.db import models
from solo.models import SingletonModel

# A weight unit
class WeightUnit(models.Model):
    name = models.CharField(max_length=20) # Name of weight unit
    factor = models.FloatField() # Factor of weight unit

    def __str__(self):
        return self.name

# Singleton weight unit to be the base weight unit
class BaseWeightUnit(SingletonModel):
    name = models.CharField(max_length=20) # Name of base weight unit
    # No factor because base is always 1

    def __str__(self):
        return f"Base Weight Unit [{self.name}]"

    class Meta:
        verbose_name = "Base Weight Unit"


# A volume unit
class VolumeUnit(models.Model):
    name = models.CharField(max_length=20) # Name of volume unit
    factor = models.FloatField() # Factor of volume unit

    def __str__(self):
        return self.name

# Singleton volume unit to be the base volume unit
class BaseVolumeUnit(SingletonModel):
    name = models.CharField(max_length=20) # Name of base volume unit
    # No factor because base is always 1

    def __str__(self):
        return f"Base Volume Unit [{self.name}]"

    class Meta:
        verbose_name = "Base Volume Unit"






