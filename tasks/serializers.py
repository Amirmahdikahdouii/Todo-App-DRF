from rest_framework import serializers
# Models:
from .models import Task


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Task
