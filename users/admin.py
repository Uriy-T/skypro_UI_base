from django.contrib import admin
from .models import CustomBaseUser


@admin.register(CustomBaseUser)
class UsersAdm(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name')
    search_fields = ('username', 'first_name', 'last_name')