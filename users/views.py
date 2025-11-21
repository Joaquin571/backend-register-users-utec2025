from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer
from .utils.notify import send_welcome_email, send_admin_notification
from django.http import JsonResponse
from django.conf import settings

class UsersView(APIView):

    def get(self, request):
        users = User.objects.all().order_by('-created_at')
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = UserSerializer(data=request.data)
        if not ser.is_valid():
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

        user = ser.save()

        try:
            send_welcome_email(user.email, user.name, user.phone)

            send_admin_notification(
                settings.ADMIN_EMAIL,
                user.name,
                user.email,
                user.phone
            )
        except Exception as e:
            print("Notification failed:", e)

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

def healthcheck(request):
    return JsonResponse({"status": "ok"})
