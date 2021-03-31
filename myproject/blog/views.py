from django.db.models import query
from django.shortcuts import render


from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from django.views.generic.base import View

from .models import Article


class ArticleListView(View):
    """ Raw list view """
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):

        context = {
            'obj': self.get_queryset()
        }
        return render(request, self.template_name, context)


class ArtcileFirstOfThemView(ArticleListView):
    """ Inherit from ArticleListView show only first """
    queryset = Article.objects.filter(id=1)


# class ArticleListView(ListView):
#     template_name = 'blog/article_list.html'
#     queryset = Article.objects.all()

class ArticleDetail(DetailView):
    template_name = 'blog/detail_view.html'
    model = Article
