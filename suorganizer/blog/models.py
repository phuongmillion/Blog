from django.db import models

# Create your models here.
from django.urls import reverse
from organizer.models import Startup, Tag


class Post(models.Model):
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    startups = models.ManyToManyField(Startup, related_name='blog_posts')

    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63, help_text='A label for URL config', unique_for_month='pub_date')
    text = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True)

    def __str__(self):
        return "{} on {}".format(self.title, self.pub_date.strftime('%Y-%m-%d'))

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       kwargs={'year': self.pub_date.year, 'month': self.pub_date.month, 'day':self.pub_date.day, 'slug': self.slug})

    class Meta:
        verbose_name = 'blog post'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'

    def get_update_url(self):
        return reverse('blog:post_update',
                       kwargs={'year': self.pub_date.year, 'month': self.pub_date.month, 'day':self.pub_date.day, 'slug': self.slug})

