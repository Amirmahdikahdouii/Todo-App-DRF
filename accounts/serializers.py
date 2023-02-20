# Rest Framework Serializers
from rest_framework import serializers

# JWT Authentication Serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Models
from django.contrib.auth import get_user_model
from .models import VerifyEmail
from django.core.mail import send_mail


# Customizing Behaviour of TokenObtainPairView Serializer Class
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = {
            "email": self.user.email,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
        }
        return data


# UserModel Serializer
class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=100, write_only=True)
    password2 = serializers.CharField(max_length=100, write_only=True)

    def validate_email(self, value):
        if VerifyEmail.objects.check_email_verification(value) is False:
            raise serializers.ValidationError("Verify Your email first!")
        elif get_user_model().objects.check_email_exist(value):
            raise serializers.ValidationError("Email Already Exists!")
        return value

    def validate(self, data):
        password1 = data.get('password1', None)
        password2 = data.get('password2', None)
        if password1 is None or password2 is None:
            raise serializers.ValidationError({
                "password": ["Password fields are required"],
            })
        elif password1 != password2:
            raise serializers.ValidationError({
                "password2": ["Password fields are not match"],
            })
        return data

    def create(self, validated_data):
        password = validated_data.pop("password1")
        validated_data.pop("password2")
        return get_user_model().objects.create(password=password, **validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.birthday = validated_data.get("birthday", instance.birthday)
        return instance

    class Meta:
        model = get_user_model()
        fields = ("email", 'password1', 'password2', 'first_name', 'last_name', 'birthday')


class VerifyEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyEmail
        fields = ['email', 'verify_key']

    def create(self, validated_data):
        user_email = validated_data.get("email")
        if VerifyEmail.objects.email_exists(user_email):
            raise serializers.ValidationError({
                "email": ["Email already exists!"]
            })
        verify_key = validated_data.get("verify_key")
        data = {
            "subject": "verification Email",
            "message": f"Please confirm your email by using this key: {verify_key}",
            "from_email": "Email from Todo-App-DRF Team",
            "recipient_list": [user_email]
        }
        send_mail(**data)
        return VerifyEmail.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if instance.verify_key == validated_data['verify_key'] and instance.email == validated_data['email']:
            instance.is_verified = True
            instance.save()
            return instance
        raise serializers.ValidationError({
            "verify_key": ['verify key is not correct!']
        })
