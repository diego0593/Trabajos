from django.db.models.functions import Cast
from rest_framework import serializers

from .models import Publicidad,Clicks,Viewability

from django.db.models import DecimalField



class PublicidadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Publicidad
        fields='__all__'


class ClickSerializer(serializers.ModelSerializer):

    class Meta:
        model=Clicks
        fields = '__all__'


class ViewableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Viewability
        fields='__all__'

