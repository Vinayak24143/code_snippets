from authentication.api import views
from django.urls import path


urlpatterns=[
    path('register/', views.RegisterUserAPI.as_view(), name='register'),
    path('login/', views.LoginUserAPI.as_view(), name='login'),
]