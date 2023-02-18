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

    def validate_user(self, user):
        """
        This Method is for validating user object that come from request data!
        """
        request = self.context.get("request", None)
        if request is None:
            # If your using shell to deserialize, change behaviour of this section
            raise serializers.ValidationError({
                "request": [
                    'rest_framework request class is required!'
                ]
            })
        if request.user != user and request.user.is_admin is False:
            raise serializers.ValidationError({
                "user": [
                    'you\'re not allowed to create or change task for someone else!'
                ]
            })
        return user

    class Meta:
        fields = "__all__"
        model = Task
