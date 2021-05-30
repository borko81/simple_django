from django.urls import path
from .views import index, like

app_name = 'posts'
urlpatterns = [
    path('', index, name='index'),
    path('like/', like, name='like')
]