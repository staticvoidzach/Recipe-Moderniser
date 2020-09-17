import graphene
from graphene_django.types import DjangoObjectType
from .models import WeightUnit, BaseWeightUnit, VolumeUnit, BaseVolumeUnit

# =====================
# Creating GQL types to read Django models
# =====================
class WeightType(DjangoObjectType):
    class Meta:
        model = WeightUnit

class VolumeType(DjangoObjectType):
    class Meta:
        model = VolumeUnit


class BaseWeightType(DjangoObjectType):
    class Meta:
        model = BaseWeightUnit

class BaseVolumeType(DjangoObjectType):
    class Meta:
        model = BaseVolumeUnit

# =====================


class Query(object):
    all_weight_units = graphene.List(WeightType) # Returns a list of weight types
    all_volume_units = graphene.List(VolumeType) # Returns a list of volume types
    base_weight_unit = graphene.Field(BaseWeightType) # Returns the base weight type
    base_volume_unit = graphene.Field(BaseVolumeType) # Returns the base volume type

    def resolve_all_weight_units(self, info, **kwargs):
        # Fetch all weight types ordered by their factor
        return WeightUnit.objects.order_by('factor').all()

    def resolve_all_volume_units(self, info, **kwargs):
        # Fetch all volume types ordered by their factor
        return VolumeUnit.objects.order_by('factor').all()

    def resolve_base_weight_unit(self, info, **kwargs):
        # Fetch the base weight unit
        return BaseWeightUnit.get_solo()

    def resolve_base_volume_unit(self, info, **kwargs):
        # Fetch the base volume unit
        return BaseVolumeUnit.get_solo()