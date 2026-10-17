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
    template_name = 'catalog/product/product_detail.html'
    context_object_name = 'product'

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['product_name', 'description', 'product_image', 'product_category', 'price_per_unit']
    template_name = 'catalog/product/product_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product/delete_product.html'

    def form_valid(self, form):
        self.category_id = self.object.product_category_id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('catalog:product_list', kwargs={'pk': self.category_id})


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
