from django.urls import path, re_path

from . import views
from .models import Post

app_name = 'blog'

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    re_path(r'^post/(?P<year>[0-9]{4})/'
            r'(?P<month>[0-9]{1,2})/'
            r'(?P<day>[0-9]{1,2})/'
            r'(?P<slug>[\w\-]+)/$', views.post_detail, name='post_detail')
]