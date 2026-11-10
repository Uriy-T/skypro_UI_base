from django.contrib import admin
from .models import ArticleModel


@admin.register(ArticleModel)
class ArticleAdm(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_public', 'view_count','created_at']
    list_filter = ('is_public',)
    search_fields = ('id', 'title', 'created_at')
