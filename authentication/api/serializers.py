from cgitb import reset
from curses import reset_prog_mode
from urllib import response
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from django.contrib.auth import authenticate

from authentication.models import User



class RegisterUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=68, min_length=6,write_only=True)
    class Meta:
        model=User
        fields=[
            'email',
            'password',
            'first_name',
            'last_name',
            'mobile',
            'role',
            'image',
        ]
    
    def validate(self, attrs):
        role= attrs.get('role',None)
        
        if not role:
            raise serializers.ValidationError({"role":'Value can not be none.'})
        
        return attrs


    def create(self, validated_data):
        print(self.context)
        request=self.context['request']
        USER_ROLE_CREATION_PERMISSION={1:1,2:1,3:1,4:2,5:2}
        if not request.user.role==USER_ROLE_CREATION_PERMISSION[int(validated_data['role'])]:
            raise PermissionDenied({"detail":"You do not have permissions to create user of this role."})

        user = User.objects.create_user(**validated_data)
        return user
    

class LoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    first_name= serializers.CharField(max_length=255,read_only=True)
    last_name= serializers.CharField(max_length=255,read_only=True)
    password= serializers.CharField(min_length=6, max_length=68, write_only=True)
    role = serializers.IntegerField(read_only = True)
    tokens = serializers.CharField(max_length=255,read_only=True)
    image = serializers.ImageField(read_only=True)
    class Meta:
        model=User
        fields=['email','first_name','last_name','password', 'role', "tokens",'image']

    def validate(self, attrs):
        email=attrs.get('email',None)
        password=attrs.get('password',None)

        user= authenticate(email=email,password=password)
        print(user)
        if not user:
            raise AuthenticationFailed('Invalid user credentials, try again.')
        
        response={
            'email':user.email,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'role':user.get_role_display(),
            'tokens':user.tokens(),
            'image':None
        }
        if user.image:
            response['image']=user.image.url

        return response
    