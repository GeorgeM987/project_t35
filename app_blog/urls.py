from django.urls import path
from .views import *

app_name = 'app_blog'

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('blog/<int:pk>/blog_detail/', blog_detail, name='blog_detail'),
    path('blog/<int:pk>/user_details/', blog_user_detail, name='blog_user_detail'),
    path('blog/<int:pk>/blog_create/', blog_create, name='blog_create'),
    path('blog/<int:pk>/blog_update/', blog_update, name='blog_update'),
    path('blog/<int:pk>/blog_delete/', blog_delete, name='blog_delete'),
]