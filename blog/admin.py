from django.contrib import admin
from blog.models import Blog, Tag
from blog.froms import PostAdmin

# Register your models here.
admin.site.register(Blog, PostAdmin)
admin.site.register(Tag)