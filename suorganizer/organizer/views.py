from django.shortcuts import render, get_object_or_404, render_to_response, redirect

# Create your views here.
from django.views.generic.base import View

from .models import Tag, Startup
from .forms import TagForm, StartupForm


def tag_list(request):
    return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)

    return render(request, 'organizer/tag_detail.html', {'tag': tag})


class TagCreate(View):
    form_class = TagForm
    template = 'organizer/tag_form.html'

    def get(self, request):
        return render(request, self.template, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_tag = form.save()
            return redirect(new_tag)
        else:
            return render(request, self.template, {'form': form})

# def tag_create(request):
#     if request.method == 'POST':
#         form = TagForm(request.POST)
#         if form.is_valid():
#             tag = form.save()
#             return redirect(tag)
#     else:
#         form = TagForm()
#     return render(request, 'organizer/tag_form.html', {'form': form})


def startup_list(request):
    return render(request, 'organizer/startup_list.html', {'startup_list': Startup.objects.all()})


def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)

    return render(request, 'organizer/startup_detail.html', {'startup': startup})


class StartupCreate(View):
    form_class = StartupForm
    template = 'organizer/startup_form.html'

    def get(self, request):
        return render(request, self.template, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_startup = form.save()
            return redirect(new_startup)
        else:
            return render(request, self.template, {'form': form})
