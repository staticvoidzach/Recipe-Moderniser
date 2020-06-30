import graphene
from graphene_django.types import DjangoObjectType
from .models import WeightUnit, BaseWeightUnit, VolumeUnit, BaseVolumeUnit

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


class Query(object):
    all_weight_units = graphene.List(WeightType)
    all_volume_units = graphene.List(VolumeType)
    base_weight_unit = graphene.Field(BaseWeightType)
    base_volume_unit = graphene.Field(BaseVolumeType)

    def resolve_all_weight_units(self, info, **kwargs):
        return WeightUnit.objects.all()

    def resolve_all_volume_units(self, info, **kwargs):
        return VolumeUnit.objects.all()

    def resolve_base_weight_unit(self, info, **kwargs):
        return BaseWeightUnit.get_solo()

    def resolve_base_volume_unit(self, info, **kwargs):
        return BaseVolumeUnit.get_solo()