# DRF Views
from rest_framework.viewsets import ModelViewSet

# Serializers:
from .serializers import TaskSerializers

# Models
from .models import Task


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializers

    def get_queryset(self):
        return Task.objects.filter(user_id=self.request.user.id)
