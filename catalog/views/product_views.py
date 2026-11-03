from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from catalog.models import Product, Category
from catalog.forms import ProductForm


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product/create_product.html'
    permission_required = 'catalog.add_product'

    def form_valid(self, form):
        self.category_id = form.cleaned_data['product_category'].pk
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('catalog:product_list', kwargs={'pk': self.category_id})


class ProductDetailView(DetailView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product/product_detail.html'
    context_object_name = 'product'


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product/product_update.html'
    permission_required = 'catalog.change_product'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product/delete_product.html'
    permission_required = 'catalog.delete_product'

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
