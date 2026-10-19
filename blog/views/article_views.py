from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from blog.models import ArticleModel
from django.core.mail import send_mail
from django.db.models import F
import os
from dotenv import load_dotenv

load_dotenv(override=True)

class CreateArticleView(CreateView):
    model = ArticleModel
    fields = ['title', 'content', 'preview_image', 'is_public']
    template_name = 'blog/article/create_article.html'
    success_url = reverse_lazy('blog:article_list')


class DetailArticleView(DetailView):
    model = ArticleModel
    template_name = 'blog/article/detail_article.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        old_view_count = obj.view_count
        ArticleModel.objects.filter(pk=obj.pk).update(view_count=F('view_count') + 1)
        obj.view_count += 1

        if old_view_count < 100 and obj.view_count>= 100 and not obj.is_reach_count:
            send_mail(
                subject=f'Тест. Статья "{obj.title}" набрала 100 просмотров.',
                message=f'Сообщение из учебного приложения. Статья достигла необходимого уровня в {obj.view_count} просмотров.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.SEND_EMAIL],
                fail_silently=False,
            )

            obj.is_reach_count = True
            obj.save(update_fields=['is_reach_count'])

        return obj

class UpdateArticleView(UpdateView):
    model = ArticleModel
    fields = ['title', 'content', 'preview_image', 'is_public']
    template_name = 'blog/article/update_article.html'
    context_object_name = 'article'

    def get_success_url(self):
        return reverse_lazy('blog:article_detail', kwargs={'pk': self.object.pk})


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
