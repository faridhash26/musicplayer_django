from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    profile_name = models.CharField(blank=True, max_length=100)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    def set_avatar(self):
        avatar = self.avatar
        if not avatar:
            self.avatar="------REPLACE THIS WITH YOUR DEFAULT AVATAR URL-----"

    def __str__(self):
        return self.email