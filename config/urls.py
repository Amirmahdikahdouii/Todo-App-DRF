from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("tasks.urls", namespace="tasks")),
    path('accounts/', include("accounts.urls", namespace="accounts")),
]
