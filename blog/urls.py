from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about-me', views.about, name="about-me"),
    path('contact', views.contact, name="contact"),
    path('tutorial', views.tutorial, name="tutorial"),
    path('blog', views.blog, name="blog"),
    path('blog/slug/<str:slug>', views.detail, name='detail'),
]