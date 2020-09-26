from django import forms
from django.contrib.auth.models import User
#
from tinymce.widgets import TinyMCE
#
from .models import BlogPost

class BlogCreateForm(forms.ModelForm):
    title = forms.CharField(max_length=100, label='Title: ', required=True)
    content = forms.CharField(widget=TinyMCE(mce_attrs={'width': 'autoresize'}), label='Content: ', required=True)

    class Meta():
        model = BlogPost
        fields = ['title', 'content']

class BlogUpdateForm(forms.ModelForm):
    title = forms.CharField(max_length=100, label='Title: ', required=True)
    content = forms.CharField(widget=TinyMCE(mce_attrs={'width': 'autoresize'}), label='Content: ', required=True)

    class Meta():
        model = BlogPost
        fields = ['title', 'content']