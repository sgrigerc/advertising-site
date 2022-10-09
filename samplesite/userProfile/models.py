from django.db import models
from django.views.generic.edit import CreateView


class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    telegramm = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):

        return str(self.user)

