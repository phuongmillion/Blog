from django.shortcuts import render, get_object_or_404, render_to_response

# Create your views here.
from .models import Tag, Startup
from .forms import TagForm


def tag_list(request):
    return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)

    return render(request, 'organizer/tag_detail.html', {'tag': tag})


def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        print(form.errors.as_json())
        print(form.errors)
        if form.errors:
            return render(request, 'organizer/tag_form.html', {'form': form})
        else:
            return render(request, 'organizer/tag_form.html', {'form': form})
    else:
        form = TagForm()
        return render(request, 'organizer/tag_form.html', {'form': form})


def startup_list(request):
    return render(request, 'organizer/startup_list.html', {'startup_list': Startup.objects.all()})


def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)

    return render(request, 'organizer/startup_detail.html', {'startup': startup})
