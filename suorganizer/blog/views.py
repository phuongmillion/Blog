from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import generic
from django.views.generic.base import View

from .forms import PostForm
from .models import Post


def post_list(request):
    return render(request, 'blog/post_list.html', {'post_list': Post.objects.all()})

# class PostList(generic.ListView):


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, pub_date='-'.join([year, month, day]), slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})


class PostCreate(View):
    form_class = PostForm
    template = 'blog/post_form.html'

    def get(self, request):
        return render(request, self.template, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_post = form.save()
            return redirect(new_post)
        else:
            return render(request, self.template, {'form': form})

