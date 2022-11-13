from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, UpdateAPIView
from accounts.serializers import RegisterSerializer, LoginSerializer, UserInfoSerializer
from rest_framework import response, status, authentication
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from accounts.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

import jwt

# Create your views here.


class RegisterAPIView(APIView):
    serializer_class = RegisterSerializer

    def get(self, request):
        return response.Response(status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def get(self, request):
        return response.Response({}, status=status.HTTP_200_OK)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # authenticate access to specified User's attributes
        user = authenticate(username=username, password=password)

        if user:
            serializer = self.serializer_class(user)

            # jwt.encode({'username': user.username, 'email': user.email}, "secret", algorithm="HS256")
            responsee = Response()

            # set JWT as a cookie
            responsee.set_cookie(key='token', value=serializer.data["token"], httponly=True)

            responsee.data = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username,
                'email': user.email,
                'phone_number': user.phone_number,
                'avatar': str(user.avatar),
                'token': serializer.data["token"]
            }

            responsee.status_code = status.HTTP_200_OK

            return responsee

            # return response.Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return response.Response({'message': "User does not exist, please try again"},
                                     status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(APIView):
    """
    Delete cookie containing token to log out user
    """

    def post(self, request):
        responsee = Response()

        responsee.status_code = status.HTTP_200_OK
        # delete cookie to logout user
        responsee.delete_cookie('token')
        responsee.data = {
            'message': 'User successfully logged out'
        }
        return responsee


class UserInfoAPIView(APIView):
    serializer_class = UserInfoSerializer
    # def get(self, request):
    #     token = request.COOKIES.get('token')
    #
    #     # check token authorization
    #     if token:
    #         return response.Response(jwt.decode(token, 'secret', algorithms="HS256"))
    #     else:
    #         return response.Response({'message': "you are not authorized to access user info"},
    #                                  status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        token = request.COOKIES.get('token')

        if token:
            user = User.objects.get(username=(jwt.decode(token, 'secret', algorithms="HS256")["username"]))
            serializer = self.serializer_class(user)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return response.Response({'message': "you are not authorized to access user info"},
                                     status=status.HTTP_401_UNAUTHORIZED)


class UpdateInfoAPIView(UpdateAPIView):
    serializer_class = UserInfoSerializer

    def update(self, request, *args, **kwargs):
        token = request.COOKIES.get('token')

        if token:
            user = User.objects.get(username=jwt.decode(token, 'secret', algorithms="HS256")["username"])
            serializer = self.serializer_class(user, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response({'message': "you are not authorized to access user info"},
                                     status=status.HTTP_401_UNAUTHORIZED)