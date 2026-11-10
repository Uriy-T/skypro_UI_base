from django.urls import path
from .views import CategoryCreateView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView, CategoryListView, \
    ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView, ProductListView

app_name = 'catalog'

urlpatterns = [
    # Пути категорий
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/detail/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('category/update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),

    # Пути продуктов
    path('category/<int:pk>/product_list', ProductListView.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete')
]
