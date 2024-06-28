# dashboard/api/serializers.py
from rest_framework import serializers
from dashboard.models import DataPoint


class DataPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPoint
        fields = '__all__'
