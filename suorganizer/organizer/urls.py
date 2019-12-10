from django.urls import path

from . import views

app_name = 'organizer'

urlpatterns = [
    path('tag/', views.tag_list, name='tag_list'),
    path('tag/create/', views.tag_create, name='tag_create'),
    path('tag/<slug:slug>', views.tag_detail, name='tag_detail'),
    path('startup/', views.startup_list, name='startup_list'),
    path('startup/<slug:slug>', views.startup_detail, name='startup_detail'),
]

