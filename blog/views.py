from django.shortcuts import render
from blog.models import Blog

def index(request):
    blog = Blog.objects.filter(publish=True)
    data = {
        "blog":blog
    }
    return render(request, 'index.html', {'data':data})

def detail(request, id=None):
    blog = Blog.objects.filter(id=id)
    data = {
        "blog":blog
    }
    return render(request, 'detail.html', {'data':data})