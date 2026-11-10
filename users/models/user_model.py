from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomBaseUser(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='media/users/avatars', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=20, blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
