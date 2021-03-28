from django.db.models import query
from django.shortcuts import render

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Article

class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()

class ArticleDetail(DetailView):
    template_name = 'blog/detail_view.html'
    model = Article
