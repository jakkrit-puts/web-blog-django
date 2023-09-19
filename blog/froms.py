from ckeditor.widgets import CKEditorWidget
from django import forms
from blog.models import Blog
from django.contrib import admin

class PostAdminForm(forms.ModelForm):
    news_detail = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blog
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    news_detail = PostAdminForm