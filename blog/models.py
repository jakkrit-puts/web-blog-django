from django.db import models
from ckeditor.fields import RichTextField

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True, blank=False)
    date_updated = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return f'{self.tag_name}'

class Blog(models.Model):
    photo = models.ImageField(upload_to='Photo', default='')
    title = models.CharField(max_length=1000)
    slug = models.CharField(max_length=1000, default='')
    content = RichTextField()
    publish = models.BooleanField(default=False, blank=False)
    date = models.DateTimeField(auto_now_add=True, blank=False)
    date_updated = models.DateTimeField(auto_now=True, blank=False)
    short_detail = models.TextField(max_length=1000)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.title}'

