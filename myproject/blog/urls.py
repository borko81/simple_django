from django.urls import path
from .views import (
    ArticleListView, ArticleDetail, ArtcileFirstOfThemView,
    ArticlePost
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('first/', ArtcileFirstOfThemView.as_view(), name='article-first'),
    path('<int:pk>/detail/', ArticleDetail.as_view(), name='article-detail'),
    path('create/', ArticlePost.as_view(), name='article-create'),
    # path('<int:id>/', name='article-detail'),
    # path('<int:id>/update/', name='article-update'),
    # path('<int:id>/delete/', name='article-delete'),
]
