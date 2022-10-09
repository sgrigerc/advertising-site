from unicodedata import name
from .views import home, RegisterView
from django.urls import path


urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
]