from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def login(request):
  user=get_object_or_404(User,username=request.data['username'])
  if not user.check_password(request.data['password']):
    return Response({"detail":"Not found"},status=status.HTTP_404_NOT_FOUND)
  token,created=Token.objects.get_or_create(user=user)
  user_data = UserSerializer(user).data
  return Response({'token': token.key, 'user': user_data}, status=status.HTTP_201_CREATED)
  
  return Response

@api_view(['POST'])
def signup(request):
    if User.objects.filter(username=request.data.get('username')).exists():
        return Response({'error': 'Username already taken.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        # Crée l'utilisateur avec create_user pour que le mot de passe soit hashé directement
        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
            email=serializer.validated_data.get('email', '')
        )

        token, _ = Token.objects.get_or_create(user=user)

        # Réutiliser le serializer pour retourner les bonnes infos sans le mot de passe
        user_data = UserSerializer(user).data
        return Response({'token': token.key, 'user': user_data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def test_token(request):
  return Response