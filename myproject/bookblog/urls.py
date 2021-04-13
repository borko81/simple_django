from django.urls import path
from . views import post_list, post_detail, ListViewPublish, post_share

app_name = 'bookblog'
urlpatterns = [
    path('', post_list, name='post_list'),
    path('onlypublished/', ListViewPublish.as_view(), name='published_list'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    path('share/<int:post_id>/', post_share, name='share'),
]
