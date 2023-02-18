from django.urls import path, include

# DRF Router:
from rest_framework import routers

# Views:
from .views import TaskViewSet

router = routers.SimpleRouter()
router.register("api-tasks", TaskViewSet, basename="task")

app_name = "tasks"
urlpatterns = [
    path("", include(router.urls))
]
