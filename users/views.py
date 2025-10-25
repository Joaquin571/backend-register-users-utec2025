from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import User
from .serializers import UserSerializer
from .utils.notify import send_welcome_email   

class UsersView(APIView):
    def get(self, request):
        users = User.objects.order_by("-id")
        data = UserSerializer(users, many=True).data
        return Response(data)

    def post(self, request):
        ser = UserSerializer(data=request.data)
        if not ser.is_valid():
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

        user = ser.save()

        try:
            send_welcome_email(user.email, user.name, user.phone)
        except Exception as e:
            print("Notification failed:", e)

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
