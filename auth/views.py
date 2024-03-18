from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.settings import api_settings

class CustomAccessToken(AccessToken):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def for_user(cls, user):
        token = super().for_user(user)
        token['email'] = user.email  
        token['username'] = user.username

        # Get groups associated with the user and add them to the token
        groups = user.groups.all()
        token['groups'] = [group.name for group in groups]

        return token


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = get_object_or_404(User, username=username)

    if not user.check_password(password):
        return Response({"detail": "Incorrect username/password"}, status=status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)
    custom_access_token = CustomAccessToken.for_user(user)

    return Response({
        'access': str(custom_access_token),
        'refresh': str(refresh),
    })

from django.contrib.auth.models import Group

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        # Save the user without committing to the database
        user = serializer.save()
        # Set password for the user
        user.set_password(request.data['password'])

        # Retrieve or create groups based on the provided group names
        group_names = request.data.get('groups', [])  # Assuming group names are provided in the request data
        groups = [Group.objects.get_or_create(name=group_name)[0] for group_name in group_names]
        
        # Assign user to groups
        user.groups.add(*groups)
        
        # Save the user with updated attributes
        user.save()

        # Generate custom access token
        custom_access_token = CustomAccessToken.for_user(user)

        return Response({"token": str(custom_access_token), "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    username = request.user.username
    return Response("Passed for {}".format(username))


