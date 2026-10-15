from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from catalog.models import Product, Category


class ProductCreateView(CreateView):
    model = Product
    fields = ['product_name', 'description', 'product_image', 'product_category', 'price_per_unit']
    template_name = 'catalog/product/create.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product/detail.html'
    context_object_name = 'category'

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['product_name', 'description', 'product_image', 'product_category', 'price_per_unit']
    template_name = 'catalog/product/update.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product/delete.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product/products_category.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs['pk']
        return Product.objects.filter(product_category_id=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, pk=self.kwargs['pk'])
        return context