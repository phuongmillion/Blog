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


class PostUpdate(View):
    form_class = PostForm
    model = Post
    template = 'blog/post_form_update.html'

    def get_object(self, year, month, day, slug):
        return get_object_or_404(self.model, pub_date='-'.join([year, month, day]), slug=slug)

    def get(self, request, year, month, day, slug):
        post = self.get_object(year, month, day, slug)
        context = {'form': self.form_class(instance=post), 'post': post}
        return render(request, self.template, context)

    def post(self, request, year, month, day, slug):
        post = self.get_object(year, month, day, slug)
        form = self.form_class(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save()
            return redirect(new_post)
        else:
            context = {'form': form, 'post': post}
            return render(request, self.template, context)


class PostDelete(View):
    form_class = PostForm
    model = Post
    template = 'blog/post_confirm_delete.html'

    def get_object(self, year, month, day, slug):
        return get_object_or_404(self.model, pub_date='-'.join([year, month, day]), slug=slug)

    def get(self, request, year, month, day, slug):
        post = self.get_object(year, month, day, slug)
        return render(request, self.template, {'post': post})

    def post(self, request, year, month, day, slug):
        post = self.get_object(year, month, day, slug)
        post.delete()
        return redirect('blog:post_list')

