# Generic Views
from rest_framework.generics import CreateAPIView

# Serializer Classes
from .serializers import UserSerializer


# APIView to register new user model
class RegisterUserAPIView(CreateAPIView):
    serializer_class = UserSerializer
