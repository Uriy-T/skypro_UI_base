from django.urls import path
from blog.views import CreateArticleView, DetailArticleView, UpdateArticleView, DeleteArticleView, ListArticleView

app_name = 'blog'

urlpatterns = [
    path('article/create/', CreateArticleView.as_view(), name='article_create'),
    path('article/detail/<int:id>', DetailArticleView.as_view(), name='article_detail'),
    path('article/update/<int:id>', UpdateArticleView.as_view(), name='article_update'),
    path('article/delete/<int:id>', DeleteArticleView.as_view(), name='article_delete'),
    path('article/list/', ListArticleView.as_view(), name='article_list')
]
