from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import WeightUnit, BaseWeightUnit, VolumeUnit, BaseVolumeUnit


# Register models so they show up in the admin interface
admin.site.register(WeightUnit)
admin.site.register(BaseWeightUnit, SingletonModelAdmin)
admin.site.register(VolumeUnit)
admin.site.register(BaseVolumeUnit, SingletonModelAdmin)
