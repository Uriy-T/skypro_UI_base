from django.db import models
from django.core.validators import MinValueValidator


class ArticleModel(models.Model):
    """
    Описание модели статьи блога
    """

    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    preview_image = models.ImageField(upload_to='articles/previews', null=True, blank=True, verbose_name='Превью')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_public = models.BooleanField(default=False, null=False, verbose_name='Опубликовано')
    view_count = models.IntegerField(default=0, null=False, validators=[MinValueValidator(0)],
                                     verbose_name='Количество просмотров')

    def __str__(self):
        return f'Статья: "{self.title}"'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']
