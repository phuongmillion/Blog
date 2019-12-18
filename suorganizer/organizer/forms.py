from django import forms
from django.core.exceptions import ValidationError

from.models import Tag, NewsLink, Startup


class SlugCleanMixin:

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        return new_slug


class TagForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

    def clean_name(self):
        return self.cleaned_data['name'].lower()

    # def save(self):
    #     new_tag = Tag.objects.create(name=self.cleaned_data['name'], slug=self.cleaned_data['slug'])
    #     return new_tag


class NewsLinkForm(forms.ModelForm):
    class Meta:
        model = NewsLink
        fields = '__all__'

    # def save(self):
    #     news_link = NewsLink.objects.create(title=self.cleaned_data['title'], pub_date=self.cleaned_data['pub_date'],
    #                                  link=self.cleaned_data['link'], startups=self.cleaned_data['startups'])
    #     return news_link


class StartupForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Startup
        fields = '__all__'

    # def save(self):
    #     new_startup = Startup.objects.create(name=self.cleaned_data['name'], slug=self.cleaned_data['slug'],
    #                                          description=self.cleaned_data['description'], founded_date=self.cleaned_data['founded_date'],
    #                                          contact=self.cleaned_data['contact'], website=self.cleaned_data['website'])
    #     tags = self.cleaned_data['tags']
    #     new_startup.tags.set(tags)
    #     return new_startup
