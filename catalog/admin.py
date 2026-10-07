from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdm(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('category_name',)


@admin.register(Product)
class ProductAdm(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price_per_unit', 'product_category')
    list_filter = ('product_category',)
    search_fields = ('product_name', 'description')
