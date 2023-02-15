# DRF Views
from rest_framework.viewsets import ModelViewSet
# Serializers:
from .serializers import TaskSerializers
# Models
from .models import Task


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializers
    queryset = Task.objects.all()
