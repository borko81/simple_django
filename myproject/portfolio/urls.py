from django.conf.urls import url
from django.urls import path


from .views import (
    hello_world
)

app_name = 'portfolio'
urlpatterns = [
    path('', hello_world, name='hello'),
]
