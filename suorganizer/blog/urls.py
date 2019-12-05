from django.urls import path, register_converter

from . import views
from .models import Post

app_name = 'blog'

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    path('blog/<int:year>/<int:month>/<slug:slug>', views.post_detail, name='post_detail')
]