from django.contrib import admin
from django.db import models
#
from tinymce.widgets import TinyMCE
#
from .models import BlogPost

class CustomAdmin(admin.ModelAdmin):
    fields = [
        'author',
        'title',
        'date_posted',
        'content',
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(BlogPost, CustomAdmin)

