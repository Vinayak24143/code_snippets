from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from rest_framework_simplejwt.tokens import RefreshToken
from .managers import UserManager
from organization.models import Organization


class User(AbstractBaseUser, PermissionsMixin):

    USER_ROLE_CHOICES = (
        (1, 'IT admin'),
        (2, 'Security admin'),
        (3, 'System integrator'),
        (4, 'Marshal'),
        (5, 'Customer'),
    )


    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=255, unique=True, db_index=True)
    mobile = models.IntegerField(null=True, blank=True, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.PositiveSmallIntegerField(choices=USER_ROLE_CHOICES, null=True,blank=True)
    organization = models.ForeignKey(to=Organization, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to="img/profile/", null=True, blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)


    USERNAME_FIELD='email'

    objects=UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {'access':str(refresh.access_token),'refresh':str(refresh)}
