# Views, Response from rest_framework
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response

# Serializer Classes
from .serializers import UserSerializer, VerifyEmailSerializer

# Permissions
from rest_framework.permissions import AllowAny

# Models
from .models import VerifyEmail


# APIView to register new user model
class RegisterUserAPIView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


# Send Verification Email APIView
class SendVerificationEmailAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = VerifyEmailSerializer

    def create(self, request, *args, **kwargs):
        import random
        verify_key = random.randint(111111, 999999)
        user_email = request.POST.get('email')
        serializer = self.serializer_class(data={'email': user_email, "verify_key": verify_key})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Email Verification send!"}, status=201)
        return Response(serializer.errors, status=409)


# Confirm Verification Email APIView

class ConfirmEmailVerificationAPIView(UpdateAPIView):
    serializer_class = VerifyEmailSerializer
    permission_classes = [AllowAny]

    def update(self, request, *args, **kwargs):
        email = request.POST.get("email")
        verify_key = request.POST.get("verify_key")
        try:
            email_instance = VerifyEmail.objects.get(email=email)
        except VerifyEmail.DoesNotExist:
            return Response({"message": "Email Not found"}, status=404)
        serializer = self.serializer_class(email_instance, {'email': email, "verify_key": verify_key})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "verification was successful!"}, status=200)
        Response(serializer.errors, status=400)
