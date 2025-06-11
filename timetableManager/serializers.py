from rest_framework import serializers
from .models import Timetable

class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = ['id', 'day_of_week', 'meal_type', 'created_at', 'updated_at', 'meals']
        read_only_fields = ['created_at', 'updated_at']
    
