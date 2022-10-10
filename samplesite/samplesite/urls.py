from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('bboard/', include('bboard.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]
