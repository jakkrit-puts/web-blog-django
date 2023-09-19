from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/slug/<int:id>', views.detail, name='detail'),
]