from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic

from .models import Post


def post_list(request):
    return render(request, 'blog/post_list.html', {'post_list': Post.objects.all()})

# class PostList(generic.ListView):


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, pub_date='-'.join([year, month, day]), slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
