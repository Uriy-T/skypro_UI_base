from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from blog.models import ArticleModel


class CreateArticleView(CreateView):
    model = ArticleModel
    fields = ['title', 'content', 'preview_image', 'is_public']
    template_name = 'blog/article/create_article.html'
    success_url = reverse_lazy('blog:article_list')


class DetailArticleView(DetailView):
    model = ArticleModel
    template_name = 'blog/article/detail_article.html'
    context_object_name = 'article'


class UpdateArticleView(UpdateView):
    model = ArticleModel
    fields = ['title', 'content', 'preview_image', 'is_public']
    template_name = 'blog/article/update_article.html'
    context_object_name = 'article'
    success_url = reverse_lazy('blog:article_list')


class DeleteArticleView(DeleteView):
    model = ArticleModel
    template_name = 'blog/article/delete_article.html'
    context_object_name = 'article'
    success_url = reverse_lazy('blog:article_list')


class ListArticleView(ListView):
    model = ArticleModel
    template_name = 'blog/article/list_article.html'
    context_object_name = 'articles'
    queryset = ArticleModel.objects.filter(is_public=True)
