from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.utils.decorators import method_decorator
from django.core.cache import cache
from catalog.models import Product, Category
from catalog.forms import ProductForm


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product/create_product.html'
    permission_required = 'catalog.add_product'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user
        self.category_id = form.cleaned_data['product_category'].pk
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('catalog:product_list', kwargs={'pk': self.category_id})

@method_decorator(vary_on_cookie, name='dispatch')
@method_decorator(cache_page(60 * 5), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product/product_detail.html'
    context_object_name = 'product'


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product/product_update.html'

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.has_perm('catalog.change_product')

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


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'catalog/product/delete_product.html'

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.has_perm('catalog.delete_product')

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
        cache_key = f'products_queryset_category_{category_id}'
        queryset = cache.get(cache_key)

        if not queryset:
            queryset = list(Product.objects.filter(product_category_id=category_id))
            cache.set(cache_key, queryset, 60 * 5)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, pk=self.kwargs['pk'])
        return context
