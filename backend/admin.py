from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import WeightUnit, BaseWeightUnit, VolumeUnit, BaseVolumeUnit

admin.site.register(WeightUnit)
admin.site.register(BaseWeightUnit, SingletonModelAdmin)
admin.site.register(VolumeUnit)
admin.site.register(BaseVolumeUnit, SingletonModelAdmin)
