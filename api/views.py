from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Users, Activities
from .serializers import UserSerializer, ActivitySerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


# Api view for returning the data in the json format.
@api_view(['GET'])
def users_api_view(request, pk=None):

    def get_object(obj_pk):
        obj = get_object_or_404(Users, pk=obj_pk)
        return obj  # Returns the object with id given in url

    if request.method == 'GET':
        data = {}

        if pk:
            user = get_object(pk)
            ser = UserSerializer(user)  # Serialize the specific object

        else:
            users = Users.objects.all()
            ser = UserSerializer(users, many=True)  # Serializing the objects

        data['ok'] = True
        data['members'] = ser.data
        return Response(data, status=status.HTTP_200_OK)  # Returns the serialized data as response
