from rest_framework import serializers
from .models import Application
import re

class ApplicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'full_name', 'phone_number', 'email', 'status', 'created_at', 'update_at']

    def validate_phone_number(self, value):
        phone_number_pattern = r'^\+998\d{9}$'
        if not re.match(phone_number_pattern, value):
            raise serializers.ValidationError("Phone number must be in the format +998xx xxx xx xx.")
        return value

    def create(self, validated_data):
        validated_data['status'] = 'new'
        return super().create(validated_data)