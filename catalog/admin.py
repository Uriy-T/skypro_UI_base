from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdm(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)


@admin.register(Product)
class ProductAdm(admin.ModelAdmin):
    list_display = ('product_name', 'price_per_unit')
    search_fields = ('product_name',)
