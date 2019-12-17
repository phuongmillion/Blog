from django.shortcuts import render, get_object_or_404, render_to_response, redirect

# Create your views here.
from django.views.generic.base import View

from .models import Tag, Startup, NewsLink
from .forms import TagForm, StartupForm, NewsLinkForm


class ObjectCreateMixin:
    form_class = None
    template = ''

    def get(self, request):
        return render(request, self.template, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_object = form.save()
            return redirect(new_object)
        else:
            return render(request, self.template, {'form': form})


class ObjectUpdateMixin:
    form_class = None
    model = None
    template = ''

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        context = {'form': self.form_class(instance=obj), self.model.__name__.lower(): obj}
        return render(request, self.template, context)

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        form = self.form_class(request.POST, instance=obj)
        if form.is_valid():
            new_object = form.save()
            return redirect(new_object)
        else:
            context = {'form': form, self.model.__name__.lower(): obj}
            return render(request, self.template, context)


def tag_list(request):
    return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)

    return render(request, 'organizer/tag_detail.html', {'tag': tag})


class TagCreate(ObjectCreateMixin, View):
    form_class = TagForm
    template = 'organizer/tag_form.html'


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


class StartupCreate(ObjectCreateMixin, View):
    form_class = StartupForm
    template = 'organizer/startup_form.html'


class NewsLinkCreate(ObjectCreateMixin, View):
    form_class = NewsLinkForm
    template = 'organizer/newslink_form.html'


class NewsLinkUpdate(View):
    form_class = NewsLinkForm
    model = NewsLink
    template = 'organizer/newslink_form_update.html'

    def get(self, request, pk):
        news_link = get_object_or_404(NewsLink, pk=pk)
        context = {'form': self.form_class(instance=news_link), 'newslink': news_link}
        return render(request, self.template, context)

    def post(self, request, pk):
        news_link = get_object_or_404(NewsLink, pk=pk)
        form = self.form_class(request.POST, instance=news_link)
        if form.is_valid():
            news_link = form.save()
            return redirect(news_link)
        else:
            return render(request, self.template, {'form': form, 'news_link': news_link})


class TagUpdate(ObjectUpdateMixin, View):
    form_class = TagCreate
    model = Tag
    template = 'organizer/tag_form_update.html'


class StartupUpdate(ObjectUpdateMixin, View):
    form_class = StartupForm
    model = Startup
    template = 'organizer/startup_form_update.html'
