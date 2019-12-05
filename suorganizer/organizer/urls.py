from django.urls import path

from . import views

app_name = 'organizer'

urlpatterns = [
    path('', views.tag_list, name='tag_list'),
    path('tag/<str:slug>', views.tag_detail, name='tag_detail'),
]

