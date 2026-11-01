from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.models import Category


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['category_name', 'description']
    template_name = 'catalog/category/create_category.html'
    success_url = reverse_lazy('catalog:category_list')

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'catalog/category/category_detail.html'
    context_object_name = 'category'

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['category_name', 'description']
    template_name = 'catalog/category/category_update.html'

    def get_success_url(self):
        return reverse_lazy('catalog:category_detail', kwargs={'pk': self.object.pk})

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'catalog/category/delete_category.html'
    success_url = reverse_lazy('catalog:category_list')

class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category/category_list.html'
    context_object_name = 'categories'
