from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

from .models import User
from .serializers import UserSerializer

class UsersView(APIView):
    def get(self, request):
        users = User.objects.all().order_by("-created_at")
        data = UserSerializer(users, many=True).data
        return Response(data, status=200)

    def post(self, request):
        ser = UserSerializer(data=request.data)
        if not ser.is_valid():
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        user = ser.save()

        # Notificación por email al crear (consola en dev)
        send_mail(
            subject="Nuevo usuario creado",
            message=f"Nombre: {user.name}\nEmail: {user.email}\nTel: {user.phone}",
            from_email=None,                 # usa DEFAULT_FROM_EMAIL si lo definís
            recipient_list=["admin@example.com"],
            fail_silently=False,
        )
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
