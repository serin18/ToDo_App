from rest_framework import serializers
from reminder.models import Task
from django.contrib.auth.models import User

class task_serializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Task
        fields="__all__"

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","password"]
        read_onl_fields=["id"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
