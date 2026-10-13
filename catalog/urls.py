from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('contacts/', views.contacts, name='contacts'),
    path('categories/', views.categories, name='categories'),
    path('category/<int:category_id>/products/', views.category_products, name='products_category'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/create', views.create_product, name='create_product')
]