from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .models import AccountSettings
from .serializers import AccountSettingsSerializer

class AccountSettingsView(APIView):
    def post(self, request):
        data = request.data.copy()

        #  HASHING
        data["password"] = make_password(data["password"])

        serializer = AccountSettingsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Account settings saved successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
