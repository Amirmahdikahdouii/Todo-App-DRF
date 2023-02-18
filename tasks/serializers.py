from rest_framework import serializers
# Models:
from .models import Task
from django.contrib.auth.models import AnonymousUser


class TaskSerializers(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = {
            "email": instance.user.email,
            "first_name": instance.user.first_name,
            "last_name": instance.user.last_name,
        }
        return data

    class Meta:
        fields = "__all__"
        model = Task
