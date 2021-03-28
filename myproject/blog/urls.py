from django.urls import path
from .views import ArticleListView, ArticleDetail

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:pk>/detail/', ArticleDetail.as_view(), name='article-detail'),
    # path('create/', name='article-create'),
    # path('<int:id>/', name='article-detail'),
    # path('<int:id>/update/', name='article-update'),
    # path('<int:id>/delete/', name='article-delete'),
]
