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

class Product(models.Model):
    """
    Описание модели продукта
    """

    product_name = models.CharField(max_length=150,
                                    verbose_name='Название продукта')
    description = models.TextField(max_length=10000,
                                   blank=True,
                                   verbose_name='Описание продукта')
    product_image = models.ImageField(upload_to='', blank=True, null=True, verbose_name='Фото')
    product_category = models.ForeignKey(Category,
                                         on_delete=models.CASCADE,
                                         related_name='products',
                                         verbose_name='Категория')
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена продукта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-created_at']

