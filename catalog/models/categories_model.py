from django.db import models

class Category(models.Model):
    """
    Описание категории продуктов
    """
    category_name = models.CharField(max_length=150,
                                     verbose_name='Название категории')
    description = models.CharField(max_length=10000,
                                   verbose_name='Описание категории')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'