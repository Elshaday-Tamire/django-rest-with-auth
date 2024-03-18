# Create your views here.
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from rest_framework import permissions

class IsNormalUser(permissions.BasePermission):
    """
    Custom permission to only allow users with group 'normalUser' to access the API.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name='normalUser').exists()



@api_view(['POST'])
def addEqubType(request):
    if isinstance(request.data, list):
        serializer = serializers.EqubTypeSerializer(data=request.data, many=True)
    else:
        serializer = serializers.EqubTypeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "message": "success fully saved"}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsNormalUser])
def addEqub(request):
    if isinstance(request.data, list):
        serializer = serializers.EqubSerializer(data=request.data, many=True)
    else:
        serializer = serializers.EqubSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "message": "success fully saved"}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)