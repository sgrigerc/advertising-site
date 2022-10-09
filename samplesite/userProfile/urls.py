from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    path('create_profile_page/',CreateProfilePageView.as_view(), name='create_user_profile'),
]

  