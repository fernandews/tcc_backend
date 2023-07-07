from rest_framework import serializers
from app.models import User, Geolocation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'course', 'birthdate', 'user_type', 'choses_path_by', 'goes_to', 'username', 'password' ]
        extra_kwargs = {
            'name': {'required': True},
            'course': {'required': True},
            'birthdate': {'required': True},
            'user_type': {'required': True},
            'choses_path_by': {'required': True},
            'goes_to': {'required': True},
            'username': {'required': True},
            'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = ['user', 'occurrence_datetime', 'geolocation_data']
        
    def create(self, validated_data):
        geolocation = Geolocation.objects.create(**validated_data)
        return geolocation