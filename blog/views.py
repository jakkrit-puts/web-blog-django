from django.shortcuts import render
from blog.models import Blog

def index(request):
    blog = Blog.objects.filter(publish=True)
    data = {
        "blog":blog
    }
    return render(request, 'index.html', {'data':data})

def detail(request, slug=None):
    blog = Blog.objects.filter(slug=slug)
    data = {
        "blog":blog
    }
    return render(request, 'blog/detail.html', {'data':data})

def about(request):
    print('about')
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def tutorial(request):
    return render(request, 'tutorial.html')

def blog(request):
    return render(request, 'blog.html')