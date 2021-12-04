from rest_framework import serializers
from .models import Profile
import uuid


class ProfileSerializer(serializers.Serializer):    
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=10)
    date_of_birth = serializers.DateField()

    def create(self, validated_data):

        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(1)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.id = validated_data.get('id', instance.id)
        instance.save()
        return instance
