from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from users.views import ResetPasswordView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('bboard/', include('bboard.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
             auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
             name='password_reset_confirm'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]
