from django.urls import path

from . import views

app_name = 'organizer'

urlpatterns = [
    path('tag/', views.tag_list, name='tag_list'),
    path('tag/create/', views.TagCreate.as_view(), name='tag_create'),
    path('tag/<slug:slug>', views.tag_detail, name='tag_detail'),
    path('startup/', views.startup_list, name='startup_list'),
    path('startup/<slug:slug>', views.startup_detail, name='startup_detail'),
    path('startup/create/', views.StartupCreate.as_view(), name='startup_create'),
    path('newslink/create/', views.NewsLinkCreate.as_view(), name='newslink_create'),
]

