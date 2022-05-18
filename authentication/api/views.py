from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .serializers import (RegisterUserSerializer, LoginSerializer)


from rest_framework import permissions


# class RegisterUserAPIView(APIView):
#     authentication_classes=[]

#     def post(self,):
        

class RegisterUserAPI(generics.GenericAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes=[permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class LoginUserAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data,status= status.HTTP_200_OK)