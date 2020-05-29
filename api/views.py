from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Users, Activities
from .serializers import UserSerializer, ActivitySerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def users_api_view(request):
    if request.method == 'GET':
        data={}
        users = Users.objects.all()
        ser = UserSerializer(users, many=True)
        data['ok'] = True
        data['members'] = ser.data
        return Response(data, status=status.HTTP_200_OK)

